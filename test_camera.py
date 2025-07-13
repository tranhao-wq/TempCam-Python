#!/usr/bin/env python3
"""
Script test camera đơn giản
"""

import cv2
import time

def test_camera():
    """Test camera với các index khác nhau"""
    print("Testing camera availability...")
    
    # Thử các camera index
    camera_indices = [0, 1, 2]
    
    for idx in camera_indices:
        print(f"\nTrying camera index: {idx}")
        
        try:
            # Thử với backend mặc định
            cap = cv2.VideoCapture(idx)
            time.sleep(0.5)
            
            if cap.isOpened():
                ret, frame = cap.read()
                if ret and frame is not None:
                    print(f"[OK] Camera {idx} works! Frame shape: {frame.shape}")
                    cap.release()
                    return idx
                else:
                    print(f"[FAIL] Camera {idx} opened but cannot read frame")
            else:
                print(f"[FAIL] Cannot open camera {idx}")
            
            cap.release()
            
        except Exception as e:
            print(f"[ERROR] Error with camera {idx}: {e}")
    
    # Thử với DirectShow (Windows)
    print(f"\nTrying DirectShow backend...")
    try:
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        time.sleep(1)
        
        if cap.isOpened():
            ret, frame = cap.read()
            if ret and frame is not None:
                print(f"[OK] DirectShow camera works! Frame shape: {frame.shape}")
                cap.release()
                return 0
            else:
                print(f"[FAIL] DirectShow camera opened but cannot read frame")
        else:
            print(f"[FAIL] Cannot open DirectShow camera")
        
        cap.release()
        
    except Exception as e:
        print(f"[ERROR] Error with DirectShow: {e}")
    
    print("\n[FAIL] No working camera found!")
    return None

if __name__ == "__main__":
    working_camera = test_camera()
    
    if working_camera is not None:
        print(f"\n[SUCCESS] Use camera index: {working_camera}")
        print("You can now run the thermal camera app!")
    else:
        print("\n[TIPS] Troubleshooting tips:")
        print("1. Make sure your camera is connected")
        print("2. Close other apps using the camera (Skype, Teams, etc.)")
        print("3. Try running as administrator")
        print("4. Check Windows Camera privacy settings")