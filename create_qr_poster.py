#!/usr/bin/env python3
"""
Create a printable poster with QR code for EKO
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Dimensions for a poster (A4 size at 300 DPI)
width = 2480  # 8.27 inches * 300 DPI
height = 3508  # 11.69 inches * 300 DPI

# Create image with gradient background
img = Image.new('RGB', (width, height), '#0a0a0f')
draw = ImageDraw.Draw(img)

# Draw gradient background (simplified with horizontal bands)
colors = [
    (10, 10, 15),      # Dark top
    (123, 44, 191),    # Purple
    (0, 245, 212),     # Cyan
    (247, 37, 133),    # Magenta
    (10, 10, 15),      # Dark bottom
]

band_height = height // (len(colors) - 1)
for i in range(len(colors) - 1):
    for y in range(band_height):
        # Interpolate between colors
        ratio = y / band_height
        r = int(colors[i][0] + (colors[i+1][0] - colors[i][0]) * ratio)
        g = int(colors[i][1] + (colors[i+1][1] - colors[i][1]) * ratio)
        b = int(colors[i][2] + (colors[i+1][2] - colors[i][2]) * ratio)

        y_pos = i * band_height + y
        draw.rectangle([0, y_pos, width, y_pos + 1], fill=(r, g, b))

# Add semi-transparent overlay for better text readability
overlay = Image.new('RGBA', (width, height), (10, 10, 15, 200))
img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
draw = ImageDraw.Draw(img)

# Try to use a nice font, fall back to default if not available
try:
    title_font = ImageFont.truetype("arial.ttf", 180)
    subtitle_font = ImageFont.truetype("arial.ttf", 80)
    body_font = ImageFont.truetype("arial.ttf", 60)
    url_font = ImageFont.truetype("arialbd.ttf", 70)
except:
    # Fallback to default
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    body_font = ImageFont.load_default()
    url_font = ImageFont.load_default()

# Title
title_text = "EKO"
title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
title_width = title_bbox[2] - title_bbox[0]
title_x = (width - title_width) // 2
draw.text((title_x, 200), title_text, fill='#00f5d4', font=title_font)

# Subtitle
subtitle_text = "Embodied Kinetic Orchestra"
subtitle_bbox = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
subtitle_x = (width - subtitle_width) // 2
draw.text((subtitle_x, 420), subtitle_text, fill='#f72585', font=subtitle_font)

# Description
desc_lines = [
    "Help shape an immersive art experience",
    "Share your thoughts on:",
    "",
    "• Myths & Cultural Stories",
    "• Movement & Interaction",
    "• Sound & Music Preferences",
    "• Visual Aesthetics",
    "• Personal Rituals"
]

y_pos = 650
for line in desc_lines:
    if line:
        line_bbox = draw.textbbox((0, 0), line, font=body_font)
        line_width = line_bbox[2] - line_bbox[0]
        line_x = (width - line_width) // 2
        draw.text((line_x, y_pos), line, fill='#ffffff', font=body_font)
    y_pos += 80

# Load and add QR code
script_dir = os.path.dirname(os.path.abspath(__file__))
qr_path = os.path.join(script_dir, 'eko-qr-code-hires.png')

try:
    qr_img = Image.open(qr_path)
    # Resize QR code to a good size
    qr_size = 800
    qr_img = qr_img.resize((qr_size, qr_size), Image.Resampling.LANCZOS)

    # Add white background behind QR code
    qr_bg_size = qr_size + 100
    qr_bg_x = (width - qr_bg_size) // 2
    qr_bg_y = 1800
    draw.rectangle([qr_bg_x, qr_bg_y, qr_bg_x + qr_bg_size, qr_bg_y + qr_bg_size],
                   fill='white')

    # Paste QR code
    qr_x = (width - qr_size) // 2
    qr_y = qr_bg_y + 50
    img.paste(qr_img, (qr_x, qr_y))

except Exception as e:
    print(f"Warning: Could not load QR code: {e}")

# URL text below QR code
url_text = "sean4e.github.io/eko"
url_bbox = draw.textbbox((0, 0), url_text, font=url_font)
url_width = url_bbox[2] - url_bbox[0]
url_x = (width - url_width) // 2
draw.text((url_x, 2750), url_text, fill='#00f5d4', font=url_font)

# Call to action
cta_text = "Scan to participate • Takes 5-10 minutes • Completely anonymous"
cta_bbox = draw.textbbox((0, 0), cta_text, font=body_font)
cta_width = cta_bbox[2] - cta_bbox[0]
cta_x = (width - cta_width) // 2
draw.text((cta_x, 2900), cta_text, fill='#ffffff', font=body_font)

# Save the poster
poster_path = os.path.join(script_dir, 'eko-poster.png')
img.save(poster_path, quality=95, dpi=(300, 300))

print(f"Poster created: {poster_path}")
print("Ready to print at A4 size (8.27 x 11.69 inches)")
print("Resolution: 300 DPI")
