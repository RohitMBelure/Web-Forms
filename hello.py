from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	name=None
	form=NameForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template('index.html', form=form, name=name)
	
if __name__ == '__main__':
	app.run(debug=True)
