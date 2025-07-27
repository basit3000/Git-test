from flask import Flask
from .routes import home

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.register_blueprint(home)

    return app