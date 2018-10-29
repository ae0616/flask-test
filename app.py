from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '0937b3b06278447b1fef94399df77313'

postit = [
    {
        'author': 'Andrew Engelhard',
        'title': 'Blog post 1',
        'content': 'First post',
        'date_posted': 'October 25, 2018'
    },
    {
        'author': 'Andrew Engelhard',
        'title': 'Blog post 2',
        'content': 'Hey there',
        'date_posted': 'October 25, 2018'
    },
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='home', posts=postit)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for(home))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = RegistrationForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(ssl_context='adhoc')
