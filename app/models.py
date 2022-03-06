from app import db


class User(db.Model):
    '''
    Class that define user instance with its attributes
    Args:
        This user class inherits from db.model in flask-sqlalchemy base class
    Returns:
        Instances are created as instances of the db.column
        __repr__ method tells python how to print objects of this class
    '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)