from flask import render_template, redirect, url_for

from toto import app
from toto.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Max'}
    posts = [
        {
            'author': {'username': 'Henk'},
            'body': 'Henkie penkie'
        },
        {
            'author': {'username': 'Jan'},
            'body': 'Jantje Piet'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()

    if form.validate_on_submit():
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=form)
