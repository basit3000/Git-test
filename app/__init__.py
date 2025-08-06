from flask import Flask, jsonify
from .routes.routes import home
from .utils.exceptions import ValidationError

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.register_blueprint(home)
    register_error_handlers(app)
    
    return app


def register_error_handlers(app):
    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        response = jsonify({
            'error': 'validation_error',
            'message': error.message,
            **error.payload
        })
        response.status_code = error.status_code
        return response

    @app.errorhandler(404)
    def not_found(e):
        return jsonify(error="not_found", message="Resource not found"), 404

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify(error="server_error", message="Something went wrong"), 500