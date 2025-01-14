from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('departments', __name__)

departments = []

@bp.route("/departments/index")
def index():
    return render_template("departments_index.html", departments=departments)

@bp.route("/departments/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            departments.append(name)
        return redirect(url_for('departments.index'))
    return render_template("departments_create.html")
