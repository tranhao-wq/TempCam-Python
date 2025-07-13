# Security Policy

## Supported Versions

We actively support the following versions of TempCam-Python:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take security vulnerabilities seriously. If you discover a security vulnerability in TempCam-Python, please report it responsibly.

### How to Report

1. **DO NOT** create a public GitHub issue for security vulnerabilities
2. Send an email to the project maintainer with details about the vulnerability
3. Include the following information:
   - Description of the vulnerability
   - Steps to reproduce the issue
   - Potential impact
   - Suggested fix (if available)

### What to Expect

- **Acknowledgment**: We will acknowledge receipt of your vulnerability report within 48 hours
- **Investigation**: We will investigate and validate the reported vulnerability
- **Timeline**: We aim to provide an initial response within 5 business days
- **Resolution**: Critical vulnerabilities will be addressed with high priority

### Security Best Practices

When using TempCam-Python:

1. **Camera Permissions**: Only grant camera access when necessary
2. **File Permissions**: Ensure captured images are stored securely
3. **Network Security**: Be cautious when transmitting thermal images over networks
4. **Updates**: Keep the application and its dependencies up to date
5. **Environment**: Run the application in a secure environment

### Known Security Considerations

- **Camera Access**: The application requires camera access to function
- **File Storage**: Captured images are stored locally in the `captures/` directory
- **Logging**: Application logs may contain system information
- **Dependencies**: Security depends on third-party libraries (OpenCV, PIL, etc.)

### Responsible Disclosure

We follow responsible disclosure practices:

- Security fixes will be released as soon as possible
- Credit will be given to researchers who report vulnerabilities responsibly
- We will coordinate with security researchers on disclosure timing

## Contact

For security-related inquiries, please contact the project maintainers through GitHub.

---

Thank you for helping keep TempCam-Python secure!