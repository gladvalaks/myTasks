from flask import Flask, render_template, request, session, redirect
from Database import *
import Forms
from Consts import *


def is_user_in_session():
    return 'username' in session


def get_taks_by_user(user_id):
    tasks = Task.query.filter_by(user_id=user_id).all()
    return tasks


def create_task(name, coins, description):
    user = db.session.query(User).filter_by(id=session['user_id']).first()
    if description:
        task = Task(name=name, description=description, coins=coins)
    else:
        task = Task(name=name, description=DESCRIPTION_TASK, coins=coins)
    user.Task.append(task)
    db.session.commit()


def auth(mail, password_to_check):
    user = db.session.query(User).filter_by(email=mail).first()
    if user and user.password == password_to_check:
        session['username'] = user.username
        session['user_id'] = user.id
        return True
    return False


@app.route('/logout')
def logout():
    if is_user_in_session():
        del session['username']
    return redirect('/base')


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = Forms.Login()
    if form.validate_on_submit():
        if auth(form.email.data, form.password.data):
            return redirect('/base')
    return render_template("login.html", form=form, user_in_session=is_user_in_session())


@app.route('/mytasks', methods=['POST', 'GET'])
def my_tasks():
    if is_user_in_session():
        form = Forms.Task()
        if form.validate_on_submit():
            create_task(name=form.name.data, coins=form.coins.data, description=form.description.data)
        return render_template("mytasks.html", user_in_session=is_user_in_session(), form=form,
                               dictionary=get_taks_by_user(session['user_id']))
    else:
        return redirect('/login')


@app.route('/')
@app.route('/base', methods=['POST', 'GET'])
def base():
    if request.method == "GET":
        return render_template("base.html", title="HI", user_in_session=is_user_in_session())


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = Forms.Registration()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        auth(user.email, user.password)
        return redirect('/base')
    return render_template("register.html", form=form, user_in_session=is_user_in_session())


if __name__ == '__main__':
    db.create_all()
    app.run(port=8080, host='127.0.0.1')
