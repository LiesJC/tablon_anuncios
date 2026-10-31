from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app.extensions import db
from app.models import Anuncio, Categoria

bp_anuncios = Blueprint('anuncios', __name__, template_folder='templates')

@bp_anuncios.route('/')
def listar():
    anuncios = Anuncio.query.all()
    return render_template('anuncios_listar.html', anuncios=anuncios)

@bp_anuncios.route('/crear', methods=['GET', 'POST'])
@login_required
def crear():
    categorias = Categoria.query.all()
    if request.method == 'POST':
        nuevo = Anuncio(
            titulo=request.form.get('titulo'),
            contenido=request.form.get('contenido'),
            categoria_id=request.form.get('categoria_id'),
            usuario_id=current_user.id
        )
        db.session.add(nuevo)
        db.session.commit()
        flash('Anuncio publicado', 'success')
        return redirect(url_for('anuncios.listar'))
    return render_template('anuncios_crear.html', categorias=categorias)

@bp_anuncios.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar(id):
    anuncio = Anuncio.query.get_or_404(id)
    categorias = Categoria.query.all()
    if request.method == 'POST':
        anuncio.titulo = request.form.get('titulo')
        anuncio.contenido = request.form.get('contenido')
        anuncio.categoria_id = request.form.get('categoria_id')
        db.session.commit()
        flash('Anuncio actualizado', 'info')
        return redirect(url_for('anuncios.listar'))
    return render_template('anuncios_editar.html', anuncio=anuncio, categorias=categorias)

@bp_anuncios.route('/eliminar/<int:id>')
@login_required
def eliminar(id):
    anuncio = Anuncio.query.get_or_404(id)
    db.session.delete(anuncio)
    db.session.commit()
    flash('Anuncio eliminado', 'danger')
    return redirect(url_for('anuncios.listar'))