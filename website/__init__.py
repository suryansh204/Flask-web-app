from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) 
    app.config['SECRET_KEY'] = 'He who shall'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #initializes the database to our app
    db.init_app(app)
  
  
    
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix ='/')
    app.register_blueprint(auth, url_prefix ='/')
    from .models import Note, User
    
    with app.app_context():
        db.create_all()
        
        #where do we get redirected if we are not loggged in and login is req  
    login_mgr = LoginManager()  # Rename the variable
    login_mgr.login_view = 'auth.login'  # Specify the login route
    login_mgr.init_app(app) #telling login manager we are using app
    
    @login_mgr.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():  # Use the application context
            db.create_all()
        print('Created Database!')

    

