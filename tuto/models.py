import yaml, os.path
from .app import app, db

Books = yaml.load(
    open(
        os.path.join(
            os.path.dirname(__file__),
            "data.yml"
        )
    ), Loader=yaml.FullLoader
)

def get_sample():
    return Book.query.limit(1000).all()

def get_book_detail(bookid):
    return Book.get(bookid)

def get_author(id):
    return Author.query.get_or_404(id)

def get_star_detail(starid):
    return Star.query.get_or_404(starid)

class Star(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    prenom = db.Column(db.String(100))
    dateNaiss = db.Column(db.String(100))
    img = db.Column(db.String(100))

    def __repr__(self):
        return "<Star (%d) %s>" % (self.nom, self.prenom)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return "<Author (%d) %s>" % (self.id, self.name)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    title = db.Column(db.String(120))
    url = db.Column(db.String(250))
    author = db.relationship("Author", backref=db.backref("books", lazy="dynamic"))
    img = db.Column(db.String(90))
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))

    def __repr__(self):
        return "<Book (%d) %s>" % (self.id, self.title)