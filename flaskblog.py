from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '1ca05a90cae867c466c6acddf8fc211a'

posts = [
	{
		'author': 'karolat',
		'title': 'first post',
		'content': 'serene',
		'date_posted': '14 Nov, 2018'
	},
		{
		'author': 'karolat',
		'title': 'post 2',
		'content': 'unsure',
		'date_posted': '15 Nov, 2018'
	},
		{
		'author': 'karolat',
		'title': 'Third Post',
		'content': 'Feel a lot more sure.  And happy and hopeful!  And hope Shiro beats his fever soon <3',
		'date_posted': '15 Nov, 2018'
	}

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
    	flash(f'Account created for {form.username.data}!', 'success')
    	return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
    	if form.email.data == 'karolat@gmail.com' and form.password.data == 'password':
    		flash('successful login', 'success')
    		return redirect(url_for('home'))
    	else:
    		flash('login unsuccessful. please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
	app.run(debug=True)