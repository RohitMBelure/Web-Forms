from flask import Flask
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app =  Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

class NameForm(Form):
	name = stringField('What is your name?', validators=[Reuired()])
	submit = SubmitField('Submit')

if __name__ == '__main__':
	app.run(debug=True)
