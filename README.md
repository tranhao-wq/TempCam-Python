<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/2dbaeaf1-186d-4efd-8c70-b10b3d601bf6" /><img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/bd511b35-7f58-4a38-8a78-5eb371eb3ce0" /># 🔥 TempCam-Python - Thermal Camera Simulator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-green.svg)](https://opencv.org/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/tranhao-wq/TempCam-Python)

Ứng dụng Python mô phỏng thermal camera sử dụng webcam laptop với giao diện Tkinter dark mode. Tạo hiệu ứng thermal thực tế dựa trên độ sáng và chuyển động, tự động chuyển đổi giữa chế độ ngày và đêm.

## 📸 Screenshots

### Day Mode (Chế độ ban ngày)
![Day Mode]<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/98b12359-bc8f-4b0a-9075-1b33e53719be" />

*Thermal effect với màu nóng (đỏ/vàng) cho điều kiện ánh sáng bình thường*

### Night Mode (Chế độ ban đêm)
![Night Mode]<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/07df6b8c-f109-4e89-94c4-06d2dd84583f" />

*Thermal effect với màu lạnh (xanh/tím) cho điều kiện ánh sáng thấp*

### Main Interface
```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        🔥 Thermal Camera Simulator                             │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │                                                                           │  │
│  │                        📷 Camera Preview                                  │  │
│  │                                                                           │  │
│  │    ████████████████████████████████████████████████████████████████████   │  │
│  │    ██████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██   │  │
│  │    ████████████████████▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██   │  │
│  │    ██████████████████▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██   │  │
│  │    ████████████████▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██   │  │
│  │    ██████████████▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██   │  │
│  │    ████████████▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██   │  │
│  │    ██████████▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██   │  │
│  │    ████████▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██   │  │
│  │    ██████▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██   │  │
│  │    ████▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██   │  │
│  │    ██▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██   │  │
│  │    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██   │  │
│  │    ████████████████████████████████████████████████████████████████████   │  │
│  │                                                                           │  │
│  └───────────────────────────────────────────────────────────────────────────┘  │
│                                                                                 │
│    ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐                         │
│    │ ▶ Start │  │ ⏸ Stop  │  │📸Capture│  │ ❌ Exit │                         │
│    └─────────┘  └─────────┘  └─────────┘  └─────────┘                         │
│                                                                                 │
│ Status: Camera running - Thermal mode active                                   │
│                          Night mode: Auto-detect | Thermal effect: Active     │
└─────────────────────────────────────────────────────────────────────────────────┘
```
*Giao diện chính với dark mode theme và thermal effect display*

## ✨ Tính năng

- **Giao diện Dark Mode**: UI tối màu, dễ nhìn
- **Thermal Effect**: Mô phỏng ảnh nhiệt bằng OpenCV colormap
- **Auto Night Mode**: Tự động phát hiện và xử lý điều kiện ánh sáng thấp
- **Image Enhancement**: Tăng sáng, tương phản và khử nhiễu cho ảnh ban đêm
- **Capture Function**: Chụp và lưu ảnh với timestamp
- **Real-time Processing**: Xử lý video real-time với threading

## 🎮 Điều khiển

- **Start**: Bắt đầu camera và hiển thị thermal effect
- **Stop**: Tạm dừng camera, giữ frame cuối cùng
- **Capture**: Chụp ảnh hiện tại và lưu file
- **Exit**: Đóng ứng dụng và giải phóng camera

## 🌙 Thermal Detection Modes

### Day Mode (Ban ngày)
- **Thermal Colors**: Đỏ/cam/vàng cho vùng nóng, xanh đen cho vùng lạnh
- **Detection**: Dựa trên độ sáng và chuyển động
- **Suitable**: Điều kiện ánh sáng bình thường

### Night Mode (Ban đêm)
- **Thermal Colors**: Xanh/tím cho vùng lạnh, trắng/vàng cho vùng nóng
- **Enhancement**: Tự động tăng sáng, tương phản và khử nhiễu
- **Detection**: Tự động kích hoạt khi độ sáng < 60/255
- **Processing**: fastNlMeansDenoising cho chất lượng tốt hơn

## 📁 Cấu trúc Project

```
thermal_scanner/
├── main.py                 # Entry point chính
├── ui_main.py              # Giao diện Tkinter
├── camera_handler.py       # Xử lý camera và thermal effects
├── night_mode.py           # Phát hiện và xử lý night mode
└── utils/
    └── logger.py           # Logging system

run_thermal_camera.py       # Launcher script
requirements.txt            # Dependencies
README.md                   # Documentation
```

## 🚀 Cài đặt và Chạy

### 1. Cài đặt Dependencies

```bash
pip install -r requirements.txt
```

### 2. Chạy ứng dụng

```bash
python run_thermal_camera.py
```

Hoặc:

```bash
cd thermal_scanner
python main.py
```

## 📋 System Requirements

### Software Requirements
- **Python**: 3.7 or higher
- **Operating System**: Windows 10/11, macOS 10.14+, Ubuntu 18.04+
- **Memory**: Minimum 4GB RAM (8GB recommended)
- **Storage**: 100MB free space

### Hardware Requirements
- **Camera**: Built-in webcam or USB camera
- **CPU**: Multi-core processor recommended for real-time processing
- **Display**: Minimum 1024x768 resolution

