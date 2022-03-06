from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    '''
    View function that set display on home page
    '''
    title = "HOME"
    return render_template('index.html', title=title)

@app.route('/login', methods=['GET','POST'])
def login():
    '''
    View function that set display on login page
    '''
    if current_user.is_authenicated:
        '''
        Redirects logged in user to home page
        '''
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        '''
        Creates user variable after successful login
        Methods:
            first assigns the unique username to be true
        '''
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            '''
            Condition to handle invalid user input
            Returns:
                Invalid response retains user on login page 
                Valid reponse redirects user to the authorized home page
            '''
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash('You are logged in succesfully')
        return redirect(url_for('index'))
    title = "LogIn"
    return render_template('login.html', title=title, form=form )