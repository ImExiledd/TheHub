from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
DB_URI = 'mysql://exile:maxelis2@phoenix.imexile.moe/hubv4test';


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = 'thehubv4begins'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'{DB_URI}'
    app.config['UPLOAD_FOLDER'] = "user-content/img/profiles/" # We use this folder to store user profile pictures!

    db.init_app(app)




    from .views import views
    from .auth import auth
    from .restful import restapi

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(restapi, url_prefix='/api')

    from .models import Users, Games

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))

    return app

def create_database(a):
    db.create_all(app=a)
    print("[DB CREATE] DB Created Successfully")