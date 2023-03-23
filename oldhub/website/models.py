from . import db
from flask_login import UserMixin

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(10000))
    name = db.Column(db.String(256))
    size = db.Column(db.String(256))
    description = db.Column(db.String(256))
    uri = db.Column(db.String(256))
    thumbnail = db.Column(db.String(256))
    mp = db.Column(db.String(256))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(150))
    pwdhash = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    IS_ADMIN = db.Column(db.Integer)
    ayako_member = db.Column(db.Integer)
    INVITE_CODES = db.Column(db.String(8))
    EXPIRY = db.Column(db.DateTime)
    IsBannedUser = db.Column(db.Integer)
    UsedInviteCodes = db.Column(db.String(8), unique=True)
    RulesAccepted = db.Column(db.Integer)
    is_hub_authed = db.Column(db.Integer)
    userProfilePicture = db.Column(db.String(900))
    pwdResetCode = db.Column(db.String(900))