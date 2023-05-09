from flask import Blueprint


views = Blueprint("views", __name__, template_folder="../templates", static_url_path="../static")

@views.route('/')
@views.route('/home')
def home():
    return "Home"