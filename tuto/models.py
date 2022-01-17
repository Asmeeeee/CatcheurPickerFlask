import yaml, os.path
from .app import app, db

def get_sample():
    return Star.query.limit(150).all()

def get_star_detail(starid):
    return Star.get(starid)

def get_user(id):
    return Utilisateur.query.get_or_404(id)

class Utilisateur(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(100))
    userLastName = db.Column(db.String(100))
    userMail = db.Column(db.String(100))
    userPassword = db.Column(db.String(100))

    def __repr__(self):
        return "<Utilisateur (%d) %s>" % (self.userName, self.userLastName)

class Star(db.Model):
    starId = db.Column(db.Integer, primary_key=True)
    starNom = db.Column(db.String(100))
    starPrenom = db.Column(db.String(100))
    starDateNaiss = db.Column(db.String(100))
    starImg = db.Column(db.String(100))
    star = db.relationship("Utilisateur", backref=db.backref("star", lazy="dynamic"))
    userId = db.Column(db.Integer, db.ForeignKey("utilisateur.userId"))

    def __repr__(self):
        return "<Star (%d) %s>" % (self.starNom, self.starPrenom)

