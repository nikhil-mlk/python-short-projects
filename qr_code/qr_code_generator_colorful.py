# PIL (Pillow) --> This is used to create/EDIT/save images

import qrcode
from PIL import Image

# Define QR Code settings
'''
# version=1 --> smallest QR Code 
# If increase the version, the QR Code will become big.
# 
# error_correction --> Even if part of QR Code damage, still QR Code could be scanned. There are 4 levels of error correction:
# L = 7% recovery
# M = 15% recovery
# Q = 25% recovery
# H = 30% recovery
# 
# box_size --> QR Code each square pixel size
# 
# border --> White space around QR Code
'''
qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=7, border=4)

# Store data in QR Code
qr.add_data('https://www.youtube.com/@KiddoWonderland2023')

# This generates actual QR Structure
# fit=True --> Adjust the size of QR Code according to the data given in previous steps
qr.make(fit=True)

# convert qr code to image with qa code color = white and back color = black
img=qr.make_image(fill_color='white', back_color='black')

# Saving the image with name
img.save('youtube_channel_colorful_qr_code.png')




