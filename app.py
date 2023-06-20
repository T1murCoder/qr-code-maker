from flask import Flask
import logging
import logging.config
from utils.log_config import get_logging_dict_config, get_file_handler
from website.views import views


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "my_super_secret_key"
    #logging.config.dictConfig(get_logging_dict_config())
    #logger = logging.getLogger("app")
    #app.logger = logger
    
    logging.basicConfig(filename="logs/logs.log")
    
    app.register_blueprint(views, url_prefix="")
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=8080, host='127.0.0.1')