from datetime import datetime
from email.policy import default
from sqlalchemy import func, or_
import yaml, os.path
from .app import app, db, login_manager
from flask_login import UserMixin, current_user

def get_sample():
    if current_user.userName == "admin":
        return Star.query.limit(150).all()
    else :
         return Star.query.filter(Star.starUserName == current_user.userName).all()

def get_entire_star():
    return Star.query.all()

def get_star_detail(starid):
    return Star.query.get_or_404(starid)

def get_star_by_hair(couleur):
    if current_user.userName == "admin":
        return Star.query.filter(Star.starHair == couleur).all()
    else :
        return Star.query.filter(Star.starHair == couleur, Star.starUserName == current_user.userName).all()
def get_star_by_height():
    if current_user.userName == "admin":
        return Star.query.order_by(Star.starHeight).all()
    else :
        return Star.query.filter(Star.starUserName == current_user.userName).order_by(Star.starHeight).all()

def get_star_by_weight():
    return Star.query.filter(Star.starUserName == current_user.userName).order_by(Star.starWeight).all()

def get_star_by_origin(nationnalite="Americain"):
    if current_user.userName == "admin":
        return Star.query.filter(Star.starOrigin == nationnalite).all()
    else :
        return Star.query.filter(Star.starOrigin == nationnalite, Star.starUserName == current_user.userName).all()

def search_star(recherche):
    if current_user.userName == "admin":
        return Star.query.filter(Star.starNom.contains(recherche) | Star.starPrenom.contains(recherche))
    else :
        return Star.query.filter(Star.starNom.contains(recherche) | Star.starPrenom.contains(recherche), Star.starUserName == current_user.userName)

def get_star(id):
    return Star.query.filter(Star.starId == id)

@login_manager.user_loader
def load_user(username):
    return Utilisateur.query.get(username)

class Utilisateur(db.Model, UserMixin):
    __tablename__='utilisateur'
    #userId = db.Column(db.Integer, autoincrement=True)
    userName = db.Column(db.String(100), primary_key=True)
    userPassword = db.Column(db.String(250))

    def __repr__(self):
        return "<Utilisateur %s mot de passe : %s>" % (self.userName, self.userPassword)

    def get_id(self):
        return self.userName

class Star(db.Model):
    __tablename__='star'
    starId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    starNom = db.Column(db.String(100))
    starPrenom = db.Column(db.String(100))
    starDateNaiss = db.Column(db.Date)
    starImg = db.Column(db.String(100), default="none.png")
    starHair = db.Column(db.String(100))
    starHeight = db.Column(db.Integer)
    starWeight = db.Column(db.Integer)
    starOrigin = db.Column(db.String(100))
    starUserName = db.Column(db.String(100), db.ForeignKey("utilisateur.userName"))
    utilisateur = db.relationship("Utilisateur", backref=db.backref("utilisateur", lazy="dynamic"))

    def __repr__(self):
        return "%d %s %s %s %s %s %s %s %s" % (self.starId, self.starNom, self.starPrenom, self.starDateNaiss, self.starImg, self.starHair, self.starHeight, self.starWeight, self.starOrigin)
