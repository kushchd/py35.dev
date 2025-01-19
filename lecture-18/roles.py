from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_required

bp = Blueprint('roles', __name__)

@bp.route('/roles/list', methods=['GET'])
@login_required
def list():
    roles = [{"id": 1, "name": "Admin"}, {"id": 2, "name": "User"}]
    return render_template('roles_list.html', roles=roles)

@bp.route("/roles/create", methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        pass
    return render_template('create_role.html')

@bp.route('/roles/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    if request.method == 'POST':
        pass
    return render_template('update_role.html', id=id)

@bp.route('/roles/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    pass
    return redirect(url_for('roles.list'))
