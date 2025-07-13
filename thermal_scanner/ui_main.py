"""
Main UI module cho thermal camera application
Giao diện Tkinter với dark mode theme
"""

import tkinter as tk
from tkinter import ttk, messagebox
import cv2
from PIL import Image, ImageTk
import threading
import os
from camera_handler import ThermalCameraHandler
from utils.logger import logger


class ThermalCameraUI:
    """Main UI class cho thermal camera application"""
    
    def __init__(self):
        """Khởi tạo UI"""
        self.root = tk.Tk()
        self.camera_handler = ThermalCameraHandler()
        
        # UI state
        self.is_camera_running = False
        self.current_photo = None
        
        # Dark mode colors
        self.colors = {
            'bg': '#2b2b2b',
            'fg': '#ffffff',
            'button_bg': '#404040',
            'button_fg': '#ffffff',
            'button_active': '#505050',
            'frame_bg': '#1e1e1e',
            'border': '#555555'
        }
        
        self._setup_ui()
        self._setup_styles()
        
        logger.info("Thermal camera UI initialized")
    
    def _setup_ui(self):
        """Setup main UI components"""
        # Main window configuration
        self.root.title("Thermal Camera Simulator")
        self.root.geometry("1200x900")
        self.root.configure(bg=self.colors['bg'])
        self.root.resizable(True, True)
        
        # Main frame
        self.main_frame = tk.Frame(
            self.root, 
            bg=self.colors['bg'],
            padx=10,
            pady=10
        )
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        self.title_label = tk.Label(
            self.main_frame,
            text="🔥 Thermal Camera Simulator",
            font=("Arial", 16, "bold"),
            bg=self.colors['bg'],
            fg=self.colors['fg']
        )
        self.title_label.pack(pady=(0, 10))
        
        # Video display frame - chiếm toàn bộ không gian
        self.video_frame = tk.Frame(
            self.main_frame,
            bg=self.colors['frame_bg'],
            relief=tk.RAISED,
            bd=2
        )
        self.video_frame.pack(pady=5, padx=5, fill=tk.BOTH, expand=True)
        
        # Video label - chiếm toàn bộ frame
        self.video_label = tk.Label(
            self.video_frame,
            text="Camera Preview\nPress 'Start' to begin",
            font=("Arial", 16),
            bg=self.colors['frame_bg'],
            fg=self.colors['fg']
        )
        self.video_label.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Control buttons frame
        self.control_frame = tk.Frame(
            self.main_frame,
            bg=self.colors['bg']
        )
        self.control_frame.pack(pady=10)
        
        # Buttons
        self._create_buttons()
        
        # Status frame
        self.status_frame = tk.Frame(
            self.main_frame,
            bg=self.colors['bg']
        )
        self.status_frame.pack(pady=(10, 0), fill=tk.X)
        
        # Status label
        self.status_label = tk.Label(
            self.status_frame,
            text="Status: Ready",
            font=("Arial", 10),
            bg=self.colors['bg'],
            fg=self.colors['fg'],
            anchor=tk.W
        )
        self.status_label.pack(side=tk.LEFT)
        
        # Info label
        self.info_label = tk.Label(
            self.status_frame,
            text="Night mode: Auto-detect | Thermal effect: Active",
            font=("Arial", 9),
            bg=self.colors['bg'],
            fg='#cccccc',
            anchor=tk.E
        )
        self.info_label.pack(side=tk.RIGHT)
    
    def _create_buttons(self):
        """Tạo các control buttons"""
        button_config = {
            'font': ("Arial", 11, "bold"),
            'bg': self.colors['button_bg'],
            'fg': self.colors['button_fg'],
            'activebackground': self.colors['button_active'],
            'activeforeground': self.colors['button_fg'],
            'relief': tk.RAISED,
            'bd': 2,
            'padx': 20,
            'pady': 8,
            'cursor': 'hand2'
        }
        
        # Start button
        self.start_btn = tk.Button(
            self.control_frame,
            text="▶ Start",
            command=self._start_camera,
            **button_config
        )
        self.start_btn.pack(side=tk.LEFT, padx=5)
        
        # Stop button
        self.stop_btn = tk.Button(
            self.control_frame,
            text="⏸ Stop",
            command=self._stop_camera,
            state=tk.DISABLED,
            **button_config
        )
        self.stop_btn.pack(side=tk.LEFT, padx=5)
        
        # Capture button
        self.capture_btn = tk.Button(
            self.control_frame,
            text="📸 Capture",
            command=self._capture_image,
            state=tk.DISABLED,
            **button_config
        )
        self.capture_btn.pack(side=tk.LEFT, padx=5)
        
        # Exit button
        self.exit_btn = tk.Button(
            self.control_frame,
            text="❌ Exit",
            command=self._exit_application,
            bg='#8B0000',
            activebackground='#A52A2A',
            **{k: v for k, v in button_config.items() if k not in ['bg', 'activebackground']}
        )
        self.exit_btn.pack(side=tk.LEFT, padx=5)
    
    def _setup_styles(self):
        """Setup ttk styles cho dark mode"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure styles
        style.configure('Dark.TFrame', background=self.colors['bg'])
        style.configure('Dark.TLabel', background=self.colors['bg'], foreground=self.colors['fg'])
    
    def _start_camera(self):
        """Start camera capture"""
        try:
            self._update_status("Starting camera...")
            
            # Start camera in separate thread để không block UI
            def start_camera_thread():
                success = self.camera_handler.start_capture(self._update_frame)
                
                if success:
                    self.is_camera_running = True
                    self.root.after(0, self._on_camera_started)
                else:
                    self.root.after(0, lambda: self._update_status("Failed to start camera"))
                    messagebox.showerror("Error", "Cannot start camera. Please check if camera is available.")
            
            threading.Thread(target=start_camera_thread, daemon=True).start()
            
        except Exception as e:
            logger.error(f"Error starting camera: {e}")
            messagebox.showerror("Error", f"Failed to start camera: {e}")
    
    def _on_camera_started(self):
        """Callback khi camera đã start thành công"""
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.capture_btn.config(state=tk.NORMAL)
        self._update_status("Camera running - Thermal mode active")
        logger.info("Camera started successfully")
    
    def _stop_camera(self):
        """Stop/pause camera capture"""
        try:
            if self.is_camera_running:
                self.camera_handler.pause_capture()
                
                self.start_btn.config(state=tk.NORMAL)
                self.stop_btn.config(state=tk.DISABLED)
                self.capture_btn.config(state=tk.DISABLED)
                
                self._update_status("Camera stopped - Last frame displayed")
                logger.info("Camera stopped")
            
        except Exception as e:
            logger.error(f"Error stopping camera: {e}")
            messagebox.showerror("Error", f"Failed to stop camera: {e}")
    
    def _capture_image(self):
        """Capture current frame"""
        try:
            if not self.is_camera_running:
                messagebox.showwarning("Warning", "Camera is not running")
                return
            
            filepath = self.camera_handler.capture_image()
            
            if filepath:
                self._update_status(f"Image saved: {os.path.basename(filepath)}")
                messagebox.showinfo("Success", f"Image captured and saved:\n{filepath}")
            else:
                messagebox.showerror("Error", "Failed to capture image")
                
        except Exception as e:
            logger.error(f"Error capturing image: {e}")
            messagebox.showerror("Error", f"Failed to capture image: {e}")
    
    def _update_frame(self, frame):
        """
        Update video display với frame mới
        
        Args:
            frame (numpy.ndarray): Frame từ camera
        """
        try:
            # Convert OpenCV frame (BGR) to PIL Image (RGB)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(frame_rgb)
            
            # Tính toán kích thước để fit toàn bộ video frame
            frame_width = self.video_label.winfo_width()
            frame_height = self.video_label.winfo_height()
            
            # Nếu chưa có kích thước thì dùng mặc định lớn
            if frame_width <= 1 or frame_height <= 1:
                display_size = (1000, 750)
            else:
                # Giữ tỷ lệ khung hình 4:3
                aspect_ratio = 4/3
                if frame_width/frame_height > aspect_ratio:
                    display_width = int(frame_height * aspect_ratio)
                    display_height = frame_height
                else:
                    display_width = frame_width
                    display_height = int(frame_width / aspect_ratio)
                
                display_size = (max(display_width-10, 640), max(display_height-10, 480))
            
            pil_image = pil_image.resize(display_size, Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage
            photo = ImageTk.PhotoImage(pil_image)
            
            # Update label
            self.video_label.configure(image=photo, text="")
            self.video_label.image = photo  # Keep reference
            
        except Exception as e:
            logger.error(f"Error updating frame: {e}")
    
    def _update_status(self, message):
        """Update status label"""
        self.status_label.config(text=f"Status: {message}")
        self.root.update_idletasks()
    
    def _exit_application(self):
        """Exit application với cleanup"""
        try:
            # Confirm exit
            if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
                self._update_status("Shutting down...")
                
                # Stop camera
                if self.is_camera_running:
                    self.camera_handler.stop_capture()
                
                logger.info("Application exiting")
                self.root.quit()
                self.root.destroy()
                
        except Exception as e:
            logger.error(f"Error during exit: {e}")
            self.root.quit()
    
    def run(self):
        """Start UI main loop"""
        try:
            # Handle window close event
            self.root.protocol("WM_DELETE_WINDOW", self._exit_application)
            
            logger.info("Starting UI main loop")
            self.root.mainloop()
            
        except Exception as e:
            logger.error(f"Error in UI main loop: {e}")
        finally:
            # Cleanup
            if hasattr(self, 'camera_handler'):
                self.camera_handler.stop_capture()
