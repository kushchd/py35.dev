from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

departments = []
roles = []

@app.route("/")
def home():
    return redirect(url_for('departments_index'))

@app.route("/departments/index")
def departments_index():
    return render_template('departments_index.html', departments=departments)

@app.route("/departments/create", methods=['GET', 'POST'])
def departments_create():
    if request.method == 'POST':
        new_department = request.form['name']
        departments.append(new_department)
        return redirect(url_for('departments_index'))
    return render_template('departments_create.html')

@app.route("/roles/index")
def roles_index():
    return render_template('roles_index.html', roles=roles)

@app.route("/roles/create", methods=['GET', 'POST'])
def roles_create():
    if request.method == 'POST':
        new_role = request.form['name']
        roles.append(new_role)
        return redirect(url_for('roles_index'))
    return render_template('roles_create.html')

if __name__ == "__main__":
    app.run(debug=True)
