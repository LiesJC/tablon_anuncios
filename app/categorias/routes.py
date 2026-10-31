from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required
from app.extensions import db
from app.models import Categoria

bp_categorias = Blueprint('categorias', __name__, template_folder='templates')

@bp_categorias.route('/')
@login_required
def listar():
    categorias = Categoria.query.all()
    return render_template('categorias_listar.html', categorias=categorias)

@bp_categorias.route('/form', methods=['GET', 'POST'])
@bp_categorias.route('/form/<int:id>', methods=['GET', 'POST'])
@login_required
def form(id=None):
    categoria = Categoria.query.get_or_404(id) if id else None
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        if categoria:
            categoria.nombre = nombre
        else:
            db.session.add(Categoria(nombre=nombre))
        db.session.commit()
        flash('Categoría guardada', 'success')
        return redirect(url_for('categorias.listar'))
    return render_template('categorias_form.html', categoria=categoria)

@bp_categorias.route('/eliminar/<int:id>')
@login_required
def eliminar(id):
    cat = Categoria.query.get_or_404(id)
    db.session.delete(cat)
    db.session.commit()
    return redirect(url_for('categorias.listar'))