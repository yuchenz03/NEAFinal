from flask import Flask

def create_app(): #This function sets up the flask application.
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret O.O'
    
    from .views import views
    from .login import login
    
    #to access whatever is within the file specified, the url will have /prefix/ruote.
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(login, url_prefix='/')
    
    return app
    