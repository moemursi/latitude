from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)

db = SQLAlchemy(app)

class User(db.model):
    __tablename__ = 'users'
    uid = db.column(db.Integer, primary_key = True)
    firstname = db.column(db.String(100))
    lastname = db.column(db.String(100))
    email = db.column(db.String(120), unique = True)
    pwdhash = db.column(db.String(54))

    def __init__(self, firstname , lastname , email , password):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.email =  email.lower()
        self.set_password(password)
    
    def set_password (self, password):
        self.pwdhash = generate_password_hash(password)
    
    def check_password (self,password):
        return check_password_hash(self.pwdhash, password)
