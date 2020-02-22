from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, g
)
from werkzeug.security import generate_password_hash


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        redis_client = g.redis_client
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif redis_client.hget('username', username):
            error = 'User {} is already registered.'.format(username)

        if error is None:
            redis_client.hset('username', username)
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')
