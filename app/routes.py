from flask import render_template, request, redirect, url_for, flash
from app import db
from app.models import User

def init_app(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/preguntas')
    def preguntas():
        return render_template('preguntas.html')

    @app.route('/chat')
    def chat():
        return render_template('chat.html')

    @app.route('/add', methods=['POST'])
    def add_user():
        title = request.form['title']
        question = request.form['question']

        if not title or not question:
            flash('Todos los campos son obligatorios.')
            return redirect(url_for('preguntas'))
        return redirect(url_for('preguntas'))

    @app.route('/delete/<int:id>')
    def delete_user(id):
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('index'))
