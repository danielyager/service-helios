from flask import Flask
from config import Config
from helios_app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize flask extensions here
    db.init_app(app)

    # Register blueprints here
    from helios_app.routes import bp as testing_bp
    app.register_blueprint(testing_bp)
    
    return app