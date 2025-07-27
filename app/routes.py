from flask import Blueprint
from markupsafe import escape

home = Blueprint("home", __name__)

@home.route('/')
def hello():
    return '<h1>Welcome to this application. </h1>'

@home.route('/about')
def about():
    return '<h3>This is a Flask web application. </h3>'

@home.route('/capitalize/<word>')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.upper()))