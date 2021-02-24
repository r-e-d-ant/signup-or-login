from signup_n_login import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(28), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    
    def __repr__(self):
        return "User(Email: {0}, Username: {1})".format(self.email, self.username)