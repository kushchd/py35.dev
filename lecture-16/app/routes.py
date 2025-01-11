#
from flask import render_template, url_for, flash, redirect
from app import app, db, bcrypt
from app.models import User
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/register", methods=['GET', 'POST'])
def register():
    # Here will be logic for registering a user
    return render_template('register.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    # Here will be logic for logging in a user
    return render_template('login.html')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/home")
@login_required
def home():
    return "Home Page - Protected Route"
