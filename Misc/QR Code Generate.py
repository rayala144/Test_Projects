import qrcode

data = 'Don\'t forget to follow me on Instagram and Twitter'

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color = 'red', background_color = 'white')
# img = qrcode.make(data)

img.save('C:/Users/rayal/Desktop/Python Projects/qrcode1.png')