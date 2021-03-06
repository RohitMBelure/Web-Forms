from flask import Flask
from flask_sqlalchemy import SQLAlchemy, os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
	'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)	

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	
	def __repr__(self):
		return '<Role %r>' % self.name
	
class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)
	
	def __repr__(self):
		return '<User %r>' % self.username

class Role(db.Model):
	
	users = db.relationship('User', backref='role')

class User(db.Model):

	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
