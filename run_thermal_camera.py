#!/usr/bin/env python3
"""
Launcher script cho Thermal Camera Simulator
Chạy file này để khởi động ứng dụng
"""

import sys
import os

# Add thermal_scanner to path
current_dir = os.path.dirname(os.path.abspath(__file__))
thermal_scanner_path = os.path.join(current_dir, 'thermal_scanner')
sys.path.insert(0, thermal_scanner_path)

# Import và chạy main
from main import main

if __name__ == "__main__":
    main()
