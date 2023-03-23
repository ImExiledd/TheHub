from flask import Blueprint, render_template, session, send_from_directory
from flask_login import login_required, current_user
from .models import Users
from .models import Games
from . import db

restapi = Blueprint('restapi', __name__)

@restapi.route('/')
def apihome():
    return '{"version": "1","status": "indev"}'

@restapi.route('/v1/get_users')
def apigetusers():
    ourusers = Users.query.all()
    usersList = []
    for user in ourusers:
        usersList.append(user.uname)
    return f"{usersList}"

@restapi.route('/v1/get_games')
def apigetgames():
    ourGames = Games.query.all()
    gamesList = []
    for game in ourGames:
        gamesList.append(game.name)
    return f"{gamesList}"
        
@restapi.route('/v1/<int:id>/get_thumb')
def apigetgamethumb(id):
    # Figure out how to fix this later.
    ourGame = Games.query.filter_by(id=id).first()
    ourGameThumb = ourGame.thumbnail
    buildUri = "static/img/"
    return send_from_directory(buildUri, path=ourGameThumb)

@restapi.route('/v1/get_profile_picture/<path:filename>')
def getprofilepicture(filename):
    return send_from_directory("user-content/img/profiles/", filename)

@restapi.route('/v1/get_worlds_reborn')
def get_worlds_reborn():
    # Temporary, make proper defs later.
    return '{"archive": "https://cdn.imexile.moe/get-file/WorldsAdriftRebornSrc.zip"}'
