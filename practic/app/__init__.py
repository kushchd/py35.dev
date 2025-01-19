from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    from . import views
    app.register_blueprint(views.bp)

    return app
