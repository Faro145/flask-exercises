from flask import render_template, request, redirect, url_for
from app import app
from app.models import Todo
from app import db
from app.forms import todoForm

@app.route('/')
def index():
    all_todo = Todo.query.all()
    return render_template('index.html', all_todo=all_todo)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = todoForm()
    if form.validate_on_submit():
        new_todo = Todo(text=form.text.data)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.route('/complete/<int:id>')
def complete(id):
    todo_to_update = Todo.query.get(id)
    todo.complete = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/incomplete/<int:id>')
def incomplete(id):

    todo_to_update = Todo.query.get(id)
    todo_to_update.complete = False
    db.session.commit()
    return redirect(url_for('index')


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = (todoForm)
    todo_to_update = Todo.query.get(id)
    if form.validate_on_submit():
        todo_to_update.text = form.text.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.text.data = todo_to_update.text

    return render_template('update.html', form=form)

@app.route('/delete/<int:id>')
def delete(id):
    todo_to_delete = Todo.query.get(id)
    db.session.delete(todo_to_delete)
    db.session.commit()
    return redirect(url_for('index'))
