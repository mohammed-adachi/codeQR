import qrcode
img = qrcode.make('Some data here')
print(img)
img.save('qrcode.jpg', 'JPEG')