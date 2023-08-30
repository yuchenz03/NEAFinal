from flask import Blueprint

#Define that this file is a blueprint of our application - it has a bunch of URLs. 
views = Blueprint('views', __name__)

@views.route('/') #route is '/'
def home():
    return "<h1>Test<h1>"