from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_required

bp = Blueprint('departments', __name__)

@bp.route('/departments/list', methods=['GET'])
@login_required
def list():
    departments = [{"id": 1, "name": "HR"}, {"id": 2, "name": "Finance"}]
    return render_template('departments_list.html', departments=departments)

@bp.route('/departments/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        pass
    return render_template('create_department.html')

@bp.route('/departments/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    if request.method == 'POST':
        pass
    return render_template('update_department.html', id=id)

@bp.route('/departments/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    pass
    return redirect(url_for('departments.list'))
