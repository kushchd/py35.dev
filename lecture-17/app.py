from flask import Flask
from departments import bp as departments_bp
from roles import bp as roles_bp

app = Flask(__name__)
app.register_blueprint(departments_bp, url_prefix='/departments')
app.register_blueprint(roles_bp, url_prefix='/roles')

if __name__ == "__main__":
    app.run(debug=True)
