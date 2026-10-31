from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from app.extensions import db
from app.models import Usuario

bp_auth = Blueprint('auth', __name__, template_folder='templates')

@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = Usuario.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))
        flash('Credenciales incorrectas', 'danger')
    return render_template('login.html')

@bp_auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        password = request.form.get('password')
        nuevo_user = Usuario(nombre=nombre, email=email)
        nuevo_user.set_password(password)
        db.session.add(nuevo_user)
        db.session.commit()
        flash('Registro exitoso, por favor inicia sesión', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@bp_auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))