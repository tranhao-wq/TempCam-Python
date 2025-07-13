"""
Night mode detection và image enhancement module
Xử lý phát hiện điều kiện ánh sáng thấp và cải thiện chất lượng ảnh
"""

import cv2
import numpy as np
from utils.logger import logger


class NightModeProcessor:
    """Class xử lý night mode detection và image enhancement"""
    
    def __init__(self, brightness_threshold=60):
        """
        Khởi tạo night mode processor
        
        Args:
            brightness_threshold (int): Ngưỡng độ sáng để detect night mode (0-255)
        """
        self.brightness_threshold = brightness_threshold
        self.alpha = 1.5  # Contrast multiplier
        self.beta = 30    # Brightness offset
        
        logger.info(f"Night mode processor initialized with threshold: {brightness_threshold}")
    
    def detect_low_light(self, frame):
        """
        Phát hiện điều kiện ánh sáng thấp
        
        Args:
            frame (numpy.ndarray): Frame ảnh input
            
        Returns:
            bool: True nếu là điều kiện ánh sáng thấp
        """
        try:
            # Convert sang grayscale để tính độ sáng trung bình
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            mean_brightness = np.mean(gray)
            
            is_low_light = mean_brightness < self.brightness_threshold
            
            if is_low_light:
                logger.debug(f"Low light detected: brightness={mean_brightness:.1f}")
            
            return is_low_light
            
        except Exception as e:
            logger.error(f"Error in low light detection: {e}")
            return False
    
    def enhance_low_light_image(self, frame):
        """
        Cải thiện chất lượng ảnh trong điều kiện ánh sáng thấp
        
        Args:
            frame (numpy.ndarray): Frame ảnh input
            
        Returns:
            numpy.ndarray: Frame ảnh đã được cải thiện
        """
        try:
            # 1. Tăng độ sáng và tương phản
            enhanced = cv2.convertScaleAbs(frame, alpha=self.alpha, beta=self.beta)
            
            # 2. Khử nhiễu
            # Convert sang grayscale để denoising
            gray = cv2.cvtColor(enhanced, cv2.COLOR_BGR2GRAY)
            denoised_gray = cv2.fastNlMeansDenoising(gray, None, 10, 7, 21)
            
            # Convert lại sang BGR
            denoised = cv2.cvtColor(denoised_gray, cv2.COLOR_GRAY2BGR)
            
            logger.debug("Low light image enhancement applied")
            return denoised
            
        except Exception as e:
            logger.error(f"Error in image enhancement: {e}")
            return frame
    
    def get_night_colormap(self):
        """
        Trả về colormap phù hợp cho night mode
        
        Returns:
            int: OpenCV colormap constant
        """
        return cv2.COLORMAP_INFERNO
    
    def get_day_colormap(self):
        """
        Trả về colormap phù hợp cho day mode
        
        Returns:
            int: OpenCV colormap constant
        """
        return cv2.COLORMAP_JET
    
    def adjust_threshold(self, new_threshold):
        """
        Điều chỉnh ngưỡng brightness threshold
        
        Args:
            new_threshold (int): Ngưỡng mới (0-255)
        """
        if 0 <= new_threshold <= 255:
            self.brightness_threshold = new_threshold
            logger.info(f"Brightness threshold adjusted to: {new_threshold}")
        else:
            logger.warning(f"Invalid threshold value: {new_threshold}. Must be 0-255")
    
    def adjust_enhancement_params(self, alpha=None, beta=None):
        """
        Điều chỉnh tham số enhancement
        
        Args:
            alpha (float): Contrast multiplier (optional)
            beta (int): Brightness offset (optional)
        """
        if alpha is not None and alpha > 0:
            self.alpha = alpha
            logger.info(f"Contrast multiplier adjusted to: {alpha}")
        
        if beta is not None:
            self.beta = beta
            logger.info(f"Brightness offset adjusted to: {beta}")
