from flask import Flask
from flask_bootstrap import Bootstrap

from gmmt2app.blueprints import add_blueprints

import gmmt2app.views.basic

app = Flask(__name__)

Bootstrap(app)

add_blueprints(app)