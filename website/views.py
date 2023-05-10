from flask import Blueprint, render_template, send_file
from make_qr import generate_code
from .forms.QRCodeForm import QRCodeForm
from base64 import b64encode

views = Blueprint("views", __name__, template_folder="../templates", static_url_path="../static")


@views.route('/', methods=['GET', 'POST'])
@views.route('/home', methods=['GET', 'POST'])
def home():
    form = QRCodeForm()
    
    if form.validate_on_submit():
        text = form.text.data
        bg_color = form.background_color.data
        fg_color = form.foreground_color.data
        size = form.size.data
        
        
        code = generate_code(text, size=size, bg_color=bg_color, fg_color=fg_color)

        return render_template("home.html", title="QR maker", form=form, img_bytes=code)
    
    return render_template("home.html", title="QR maker", form=form)


@views.app_template_filter("b64encode")
def b64_encode_filter(img):
    return b64encode(img).decode('utf-8')


@views.route('/test', methods=['GET', 'POST'])
def test():
    return render_template("test3.html")