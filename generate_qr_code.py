#!/usr/bin/env python3
"""
Generate QR codes for EKO questionnaire with improved contrast and branding
Requires: pip install qrcode[pil]
"""

import qrcode
from PIL import Image, ImageDraw
import os

# URL to encode
url = "https://sean4e.github.io/eko"
script_dir = os.path.dirname(os.path.abspath(__file__))

# Version 1: High contrast cyan on dark background (best for visibility)
print("Generating Version 1: High Contrast (Cyan on Dark)...")
qr1 = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr1.add_data(url)
qr1.make(fit=True)
img1 = qr1.make_image(fill_color="#00f5d4", back_color="#0a0a0f")
img1.save(os.path.join(script_dir, 'eko-qr-code.png'))

# Version 2: High-res for printing (dark on light with border)
print("Generating Version 2: High-Res Print (Dark on Light with Border)...")
qr2 = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=4,
)
qr2.add_data(url)
qr2.make(fit=True)
img2_qr = qr2.make_image(fill_color="#0a0a0f", back_color="white")

# Add colored border to high-res version
width, height = img2_qr.size
bordered = Image.new('RGB', (width + 40, height + 40), '#00f5d4')
bordered.paste(img2_qr, (20, 20))
bordered.save(os.path.join(script_dir, 'eko-qr-code-hires.png'))

# Version 3: Magenta variant (alternative branding)
print("Generating Version 3: Magenta Variant...")
qr3 = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr3.add_data(url)
qr3.make(fit=True)
img3 = qr3.make_image(fill_color="#f72585", back_color="#0a0a0f")
img3.save(os.path.join(script_dir, 'eko-qr-code-magenta.png'))

# Version 4: Print-optimized with logo area
print("Generating Version 4: Print Version with Logo Space...")
qr4 = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=25,
    border=2,
)
qr4.add_data(url)
qr4.make(fit=True)
img4_qr = qr4.make_image(fill_color="#0a0a0f", back_color="white")

# Create large canvas with gradient border
canvas_size = img4_qr.size[0] + 120
canvas = Image.new('RGB', (canvas_size, canvas_size), 'white')
draw = ImageDraw.Draw(canvas)

# Draw gradient border (simulated with bands)
colors = [(0, 245, 212), (123, 44, 191), (247, 37, 133), (255, 159, 28)]
border_width = 15
for i, color in enumerate(colors):
    offset = i * 5
    draw.rectangle([offset, offset, canvas_size-offset, canvas_size-offset],
                   outline=color, width=4)

# Paste QR code in center
offset = 60
canvas.paste(img4_qr, (offset, offset))
canvas.save(os.path.join(script_dir, 'eko-qr-code-print.png'))

print("\nQR codes generated successfully!")
print("  - eko-qr-code.png (High contrast for web - Cyan on Dark)")
print("  - eko-qr-code-hires.png (High-res with cyan border)")
print("  - eko-qr-code-magenta.png (Magenta variant)")
print("  - eko-qr-code-print.png (Print-optimized with gradient border)")
print(f"\nAll scan to: {url}")
