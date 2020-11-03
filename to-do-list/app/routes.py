from flask import render_template, request, redirect, url_for
from app import app
from app.models import Todo
from app import db


@app.route('/')
def index():
	incomplete = Todo.query.filter_by(complete=False).all()
	complete = Todo.query.filter_by(complete=True).all()

	return render_template('index.html', incomplete=incomplete, complete=complete)


@app.route('/add', methods=['POST'])
def add():
	todo = Todo(text=request.form['todoitem'], complete=False)
	db.session.add(todo)
	db.session.commit()

	return redirect(url_for('index'))

@app.route('/incomplete/<id>')
def incomplete:

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
def update():
	todo = Todo.query.filter_by(id=int(id)).first()
        todo.session.update(todo)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/delete', methods=['POST'])
def delete():
        todo = Todo.query.filter_by(id=int(id)).first()
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for('index'))
