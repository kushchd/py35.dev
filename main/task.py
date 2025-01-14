from flask import Blueprint

bp = Blueprint('task', __name__)

@bp.route("/hello")
def hello():
    return "Hello from Task Blueprint!"
