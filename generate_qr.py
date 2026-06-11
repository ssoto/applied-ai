#!/usr/bin/env python3
"""Generate QR code for assets/qr.png"""

import qrcode
from pathlib import Path

URL = "https://ssoto.github.io/applied-ai/"
OUTPUT = Path(__file__).parent / "assets" / "qr.png"

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=12,
    border=2,
)
qr.add_data(URL)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(OUTPUT)
print(f"QR generado: {OUTPUT}  →  {URL}")
