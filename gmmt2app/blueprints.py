from flask import Blueprint

basic_blueprint = Blueprint('basic_view', __name__, template_folder='templates')

def add_blueprints(app):
	app.register_blueprint(basic_blueprint)