from flask import flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URL'] = "sqlite:///"

if __name__ == "__main__":
    app.run(debug=True)


