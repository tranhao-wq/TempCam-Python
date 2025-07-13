"""
Camera handler module
Xử lý camera operations và thermal effects
"""

import cv2
import numpy as np
import threading
import time
from datetime import datetime
import os
from night_mode import NightModeProcessor
from utils.logger import logger


class ThermalCameraHandler:
    """Class xử lý camera và thermal effects"""
    
    def __init__(self, camera_index=0):
        """
        Khởi tạo camera handler
        
        Args:
            camera_index (int): Index của camera (default: 0)
        """
        self.camera_index = camera_index
        self.cap = None
        self.is_running = False
        self.is_capturing = False
        self.current_frame = None
        self.thermal_frame = None
        self.frame_callback = None
        
        # Night mode processor
        self.night_processor = NightModeProcessor()
        
        # Threading
        self.capture_thread = None
        self.thread_lock = threading.Lock()
        
        # Frame rate control - giảm FPS để ổn định hơn
        self.fps = 15
        self.frame_delay = 1.0 / self.fps
        
        logger.info(f"Thermal camera handler initialized for camera {camera_index}")
    
    def initialize_camera(self):
        """
        Khởi tạo camera với fallback cho nhiều camera index
        
        Returns:
            bool: True nếu khởi tạo thành công
        """
        # Thử các camera index khác nhau
        camera_indices = [0, 1, 2, -1]  # -1 cho DirectShow trên Windows
        
        for idx in camera_indices:
            try:
                logger.info(f"Trying camera index: {idx}")
                
                # Thử với DirectShow backend trên Windows
                if idx == -1:
                    self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                else:
                    self.cap = cv2.VideoCapture(idx)
                
                # Đợi một chút để camera khởi tạo
                time.sleep(0.5)
                
                if self.cap.isOpened():
                    # Test đọc frame
                    ret, frame = self.cap.read()
                    if ret and frame is not None:
                        # Set camera properties
                        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
                        self.cap.set(cv2.CAP_PROP_FPS, 15)  # Giảm FPS để ổn định hơn
                        
                        self.camera_index = idx if idx != -1 else 0
                        logger.info(f"Camera initialized successfully with index: {self.camera_index}")
                        return True
                
                # Nếu không thành công, release và thử tiếp
                if self.cap:
                    self.cap.release()
                    self.cap = None
                    
            except Exception as e:
                logger.warning(f"Failed to initialize camera {idx}: {e}")
                if self.cap:
                    self.cap.release()
                    self.cap = None
        
        logger.error("Cannot initialize any camera")
        return False
    
    def start_capture(self, frame_callback=None):
        """
        Bắt đầu capture video
        
        Args:
            frame_callback (function): Callback function để xử lý frame
            
        Returns:
            bool: True nếu start thành công
        """
        if self.is_running:
            logger.warning("Camera is already running")
            return True
        
        if not self.initialize_camera():
            logger.error("Failed to initialize camera")
            return False
        
        self.frame_callback = frame_callback
        self.is_running = True
        self.is_capturing = True
        
        # Start capture thread
        self.capture_thread = threading.Thread(target=self._capture_loop)
        self.capture_thread.daemon = True
        self.capture_thread.start()
        
        logger.info("Camera capture started")
        return True
    
    def _capture_loop(self):
        """Main capture loop chạy trong thread riêng"""
        last_frame_time = time.time()
        
        while self.is_running and self.cap and self.cap.isOpened():
            try:
                # Frame rate control
                current_time = time.time()
                if current_time - last_frame_time < self.frame_delay:
                    time.sleep(0.001)  # Small sleep to prevent busy waiting
                    continue
                
                ret, frame = self.cap.read()
                if not ret:
                    logger.warning("Failed to read frame from camera")
                    continue
                
                # Process frame
                processed_frame = self._process_frame(frame)
                
                # Thread-safe frame update
                with self.thread_lock:
                    self.current_frame = frame.copy()
                    self.thermal_frame = processed_frame.copy()
                
                # Callback to UI
                if self.frame_callback and self.is_capturing:
                    self.frame_callback(processed_frame)
                
                last_frame_time = current_time
                
            except Exception as e:
                logger.error(f"Error in capture loop: {e}")
                break
        
        logger.info("Capture loop ended")
    
    def _process_frame(self, frame):
        """
        Xử lý frame để tạo thermal effect thực tế
        
        Args:
            frame (numpy.ndarray): Frame gốc
            
        Returns:
            numpy.ndarray: Frame với thermal effect
        """
        try:
            # Detect low light condition
            is_low_light = self.night_processor.detect_low_light(frame)
            
            if is_low_light:
                # Night mode: Thermal scanning với màu lạnh
                thermal = self._create_night_thermal(frame)
            else:
                # Day mode: Thermal scanning với màu nóng
                thermal = self._create_day_thermal(frame)
            
            return thermal
            
        except Exception as e:
            logger.error(f"Error processing frame: {e}")
            return frame
    
    def _create_night_thermal(self, frame):
        """
        Tạo thermal effect cho ban đêm (màu lạnh - xanh/tím)
        """
        # Enhance cho điều kiện ánh sáng thấp
        enhanced = self.night_processor.enhance_low_light_image(frame)
        
        # Convert sang grayscale
        gray = cv2.cvtColor(enhanced, cv2.COLOR_BGR2GRAY)
        
        # Tạo thermal map dựa trên độ sáng
        # Vùng sáng = nóng (màu trắng/vàng), vùng tối = lạnh (màu xanh/tím)
        thermal_map = np.zeros_like(frame, dtype=np.uint8)
        
        # Normalize gray values
        normalized = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX)
        
        # Tạo gradient màu từ lạnh đến nóng
        for i in range(frame.shape[0]):
            for j in range(frame.shape[1]):
                intensity = normalized[i, j]
                
                if intensity < 50:  # Rất lạnh - xanh đậm
                    thermal_map[i, j] = [intensity, 0, 100]
                elif intensity < 100:  # Lạnh - xanh nhạt
                    thermal_map[i, j] = [intensity, intensity//2, 150]
                elif intensity < 150:  # Ấm - tím
                    thermal_map[i, j] = [intensity, intensity//3, 200]
                elif intensity < 200:  # Nóng - đỏ
                    thermal_map[i, j] = [50, intensity//4, intensity]
                else:  # Rất nóng - trắng/vàng
                    thermal_map[i, j] = [100, intensity//2, intensity]
        
        return thermal_map
    
    def _create_day_thermal(self, frame):
        """
        Tạo thermal effect cho ban ngày (màu nóng - đỏ/vàng)
        """
        # Convert sang grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Tạo thermal map dựa trên độ sáng và chuyển động
        thermal_map = np.zeros_like(frame, dtype=np.uint8)
        
        # Normalize gray values
        normalized = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX)
        
        # Tạo gradient màu từ lạnh đến nóng (phong cách ban ngày)
        for i in range(frame.shape[0]):
            for j in range(frame.shape[1]):
                intensity = normalized[i, j]
                
                if intensity < 60:  # Lạnh - xanh đen
                    thermal_map[i, j] = [intensity//2, 0, 0]
                elif intensity < 120:  # Ấm - đỏ đậm
                    thermal_map[i, j] = [0, 0, intensity]
                elif intensity < 180:  # Nóng - đỏ cam
                    thermal_map[i, j] = [0, intensity//3, intensity]
                elif intensity < 220:  # Rất nóng - vàng
                    thermal_map[i, j] = [0, intensity//2, intensity]
                else:  # Cực nóng - trắng
                    thermal_map[i, j] = [intensity//3, intensity//2, intensity]
        
        return thermal_map
    
    def pause_capture(self):
        """Tạm dừng capture (giữ frame cuối cùng)"""
        self.is_capturing = False
        logger.info("Camera capture paused")
    
    def resume_capture(self):
        """Tiếp tục capture"""
        if self.is_running:
            self.is_capturing = True
            logger.info("Camera capture resumed")
    
    def stop_capture(self):
        """Dừng capture hoàn toàn"""
        self.is_running = False
        self.is_capturing = False
        
        # Wait for thread to finish
        if self.capture_thread and self.capture_thread.is_alive():
            self.capture_thread.join(timeout=2.0)
        
        # Release camera
        if self.cap:
            self.cap.release()
            self.cap = None
        
        logger.info("Camera capture stopped")
    
    def capture_image(self, save_directory="captures"):
        """
        Chụp ảnh hiện tại và lưu file
        
        Args:
            save_directory (str): Thư mục lưu ảnh
            
        Returns:
            str: Đường dẫn file đã lưu hoặc None nếu lỗi
        """
        try:
            with self.thread_lock:
                if self.thermal_frame is None:
                    logger.warning("No frame available for capture")
                    return None
                
                frame_to_save = self.thermal_frame.copy()
            
            # Tạo thư mục nếu chưa có
            os.makedirs(save_directory, exist_ok=True)
            
            # Tạo filename với timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"thermal_capture_{timestamp}.jpg"
            filepath = os.path.join(save_directory, filename)
            
            # Lưu ảnh
            success = cv2.imwrite(filepath, frame_to_save)
            
            if success:
                logger.info(f"Image captured and saved: {filepath}")
                return filepath
            else:
                logger.error("Failed to save captured image")
                return None
                
        except Exception as e:
            logger.error(f"Error capturing image: {e}")
            return None
    
    def get_current_frame(self):
        """
        Lấy frame hiện tại (thread-safe)
        
        Returns:
            numpy.ndarray: Frame hiện tại hoặc None
        """
        with self.thread_lock:
            if self.thermal_frame is not None:
                return self.thermal_frame.copy()
            return None
    
    def is_camera_available(self):
        """
        Kiểm tra camera có sẵn không
        
        Returns:
            bool: True nếu camera available
        """
        return self.cap is not None and self.cap.isOpened()
    
    def __del__(self):
        """Destructor - cleanup resources"""
        self.stop_capture()
