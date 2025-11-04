
try:
	import pyqrcode
	from pyqrcode import QRCode
except ImportError as e:
	print("ERROR: Required module missing.")
	print("Details:", e)
	print("To fix, run:")
	print("    pip install pyqrcode pypng")
	exit(1)

# String which represent the QR code 
s = "https://www.youtube.com/channel/UCBz4yaxNxfiz1XYh-07UfWQ"

# Generate QR code 
url = pyqrcode.create(s)

# Create and save the SVG file naming "myyoutube.svg" 
url.svg("myyoutube.svg", scale=8)
print("QR code SVG generated: myyoutube.svg")