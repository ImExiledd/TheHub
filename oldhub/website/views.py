import random
import string
from flask import Blueprint, render_template, session, send_from_directory
from flask_login import login_required, current_user

from flask_wtf import FlaskForm

from .models import Users
from .models import Games
from . import db

from werkzeug.utils import secure_filename
from wtforms import FileField, SubmitField

from flask import current_app
import os

views = Blueprint('views', __name__)

class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")


@views.route('/', methods=["GET", "POST"])
@login_required
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # Get file
        # get file extension first
        splitme = os.path.splitext(file.filename)
        ourExt = splitme[1]
        ourFileName = str(''.join(random.choices(string.ascii_letters, k=24))) + ourExt
        ourFileUri = f"/api/v1/get_profile_picture/{ourFileName}"
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),current_app.config['UPLOAD_FOLDER'],secure_filename(ourFileName))) # Then save the file
        # Next, we need to update the database!
        OurUserToUpdate = Users.query.filter_by(id=int(session["uid"])).first()
        OurUserToUpdate.userProfilePicture = f"{ourFileUri}"
        db.session.commit()
        
    if "uid" in session:
        userid = session["uid"]
        uname = session["username"]
        profpic = session["profpic"]
        invcode = session["invcode"]
        isadmin = session["admin"]
        games = Games.query.all()
        return render_template("games.html", uname=uname, profpic=profpic, invcode=invcode, isadmin=isadmin, games=games, form=form)
    else:
        return "403"

@views.route("/img/v2_games/<path:filename>")
@login_required
def image(filename):
    return send_from_directory("static/img/v2_games/", filename)

@views.route("logos/<path:filename>")
@login_required
def logo(filename):
    return send_from_directory("static/img/", path=filename + ".png")

@views.route("/attain/<path:filename>")
@login_required
def download(filename):
    games_folder = "/var/www/html/hub_games/"
    return send_from_directory(games_folder, path=filename)

@views.route("/admin", methods=["POST", "GET"])
@login_required
def admin():
    if session["admin"] == 1:
        if "uid" in session:
            userid = session["uid"]
            uname = session["username"]
            profpic = session["profpic"]
            invcode = session["invcode"]
            isadmin = session["admin"]
            games = Games.query.all()
            return render_template("admin.html", uname=uname, profpic=profpic, invcode=invcode, isadmin=isadmin, games=games)
    elif session["admin"] == 0:
        return render_template("403.html")
