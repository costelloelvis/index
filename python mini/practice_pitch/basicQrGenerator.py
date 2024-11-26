import qrcode as qr

qrImg = qr.make("www.google.com")
qrImg.save('demo.png')