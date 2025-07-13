# Contributing to TempCam-Python

Cảm ơn bạn đã quan tâm đến việc đóng góp cho TempCam-Python! 🎉

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Submitting Changes](#submitting-changes)
- [Coding Standards](#coding-standards)
- [Testing](#testing)

## 📜 Code of Conduct

Dự án này tuân thủ các nguyên tắc:
- Tôn trọng lẫn nhau
- Xây dựng môi trường thân thiện
- Chấp nhận phản hồi xây dựng
- Tập trung vào điều tốt nhất cho cộng đồng

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Git
- Webcam hoặc camera USB
- Kiến thức cơ bản về Python và OpenCV

### Development Setup

1. **Fork repository**
   ```bash
   # Trên GitHub, click "Fork" button
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/your-username/TempCam-Python.git
   cd TempCam-Python
   ```

3. **Set up upstream remote**
   ```bash
   git remote add upstream https://github.com/tranhao-wq/TempCam-Python.git
   ```

4. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

5. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

6. **Test installation**
   ```bash
   python test_camera.py
   python run_thermal_camera.py
   ```

## 🔧 Making Changes

### Branch Strategy

- `main` - Production-ready code
- `develop` - Development branch
- `feature/feature-name` - New features
- `bugfix/bug-description` - Bug fixes
- `hotfix/critical-fix` - Critical fixes

### Creating a Feature Branch

```bash
# Update your main branch
git checkout main
git pull upstream main

# Create feature branch
git checkout -b feature/your-feature-name
```

### Types of Contributions

#### 🐛 Bug Fixes
- Fix existing functionality
- Add tests for the fix
- Update documentation if needed

#### ✨ New Features
- Add new thermal effects
- Improve UI/UX
- Add new camera modes
- Performance improvements

#### 📚 Documentation
- Improve README
- Add code comments
- Create tutorials
- Update API documentation

#### 🧪 Testing
- Add unit tests
- Improve test coverage
- Add integration tests

## 📤 Submitting Changes

### Before Submitting

1. **Test your changes**
   ```bash
   python test_camera.py
   python -m pytest tests/  # if tests exist
   ```

2. **Check code style**
   ```bash
   # Format code (optional but recommended)
   black thermal_scanner/
   ```

3. **Update documentation**
   - Update README if needed
   - Add docstrings to new functions
   - Update CHANGELOG.md

### Pull Request Process

1. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add new thermal effect for night mode"
   ```

2. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create Pull Request**
   - Go to GitHub and create PR
   - Use descriptive title and description
   - Link related issues
   - Add screenshots if UI changes

### Commit Message Format

Sử dụng conventional commits:

```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(camera): add DirectShow backend support for Windows
fix(ui): resolve camera frame sizing issue
docs(readme): add troubleshooting section
```

## 🎨 Coding Standards

### Python Style Guide

- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions small and focused
- Use type hints where appropriate

### Code Structure

```python
def function_name(param1: type, param2: type) -> return_type:
    """
    Brief description of function.
    
    Args:
        param1 (type): Description of param1
        param2 (type): Description of param2
        
    Returns:
        return_type: Description of return value
        
    Raises:
        ExceptionType: Description of when this exception is raised
    """
    # Implementation
    pass
```

### File Organization

```
thermal_scanner/
├── __init__.py
├── main.py              # Entry point
├── ui_main.py           # UI components
├── camera_handler.py    # Camera operations
├── night_mode.py        # Night mode processing
└── utils/
    ├── __init__.py
    └── logger.py        # Logging utilities
```

## 🧪 Testing

### Running Tests

```bash
# Test camera functionality
python test_camera.py

# Run unit tests (if available)
python -m pytest tests/

# Test specific module
python -c "from thermal_scanner import camera_handler; print('Import successful')"
```

### Adding Tests

Khi thêm feature mới, hãy thêm tests:

```python
# tests/test_camera_handler.py
import unittest
from thermal_scanner.camera_handler import ThermalCameraHandler

class TestThermalCameraHandler(unittest.TestCase):
    def test_initialization(self):
        handler = ThermalCameraHandler()
        self.assertIsNotNone(handler)
        
    def test_camera_detection(self):
        # Test camera detection logic
        pass
```

## 📝 Documentation

### Code Documentation

- Add docstrings to all public functions
- Use clear variable names
- Comment complex algorithms
- Update README for new features

### README Updates

Khi thêm feature mới:
- Cập nhật feature list
- Thêm usage examples
- Cập nhật screenshots nếu cần
- Thêm troubleshooting tips

## 🎯 Priority Areas

Chúng tôi đặc biệt hoan nghênh contributions trong các lĩnh vực:

1. **Performance Optimization**
   - Cải thiện FPS
   - Giảm CPU usage
   - Tối ưu memory usage

2. **Cross-platform Support**
   - Test trên macOS/Linux
   - Fix platform-specific issues

3. **New Thermal Effects**
   - Advanced thermal algorithms
   - Real-time heat detection
   - Motion-based thermal mapping

4. **UI/UX Improvements**
   - Better responsive design
   - More intuitive controls
   - Accessibility features

5. **Testing & Quality**
   - Unit tests
   - Integration tests
   - Error handling improvements

## ❓ Questions?

- 💬 **Discussions**: [GitHub Discussions](https://github.com/tranhao-wq/TempCam-Python/discussions)
- 🐛 **Issues**: [GitHub Issues](https://github.com/tranhao-wq/TempCam-Python/issues)
- 📧 **Contact**: Create an issue for questions

## 🙏 Recognition

Contributors sẽ được ghi nhận trong:
- README.md
- CONTRIBUTORS.md
- Release notes
- GitHub contributors page

---

**Cảm ơn bạn đã đóng góp cho TempCam-Python! 🚀**