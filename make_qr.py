import qrcode
from qrcode.image.styles.moduledrawers.pil import SquareModuleDrawer, GappedSquareModuleDrawer, CircleModuleDrawer, RoundedModuleDrawer, VerticalBarsDrawer, HorizontalBarsDrawer
from qrcode.image.styledpil import StyledPilImage
from io import BytesIO


def generate_code(text, size=450, bg_color="#FFFFFF", fg_color="#000000", style="Default") -> BytesIO:
    qr = qrcode.QRCode(
        version=5,
        border=4,
        box_size=size // 45
    )
    
    qr.add_data(text)
    qr.make(fit=True)
    
    module_drawer = get_module_drawer(style)
    
    img = qr.make_image(back_color=bg_color, fill_color=fg_color, image_factory=StyledPilImage, module_drawer=module_drawer())
    
    img_bytes = BytesIO()
    img.seek(0)
    img.save(img_bytes, format='png')
    img_bytes.seek(0)
    
    return img_bytes


def get_module_drawer(style: str):
    if style == "Gapped":
        return GappedSquareModuleDrawer
    elif style == "Circle":
        return CircleModuleDrawer
    elif style == "Rounded":
        return RoundedModuleDrawer
    elif style == "Verticlal bars":
        return VerticalBarsDrawer
    elif style == "Horizontal bars":
        return HorizontalBarsDrawer
    return SquareModuleDrawer
    

if __name__ == '__main__':
    text = input()
    img_bytes = generate_code(text)
    
    with open('test.png', 'wb') as f:
        f.write(img_bytes.read())