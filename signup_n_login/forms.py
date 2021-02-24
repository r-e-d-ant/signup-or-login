from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from signup_n_login.models import User

class SignupForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=28)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=2, max=120)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password", message="Password must be match")])
    submit_btn = SubmitField("register")
    
    # check if the email is alreadt taken
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError("That email is taken, please choose different one")
        
    # check if the username is alreadt taken
    def validate_username(self, username):
        user_name = User.query.filter_by(username=username.data).first()
        if user_name:
            raise ValidationError("That username is taken, please choose different one")
    
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit_btn = SubmitField("login")