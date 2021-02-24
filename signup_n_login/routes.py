
from signup_n_login import app, db, bcrypt # import some stuffs decraled in __init__.py
from signup_n_login.forms import SignupForm, LoginForm # import form classess
from signup_n_login.models import User # import User class, which is a table holding User

from flask import render_template, redirect, url_for, flash
# import flask_login for handling user session
from flask_login import login_user, current_user, logout_user, login_required

# home route

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", title="Home")

# signup route

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    # check if the user is trying to go at signup route when is already logged in.
    if current_user.is_authenticated:
        # redirect the user at home route if id logged in.
        return redirect(url_for('home'))
    # Init
    form = SignupForm()
    # check if all the form match the requirements to be valid
    if form.validate_on_submit():
        # hash password with bcrypt
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        # save to database
        user = User(email=form.email.data, username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Signup, successfully now you can login", "success")
        return redirect(url_for('login'))
    return render_template("signup.html", form=form, title="Signup")

# login route
@app.route("/login", methods=['GET', 'POST'])
def login():
    # check if the user is trying to go at login route when is already logged in.
    if current_user.is_authenticated:
         # redirect the user at home route if id logged in.
        return redirect(url_for('home'))
    
    # Init
    form = LoginForm()
    # check if all the form match the requirements to be valid
    if form.validate_on_submit():
        # search in database to see if the email is available
        email = User.query.filter_by(email=form.email.data).first()
        # if the email is in then check the password if is match
        if email and bcrypt.check_password_hash(email.password, form.password.data):
            # if email is valid and password then login the user
            login_user(email)
            flash("Login Welcome back", "success")
            return redirect(url_for('home'))
        else:
            flash("Something went wrong, please try again", 'danger')
    return render_template("login.html", form=form, title="Login")

# route to logout user
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

# account route
@app.route('/account')
@login_required
def account():
    return render_template("account.html", title="Account")