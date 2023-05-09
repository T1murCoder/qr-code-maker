import qrcode
from io import BytesIO


def generate_code(text) -> BytesIO:
    qr = qrcode.QRCode(
        version=5,
        border=4
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image()
    img_bytes = BytesIO()
    img.seek(0)
    img.save(img_bytes, format='png')
    img_bytes.seek(0)
    return img_bytes


if __name__ == '__main__':
    text = input()
    img_bytes = generate_code(text)
    
    print(img_bytes)
    with open('test.png', 'wb') as f:
        f.write(img_bytes.read())