from flask import Blueprint, render_template, send_file
from make_qr import generate_code
from .forms.QRCodeForm import QRCodeForm

views = Blueprint("views", __name__, template_folder="../templates", static_url_path="../static")

@views.route('/', methods=['GET', 'POST'])
@views.route('/home', methods=['GET', 'POST'])
def home():
    form = QRCodeForm()
    
    if form.validate_on_submit():
        text = form.text.data
        
        code = generate_code(text)
        response = send_file(code, download_name="qr_code.png", mimetype="image/png")
        print(response.content_type)
        return response
    
    return render_template("home.html", title="QR maker", form=form)