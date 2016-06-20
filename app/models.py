from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % self.username

class OnboardRequest(db.Model):
    __tablename__ = 'onboard_request'
    id = db.Column(db.Integer, primary_key=True)
    software_product = db.Column(db.String(64))
    sharepoint_path = db.Column(db.Text())
    milestone_name = db.Column(db.String(64))
    test_cycle = db.Column(db.String(24))
    create_date = db.Column(db.DateTime(), default=datetime.utcnow)
    active = db.Column(db.Boolean, default=False)
    requester = db.Column(db.String(64))

    def __repr__(self):
        return '<Onboard request %r from %r>'%(self.software_product, self.requester)

class SharepointServer(db.Model):
    __tablename__ = 'sharepoint_server'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128),unique=True,index=True)

    def __repr__(self):
        return '<Sharepoint server %d>'%self.id

