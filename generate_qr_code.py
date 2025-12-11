#!/usr/bin/env python3
"""
Generate QR code for EKO questionnaire
Requires: pip install qrcode[pil]
"""

import qrcode
from PIL import Image
import os

# URL to encode
url = "https://sean4e.github.io/eko"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,  # Size of each box in pixels
    border=4,  # Border size in boxes
)

# Add data
qr.add_data(url)
qr.make(fit=True)

# Create QR code image with custom colors
img = qr.make_image(fill_color="#00f5d4", back_color="white")

# Save the QR code
script_dir = os.path.dirname(os.path.abspath(__file__))
qr_path = os.path.join(script_dir, 'eko-qr-code.png')
img.save(qr_path)

print(f"QR code generated: {qr_path}")
print(f"Scan to visit: {url}")

# Also create a high-res version
qr_hires = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,  # Larger boxes for printing
    border=4,
)
qr_hires.add_data(url)
qr_hires.make(fit=True)
img_hires = qr_hires.make_image(fill_color="#00f5d4", back_color="white")

qr_hires_path = os.path.join(script_dir, 'eko-qr-code-hires.png')
img_hires.save(qr_hires_path)

print(f"High-res QR code generated: {qr_hires_path}")
print("\nUse eko-qr-code.png for web")
print("Use eko-qr-code-hires.png for printing")
