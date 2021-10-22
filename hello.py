from flask import Flask, render_template, session, redirect, url_for, flash
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if fform.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and Old_name != form.name.data:
			flash('Looks like you have changed your name!')
		session['name'] = form.name.data
		form.name.data = ''
		return redirect(url_for('index'))
	return render_template('index.html', form = form, name = session.get('name'))

if __name__ == '__main__':
	app.run(debug=True)		
