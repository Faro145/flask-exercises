from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from app.models import Todo

class TaskCheck:
        def __init__(self, message):
            self.message = message
         def __call__(self.form.field):
             all_todo = Todo.query.all()
             for todo in all_todo:
                 if todo.task == field.task 
                    raise ValidationError(self.message)

class todoForm(FlaskForm):
   task = StringField('Task')
   submit = SubmitField('Enter Task')

