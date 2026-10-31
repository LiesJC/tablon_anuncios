from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required
from app.extensions import db
from app.models import Usuario

bp_usuarios = Blueprint('usuarios', __name__, template_folder='templates')

@bp_usuarios.route('/')
@login_required
def listar():
    usuarios = Usuario.query.all()
    return render_template('listar.html', usuarios=usuarios)

@bp_usuarios.route('/crear', methods=['GET', 'POST'])
@login_required
def crear():
    if request.method == 'POST':
        user = Usuario(nombre=request.form.get('nombre'), email=request.form.get('email'))
        user.set_password(request.form.get('password'))
        db.session.add(user)
        db.session.commit()
        flash('Usuario creado', 'success')
        return redirect(url_for('usuarios.listar'))
    return render_template('crear.html')

@bp_usuarios.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar(id):
    user = Usuario.query.get_or_404(id)
    if request.method == 'POST':
        user.nombre = request.form.get('nombre')
        user.email = request.form.get('email')
        if request.form.get('password'):
            user.set_password(request.form.get('password'))
        db.session.commit()
        flash('Usuario actualizado', 'info')
        return redirect(url_for('usuarios.listar'))
    return render_template('editar.html', usuario=user)

@bp_usuarios.route('/eliminar/<int:id>')
@login_required
def eliminar(id):
    user = Usuario.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('Usuario eliminado', 'danger')
    return redirect(url_for('usuarios.listar'))