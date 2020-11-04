from flask import render_template, request, redirect, url_for
from app import app
from app.models import Todo
from app import db

@app.route('/')
def index():
        all_todo = Todo.query.all()
	incomplete = Todo.query.filter_by(complete=False).all()
	complete = Todo.query.filter_by(complete=True).all()

	return render_template('index.html', all_todo=all_todo, incomplete=incomplete, complete=complete)


@app.route('/add', methods=['POST'])
def add():
        form = TaskForm9)
        if form.validate_on_submit():
	todo = Todo(text=request.form['todoitem'], complete=False)
	db.session.add(todo)
	db.session.commit()
        return
	return redirect(url_for('index'))

@app.route('/incomplete/<id>')
def incomplete(id):

    todo = Todo.query.filter_by(id=int(id)).first()
    todo.incomplete = True
    db.session.commit()
    return redirect(url_for('index')


@app.route('/complete/<id>')
def complete(id):

    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = True
    db.session.commit()
    return redirect(url_for('index')


@app.route('/update', methods=['POST'])
def update(task):
	todo_to_update = Todo.query.get(id)
        todo_to_update.complete = False
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/delete', methods=['POST'])
def delete():
        todo = Todo.query.first()
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for('index'))
