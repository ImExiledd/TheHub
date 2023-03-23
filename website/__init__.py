from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
lhubdb = SQLAlchemy()
DB_URI = 'mysql://exile:maxelis2@127.0.0.1/hub';
#LHUBDB_URI = 'mysql://exile:maxelis2@phoenix.imexile.moe/lolihub';


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = 'thehubv4begins'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'{DB_URI}'
    app.config['UPLOAD_FOLDER'] = "user-content/img/profiles/" # We use this folder to store user profile pictures!
    app.config["LHUB_UPLOAD_FOLDER"] = "lhub_uploads/"
    app.config['LHUB_DATABASE_URI'] = f'NULL'

    db.init_app(app)
    lhubdb.init_app(app)




    from .views import views
    from .auth import auth
    from .restful import restapi

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(restapi, url_prefix='/api')

    from .models import Users, Games

    with app.app_context():
        db.create_all()
        lhubdb.create_all()


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))

    return app

def create_database(a):
    db.create_all(app=a)
    lhubdb.create_all(app=a)
    print("[DB CREATE] DB Created Successfully")
