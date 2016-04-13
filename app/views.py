from app import app
from flask import render_template,flash,redirect,url_for,abort,request
from .models import User
from .forms import LoginForm
from app import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        #login_user(user)

        flash('Logged in successfully.')
        flash(form.name.data)
        flash(form.password.data)
        flash(form.password.data)
        # next_is_valid should check if the user has valid
        # permission to access the `next` url
        #if not next_is_valid(next):
        #    return abort(400)


        return redirect(url_for('index'))
    return render_template('login.html',form =form)