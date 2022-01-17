from .app import app, db
from flask import render_template, redirect, url_for
from .models import Author, get_sample, get_book_detail, get_author
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, validators
#from wtforms.validators import DataRequired, validators

class AuthorForm(FlaskForm):
    id = HiddenField('id')
    #name = StringField('Nom', [validators.InputRequired(), validators.Lenght(min=2, max=25, message = "Le nom doit avoir entre 2 et 25 caractères mon pote !", validators.Regexp('a-zA-Z]+$', message = "Le nom doit avoir entre 2 et 25 caractères mon pote !"))])
    name = StringField('Nom', validators =[validators.InputRequired()])

@app.route("/")
def home():
    return render_template(
        "home.html",
        title = "Listes de film pour se faire chier",
        books = get_sample()
    )

@app.route("/edit")
def edit():
    return render_template( 'edit.html' )


@app.route("/edit/author/<int:id>")
def edit_author(id=None):
    nom = None
    if id is None:
        a = get_author(id)
        nom = a.name
    else :
        a = None

    f = AuthorForm(id=id, name=nom)
    return render_template( "edit_author.html", author = a, form = f)

@app.route("/save/author/", methods=["POST"])
def save_author():
    f = AuthorForm()
    # si on est en update d'author
    if f.id.data != "":
        id = int(f.id.data)
        a = get_author(id)
    else : # on n'a pas d'ID ==> création d'Author
        a = Author(name=f.name.data)
        db.session.add(a)
    if f.validate_on_submit():
        a.name = f.name.data
        #on sauvegarde l'auteur
        db.session.commit()
        id = a.id
        return redirect(url_for("one_author", id=id))
    return render_template("edit_author.html",author=a, form=f)

@app.route("/author/<int:id>")
def one_author(id):
    auteur = get_author(id)
    return render_template(
        "home.html",
        title = "Livre de " + auteur.name, books=auteur.book)