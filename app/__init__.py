from flask import Flask
from app.routes import bp as routes_bp
from app.error_handlers import register_error_handlers

def create_app():
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(routes_bp)

    # Register Error Handlers
    register_error_handlers(app)

    return app
