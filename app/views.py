from app import app
from flask import render_template,flash,redirect,url_for,abort,request,session,g
from .models import User,ReportModel,KanshouModel,TongbaoModel
from .forms import LoginForm,ReportForm
from flask.ext.login import login_user, login_required, logout_user, current_user
from app import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(nickname = form.name.data).first()
        if user is not None and user.password == form.password.data:
        # Login and validate the user.
        # user should be an instance of your `User` class
            login_user(user)
            return redirect(url_for('add'))
        else:
            error = '登录失败,请重新登录！'
    return render_template('login.html',form = form,error = error)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.before_request
def before_request():
    g.user = current_user

@app.route("/add")
@login_required
def add():
    username = g.user.nickname
    form = ReportForm()
    return render_template('add.html',username = username)