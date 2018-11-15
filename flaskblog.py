from flask import Flask, render_template, url_for
app = Flask(__name__)

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


if __name__ == '__main__':
	app.run(debug=True)