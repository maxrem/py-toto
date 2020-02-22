import os

from flask import Flask
from flask_redis import FlaskRedis


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        REDIS_URL=os.environ['REDIS_URL']
    )
    redis_client = FlaskRedis(app=app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        redis_client.sadd('test', 'test value')

        return redis_client.get('test')
        # return os.environ['REDIS_URL']

    return app
