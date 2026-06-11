import qrcode as qr

# make QR Code
img=qr.make('https://www.youtube.com/@KiddoWonderland2023')

# save it as .png file
img.save('kiddo_wonderland_youtube.png')

