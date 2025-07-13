"""
Logger module cho thermal camera application
Cung cấp logging functionality với các level khác nhau
"""

import logging
import os
from datetime import datetime


class ThermalLogger:
    """Logger class cho thermal camera application"""
    
    def __init__(self, name="ThermalCamera", log_file=None):
        """
        Khởi tạo logger
        
        Args:
            name (str): Tên logger
            log_file (str): Đường dẫn file log (optional)
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        # Tránh duplicate handlers
        if not self.logger.handlers:
            self._setup_handlers(log_file)
    
    def _setup_handlers(self, log_file):
        """Setup console và file handlers"""
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # File handler (nếu có)
        if log_file:
            # Tạo thư mục logs nếu chưa có
            os.makedirs(os.path.dirname(log_file), exist_ok=True)
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.DEBUG)
            
            # Format cho file
            file_formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            file_handler.setFormatter(file_formatter)
            self.logger.addHandler(file_handler)
        
        # Format cho console
        console_formatter = logging.Formatter(
            '%(levelname)s - %(message)s'
        )
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)
    
    def info(self, message):
        """Log info message"""
        self.logger.info(message)
    
    def debug(self, message):
        """Log debug message"""
        self.logger.debug(message)
    
    def warning(self, message):
        """Log warning message"""
        self.logger.warning(message)
    
    def error(self, message):
        """Log error message"""
        self.logger.error(message)
    
    def critical(self, message):
        """Log critical message"""
        self.logger.critical(message)


# Global logger instance
logger = ThermalLogger(
    name="ThermalCamera",
    log_file=f"logs/thermal_camera_{datetime.now().strftime('%Y%m%d')}.log"
)
