import os

from flask import (Flask, g)
from flask_redis import FlaskRedis

from . import auth


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        REDIS_URL=os.environ['REDIS_URL']
    )
    g.redis_client = FlaskRedis(app=app)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(auth.bp)

    return app