### Python Dependencies
```
opencv-python>=4.5.0
Pillow>=8.0.0
numpy>=1.19.0
```

## 🎯 Sử dụng

1. **Khởi động**: Chạy `python run_thermal_camera.py`
2. **Start Camera**: Click nút "Start" để bắt đầu
3. **Xem Thermal Effect**: Camera sẽ hiển thị với hiệu ứng thermal
4. **Chụp ảnh**: Click "Capture" để lưu ảnh hiện tại
5. **Dừng**: Click "Stop" để tạm dừng hoặc "Exit" để thoát

## 📸 Capture Images

Ảnh được lưu trong thư mục `captures/` với format:
```
thermal_capture_YYYYMMDD_HHMMSS.jpg
```

## 🔧 Tùy chỉnh

### Điều chỉnh Night Mode Threshold

Trong `night_mode.py`, thay đổi `brightness_threshold`:

```python
# Ngưỡng độ sáng (0-255), thấp hơn = nhạy hơn với ánh sáng thấp
brightness_threshold = 60
```

### Thay đổi Colormap

Trong `night_mode.py`:

```python
def get_day_colormap(self):
    return cv2.COLORMAP_JET  # Hoặc COLORMAP_HOT, COLORMAP_COOL, etc.

def get_night_colormap(self):
    return cv2.COLORMAP_INFERNO  # Hoặc COLORMAP_MAGMA, COLORMAP_PLASMA, etc.
```

## 🐛 Troubleshooting

### Camera Issues

**Camera không hoạt động:**
```bash
# Test camera trước khi chạy app
python test_camera.py
```
- ✅ Kiểm tra camera có được kết nối không
- ✅ Đảm bảo không có ứng dụng khác đang sử dụng camera (Skype, Teams, etc.)
- ✅ Thử chạy với quyền Administrator
- ✅ Kiểm tra Windows Camera privacy settings

**Camera lag hoặc chậm:**
- Đóng các ứng dụng khác đang chạy
- Giảm FPS trong `camera_handler.py` (line 35: `self.fps = 10`)
- Giảm resolution camera

### Installation Issues

**Import Errors:**
```bash
# Cài đặt lại dependencies
pip install --upgrade -r requirements.txt

# Hoặc cài đặt từng package
pip install opencv-python pillow numpy
```

**Python Version:**
```bash
# Kiểm tra Python version
python --version
# Cần Python 3.7+
```

### Performance Optimization

**Cải thiện hiệu suất:**
1. Giảm FPS: `self.fps = 10` trong `camera_handler.py`
2. Giảm resolution: Sửa `CAP_PROP_FRAME_WIDTH/HEIGHT`
3. Tắt night mode enhancement nếu không cần thiết
4. Sử dụng SSD thay vì HDD cho lưu trữ

### Common Error Messages

| Error | Solution |
|-------|----------|
| `Cannot open camera 0` | Thử `python test_camera.py` để tìm camera index đúng |
| `Import error: No module named 'cv2'` | `pip install opencv-python` |
| `Failed to read frame` | Restart camera hoặc thử camera index khác |
| `Permission denied` | Chạy với quyền Administrator |

## 📝 Logs

Logs được lưu trong thư mục `logs/` với format:
```
thermal_camera_YYYYMMDD.log
```

## 🤝 Contributing

Chúng tôi hoan nghênh mọi đóng góp! Hãy xem [CONTRIBUTING.md](CONTRIBUTING.md) để biết thêm chi tiết.

### Quick Start for Contributors

1. **Fork** repository này
2. **Clone** fork của bạn:
   ```bash
   git clone https://github.com/your-username/TempCam-Python.git
   ```
3. **Create branch** cho feature mới:
   ```bash
   git checkout -b feature/amazing-feature
   ```
4. **Commit** changes:
   ```bash
   git commit -m 'Add amazing feature'
   ```
5. **Push** to branch:
   ```bash
   git push origin feature/amazing-feature
   ```
6. **Open Pull Request**

### Development Setup

```bash
# Clone repository
git clone https://github.com/tranhao-wq/TempCam-Python.git
cd TempCam-Python

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
python test_camera.py

# Run application
python run_thermal_camera.py
```

## 🔒 Security

Bảo mật là ưu tiên hàng đầu. Vui lòng xem [SECURITY.md](SECURITY.md) để:
- Báo cáo lỗ hổng bảo mật
- Hiểu các best practices
- Xem các phiên bản được hỗ trợ

## 📊 Project Stats

- **Language**: Python 🐍
- **Framework**: Tkinter (GUI), OpenCV (Computer Vision)
- **License**: MIT 📄
- **Platform**: Cross-platform 🌐
- **Status**: Active Development 🚀

## 🙏 Acknowledgments

- **OpenCV** - Computer vision library
- **Pillow** - Python Imaging Library
- **NumPy** - Numerical computing
- **Tkinter** - GUI framework

## 📞 Support

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/tranhao-wq/TempCam-Python/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/tranhao-wq/TempCam-Python/discussions)
- 📧 **Contact**: Create an issue for support

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <strong>⭐ Star this repository if you find it helpful! ⭐</strong>
  <br><br>
  Made with ❤️ by <a href="https://github.com/tranhao-wq">tranhao-wq</a>
</div>
