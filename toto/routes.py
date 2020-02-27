from flask import render_template

from toto import app


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
