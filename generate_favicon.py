#!/usr/bin/env python3
"""
Generate favicon.ico and PNG icons for EKO
Requires: pip install Pillow
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size):
    """Create an icon with gradient background and EKO text"""
    # Create image with transparent background
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Draw circle background with gradient effect (simplified)
    # Using multiple circles with different colors for gradient effect
    colors = [
        (0, 245, 212, 255),      # cyan
        (123, 44, 191, 255),     # purple
        (247, 37, 133, 255),     # magenta
    ]

    for i, color in enumerate(colors):
        alpha = int(180 - i * 40)
        circle_color = color[:3] + (alpha,)
        offset = i * int(size * 0.05)
        if offset * 2 < size:  # Ensure valid coordinates
            draw.ellipse([offset, offset, size-offset, size-offset], fill=circle_color)

    # Draw person figure (simplified)
    center_x, center_y = size // 2, size // 2 - size // 8

    # Head
    head_size = size // 8
    draw.ellipse([center_x - head_size//2, center_y - head_size,
                  center_x + head_size//2, center_y], fill=(255, 159, 28, 255))

    # Body
    body_width = size // 6
    body_height = size // 4
    draw.rectangle([center_x - body_width//2, center_y,
                    center_x + body_width//2, center_y + body_height],
                   fill=(255, 159, 28, 255))

    # Sound waves (simplified as arcs)
    wave_color = (0, 245, 212, 200)
    for i in range(3):
        offset = 15 + i * 10
        thickness = 3 - i
        draw.arc([size//4 - offset, center_y - offset//2,
                  size//4, center_y + offset//2],
                 start=270, end=90, fill=wave_color, width=thickness)
        draw.arc([3*size//4, center_y - offset//2,
                  3*size//4 + offset, center_y + offset//2],
                 start=90, end=270, fill=wave_color, width=thickness)

    return img

# Create directory for icons if it doesn't exist
script_dir = os.path.dirname(os.path.abspath(__file__))

# Generate various sizes
sizes = [16, 32, 48, 64, 128, 256, 512]
images = []

for size in sizes:
    img = create_icon(size)
    images.append(img)

    # Save individual PNG files
    if size in [192, 512]:
        img.save(os.path.join(script_dir, f'icon-{size}.png'))

# Save favicon.ico with multiple sizes
favicon_path = os.path.join(script_dir, 'favicon.ico')
images[0].save(favicon_path, format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])

# Save apple-touch-icon
apple_icon = create_icon(180)
apple_icon.save(os.path.join(script_dir, 'apple-touch-icon.png'))

# Save main icon
main_icon = create_icon(512)
main_icon.save(os.path.join(script_dir, 'icon-512.png'))

print("favicon.ico created")
print("icon-192.png created")
print("icon-512.png created")
print("apple-touch-icon.png created")
