import uuid
from flask import Blueprint, render_template, session, send_from_directory
from flask_login import login_required, current_user
import pathlib
from flask_wtf import FlaskForm

from .lhub_models import Posts
from . import db

from werkzeug.utils import secure_filename
from wtforms import FileField, SubmitField

from flask import current_app
import os

lhub = Blueprint('lhub', __name__)

class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")


@lhub.route('/lolihub', methods=["GET", "POST"])
def lhub():

    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        ourRandomFileName = uuid.uuid4()
        ourRandomFileExt = file_extension = pathlib.Path(file.filename).suffix
        ourRandomFileName = str(ourRandomFileName) + str(ourRandomFileExt)
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),current_app.config["UPLOAD_FOLDER"],secure_filename(ourRandomFileName)))
        ourNewFile = Posts(fileLocation=f"uploads/{ourRandomFileName}")
        db.session.add(ourNewFile)
        db.session.commit()
    lewds = Posts.query.all()
    for lewd in lewds:
        print(lewd.fileLocation)
    return render_template("lhub_home.html", lewds=lewds, form=form)

@lhub.route("/lhub_uploads/<path:filename>")
def image(filename):
    return send_from_directory("lhubuploads/", filename)
