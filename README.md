# QR Code Application

This is a Python-based GUI application for generating and scanning QR codes. The application provides a user-friendly interface to either generate a QR code from a given link or scan a QR code using a camera or an uploaded image.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Code Explanation](#code-explanation)

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/qrcode-app.git
    cd qrcode-app
    ```

2. **Install dependencies**:
    ```sh
    pip install qrcode[pil] opencv-python-headless pyzbar numpy pillow
    ```

3. **Run the application**:
    ```sh
    python app.py
    ```

## Usage

1. **Generate QR Code**:
    - Click on the "Generate QR Code" button.
    - Enter the link in the provided text field.
    - Click "Generate" to create the QR code.
    - Save the generated QR code image.

2. **Scan QR Code**:
    - Click on the "Scan QR Code" button.
    - Choose either "Open Camera" to scan using a webcam or "Upload Image" to scan from an image file.
    - View the decoded QR code data.

## Features

- Generate QR codes from a given link.
- Scan QR codes using a webcam or from an uploaded image.
- User-friendly interface with clear prompts and error handling.

## Code Explanation

### Import Statements

- `tkinter` for creating the GUI.
- `filedialog` and `messagebox` for file selection and displaying messages.
- `qrcode` for generating QR codes.
- `cv2` for accessing the camera and reading images.
- `pyzbar` for decoding QR codes.
- `numpy` for handling arrays.
- `PIL` for image processing.

### QRApp Class

- `__init__(self, root)`: Initializes the main window and sets the title.
- `create_widgets(self)`: Creates the initial buttons for generating or scanning QR codes.
- `generate_qr_code(self)`: Prompts the user to enter a link and generates a QR code.
- `save_qr_code(self)`: Saves the generated QR code to a file.
- `scan_qr_code(self)`: Provides options to scan a QR code using a camera or an uploaded image.
- `scan_with_camera(self)`: Opens the camera and scans for QR codes in real-time.
- `upload_image(self)`: Allows the user to upload an image file to scan for QR codes.
- `clear_frame(self)`: Clears the current window contents.

### Main Block

- `if __name__ == "__main__":`: Initializes and runs the application.

This application is a practical tool for generating and scanning QR codes, making it suitable for various use cases such as sharing links, contact information, or any other data in QR code format.
