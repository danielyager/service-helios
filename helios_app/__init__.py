from flask import Flask
from config import Config
from helios_app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize flask extensions here
    db.init_app(app)

    # Register blueprints here
    from helios_app.routes import bpTest as testing_bp
    app.register_blueprint(testing_bp)

    from helios_app.routes import bpAccount as account_bp
    app.register_blueprint(account_bp, url_prefix='/account')
    
    return app