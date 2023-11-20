from helios_app.routes import bp

@bp.route('/')
def index():
    return '<h1>Testing the home page!</h1>'

@bp.route('/hello-test/')
def hello_world_test():
    return '<h1>Hello, World!</h1>'