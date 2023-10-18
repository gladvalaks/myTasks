from flask import  Flask
from flask_sqlalchemy import SQLAlchemy

DESCRIPTION_TASK = "Можешь добавить в меня описание :)"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'taskMaster'
db = SQLAlchemy(app)

