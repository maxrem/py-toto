from flask import Flask
from toto.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from toto import routes