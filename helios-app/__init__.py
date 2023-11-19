from flask import Flask

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize flask extensions here

    # Register blueprints here

    @app.route('/')
    def index_test():
        return '<h1>Testing the home page!</h1>'

    @app.route('/hello-test/')
    def hello_world_test():
        return '<h1>Hello, World!</h1>'
    
    return app