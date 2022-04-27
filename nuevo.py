from unittest import result
import qrcode
from pyzbar.pyzbar import decode
import cv2

qr = qrcode.QRCode(
    version= 1,
    box_size=10,
    border = 2
)
datos = ('dayitecnologia',12578245822,'cup',5633254)
qr.add_data(datos)
qr.make(fit=True)

img = qr.make_image(fill_color='black',back_color='pink')
img.save('qrcode.png')

img1 = cv2.imread('qrcode.png')
resultado = decode(img1)
print(resultado)
for i in resultado:
    print(i.data.decode('utf-8'))
