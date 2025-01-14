from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('roles', __name__)

roles = []

@bp.route("/roles/index")
def index():
    return render_template("roles_index.html", roles=roles)

@bp.route("/roles/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            roles.append(name)
        return redirect(url_for('roles.index'))
    return render_template("roles_create.html")

