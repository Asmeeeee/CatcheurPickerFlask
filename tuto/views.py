from .app import app, db
from flask import render_template, redirect, url_for
from .models import *
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
        stars = get_sample()
    )

@app.route("/hairColor/<string:couleur>")
def hairColor(couleur):
    return render_template("home.html", stars = get_star_by_hair(couleur))

@app.route("/Size")
def size():
    return render_template("home.html", stars = get_star_by_size())

@app.route("/Heigh")
def heigh():
    return render_template("home.html", stars = get_star_by_heigh())

@app.route("/Origin/<string:origin>")
def origin(origin):
    return render_template("home.html", stars = get_star_by_origin(origin))


@app.route("/editSupprimer")
def editSupprimer():
    return render_template( 'edit/editSupprimer.html' )

@app.route("/editAjouter")
def editAjouter():
    return render_template( 'edit/editAjouter.html' )    


# @app.route("/editModifier")
# def editModifier():
#     return render_template( 'edit/editModifier.html' )   


@app.route("/editModifier/<int:id>")
def edit_author(id=None):
    print(id)
    nom = None
    if id is None:
        a = get_sample(id)
        nom = a.name
    else :
        a = ("Salut", "Mon", "Pote")
    print(id, a, nom)

    f = AuthorForm(id=id, name=nom)
    return render_template( "edit/editModifier.html", star = a, form = f)

@app.route("/save/author/", methods=["POST"])
def save_author():
    f = AuthorForm()
    # si on est en update d'author
    if f.id.data != "":
        id = int(f.id.data)
        a = get_user(id)
    else : # on n'a pas d'ID ==> création d'Author
        a = Utilisateur(userName=f.name.data)
        db.session.add(a)
    if f.validate_on_submit():
        a.name = f.name.data
        #on sauvegarde l'auteur
        db.session.commit()
        id = a.id
        return redirect(url_for("one_author", id=id))
    return render_template("edit_author.html",author=a, form=f)

@app.route("/.../")
def one_author(id):
    user = get_user(id)
    return render_template(
        "home.html",
        title = "Livre de " + user.name, books=user.name)
