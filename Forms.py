from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, IntegerField,TextAreaField
from wtforms.validators import DataRequired, NumberRange



class Task(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    coins = IntegerField('Сколько монеток', validators=[DataRequired(), NumberRange(min=0, max=10)], default=5)
    description = TextAreaField('Описание', validators=[DataRequired()])
    submit = SubmitField('Создать')


class Login(FlaskForm):
    email = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


class Registration(FlaskForm):
    email = StringField('Логин', validators=[DataRequired()])
    username = StringField('Имя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')
