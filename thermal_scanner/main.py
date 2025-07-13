"""
Main entry point cho Thermal Camera Simulator
Khởi chạy ứng dụng với error handling và logging
"""

import sys
import os
import traceback

# Add current directory to path để import modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from ui_main import ThermalCameraUI
    from utils.logger import logger
except ImportError as e:
    print(f"Import error: {e}")
    print("Please make sure all required packages are installed:")
    print("pip install -r requirements.txt")
    sys.exit(1)


def check_dependencies():
    """Kiểm tra các dependencies cần thiết"""
    required_modules = ['cv2', 'PIL', 'numpy', 'tkinter']
    missing_modules = []
    
    for module in required_modules:
        try:
            if module == 'PIL':
                import PIL
            elif module == 'cv2':
                import cv2
            elif module == 'numpy':
                import numpy
            elif module == 'tkinter':
                import tkinter
        except ImportError:
            missing_modules.append(module)
    
    if missing_modules:
        logger.error(f"Missing required modules: {missing_modules}")
        print(f"Error: Missing required modules: {missing_modules}")
        print("Please install them using: pip install -r requirements.txt")
        return False
    
    return True


def main():
    """Main function"""
    try:
        logger.info("=" * 50)
        logger.info("Starting Thermal Camera Simulator")
        logger.info("=" * 50)
        
        # Check dependencies
        if not check_dependencies():
            return 1
        
        # Create and run UI
        app = ThermalCameraUI()
        app.run()
        
        logger.info("Application closed successfully")
        return 0
        
    except KeyboardInterrupt:
        logger.info("Application interrupted by user")
        return 0
        
    except Exception as e:
        logger.critical(f"Unexpected error: {e}")
        logger.critical(f"Traceback: {traceback.format_exc()}")
        print(f"Critical error: {e}")
        print("Check logs for more details")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
