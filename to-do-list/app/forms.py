from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DateRequired

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
   task = StringField('Task',[validators=[DataRequired(), TaskCheck(message='Already Exists')])
   submit = SubmitField('Enter Task')

