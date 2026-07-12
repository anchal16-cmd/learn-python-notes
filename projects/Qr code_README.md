# QR Code Generator

A simple Python project that generates QR codes from text or URLs and saves them as PNG image files. This project uses the `qrcode` and `Pillow` libraries to create high-quality, scannable QR codes.

## Features

* Generate QR codes from any text or URL
* Automatically save the QR code as a PNG image
* Custom file name support
* Beginner-friendly and easy to use
* Simple command-line interface

## Technologies Used

* Python
* qrcode
* Pillow (PIL)

## Project Structure

```text
QR-Code-Generator/
│── qr_code.py
│── github.png
└── README.md
```

## Installation

Install the required libraries:

```bash
pip install qrcode[pil]
```

## How to Run

Run the program:

```bash
python qr_code.py
```

Enter the text or URL when prompted:

```text
Enter a URL or text: https://github.com/anchal16-cmd
Enter file name (without extension): github
```

The generated QR code will be saved as:

```text
github.png
```

## Example

### Input

```text
URL: https://github.com/anchal16-cmd
File Name: github
```

### Output

* A QR code image named **github.png** is created successfully.
* Scanning the QR code opens the specified GitHub profile.

## Future Improvements

* Add custom QR code colors
* Add logo in the center of the QR code
* Build a graphical user interface (GUI) using Tkinter
* Generate multiple QR codes from a CSV or Excel file
* Allow users to choose the save location

## Author

**Aanchal Pandey**

GitHub: https://github.com/anchal16-cmd
