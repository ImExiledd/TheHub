from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import Games, Users
from modules import bcrypt as bc
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        useremail = request.form.get("UserEmail")
        userpasswd = request.form.get("UserPasswd")
        
        user = Users.query.filter_by(email=useremail).first()
        
        if user:
            if bc.HashTools.CheckHash(userpasswd, user.pwdhash):
                login_user(user, remember=True)
                session["uid"] = user.id
                session["username"] = user.uname
                session["profpic"] = user.userProfilePicture
                session["invcode"] = user.INVITE_CODES
                session["admin"] = user.IS_ADMIN
                return redirect(url_for('views.home'))
            else:
                flash(f"Invalid username or password")
    
    return  render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route('/register', methods=['POST', 'GET'])
def register():
    #new_user = Users(
    #    uname="Exile",
    #    pwdhash = bc.HashTools.HashPassword("maxelis2"),
    #    email="csxkingjp@gmail.com",
    #    IS_ADMIN = 1,
    #    ayako_member = 0,
    #    INVITE_CODES = "12345678",
    #    IsBannedUser = 0,
    #    UsedInviteCodes = "",
    #    RulesAccepted = 1,
    #    is_hub_authed = 1,
    #    userProfilePicture = "#",
    #    pwdResetCode = "#"
    #)
    #db.session.add(new_user)
    #db.session.commit()
    return "<p>Register</p>"