from datetime import datetime
from email.policy import default
from sqlalchemy import func
import yaml, os.path
from .app import app, db

def get_sample():
    return Star.query.limit(150).all()

def get_star_detail(starid):
    return Star.query.get_or_404(starid)

def get_star_by_hair(couleur):
    return Star.query.filter(Star.starHair == couleur).all()

def get_star_by_height():
    return Star.query.order_by(Star.starHeight).all()

def get_star_by_weight():
    return Star.query.order_by(Star.starWeight).all()

def get_star_by_origin(nationnalite="Americain"):
    return Star.query.filter(Star.starOrigin == nationnalite).all()

def get_safe_mode():
    return Star.query.filter(Star.starId == 1)

# def get_lastId():
#     max_id = db.session.query(func.max(Star.starId)).scalar()
#     return max_id + 1 

def get_star(id):
    return Star.query.filter(Star.starId == id)

class Utilisateur(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(100))
    userLastName = db.Column(db.String(100))
    userMail = db.Column(db.String(100))
    userPassword = db.Column(db.String(100))

    def __repr__(self):
        return "<Utilisateur (%d) %s>" % (self.userName, self.userLastName)

class Star(db.Model):
    starId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    starNom = db.Column(db.String(100))
    starPrenom = db.Column(db.String(100))
    starDateNaiss = db.Column(db.Date)
    starImg = db.Column(db.String(100), default="none.png")
    starHair = db.Column(db.String(100))
    starHeight = db.Column(db.Integer)
    starWeight = db.Column(db.Integer)
    starOrigin = db.Column(db.String(100))
    star = db.relationship("Utilisateur", backref=db.backref("star", lazy="dynamic"))
    userMail = db.Column(db.String(100), db.ForeignKey("utilisateur.userMail"))

    def __repr__(self):
        return "%d %s %s %s %s %s %s %s %s" % (self.starId, self.starNom, self.starPrenom, self.starDateNaiss, self.starImg, self.starHair, self.starHeight, self.starWeight, self.starOrigin)
