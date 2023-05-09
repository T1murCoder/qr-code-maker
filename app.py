from flask import Flask
from website.views import views


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "my_super_secret_key"
    
    app.register_blueprint(views, url_prefix="")
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=8080, host='127.0.0.1')