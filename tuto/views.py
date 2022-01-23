from .app import app, db
from flask import flash, render_template, redirect, request, session, url_for
from .models import *
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, validators, SubmitField, SelectField, DateField, FileField
from wtforms.validators import DataRequired

class CreateStar(FlaskForm):
    id = HiddenField('id')
    prenom = StringField('Prénom', validators =[validators.InputRequired()])
    nom = StringField('Nom', validators =[validators.InputRequired()])
    dateNaiss = DateField('Date de naissance')
    origin = SelectField('Nationnalité', [DataRequired()], choices =[
                                                                    ('inconnu', 'Inconnu'),
                                                                    ('francaise', 'Française'),
                                                                    ('americaine', 'Américaine'),
                                                                    ('africaine', 'Africaine'),
                                                                    ('asiatique', 'Asiatique'),
                                                                    ('mexicaine', 'Mexicaine'),
                                                                    ('russe', 'Russe'),
                                                                    ('italienne', 'Italienne'),
                                                                    ('arabe', 'Arabe')
                                                                    ])
    img = FileField('Image')
    height = StringField('Taille', validators =[validators.InputRequired()])
    weight = StringField('Poids', validators =[validators.InputRequired()])
    hairColor = SelectField('Couleur de cheveux', [DataRequired()], choices =[
                                                                             ('blond', 'Blond'),
                                                                             ('brun', 'Brun'),
                                                                             ('roux', 'Roux'),
                                                                             ('noir', 'Noir'),
                                                                             ('chauve', 'Chauve'),
                                                                             ('fantaisie', 'Fantaisie')
                                                                             ])
    submit = SubmitField("Save")
    submitRemove = SubmitField("Remove")

@app.route("/")
def home():
    return render_template(
        "home.html",
        title = "Liste des catcheur(ses)",
        stars = get_sample()
    )

@app.route("/hairColor/", methods=['GET', 'POST'])
def hairColor():
    couleur = request.form['hairColorChoice']
    return render_template("home.html", stars = get_star_by_hair(couleur))

@app.route("/Height")
def height():
    return render_template("home.html", stars = get_star_by_height())

@app.route("/Weight")
def weight():
    return render_template("home.html", stars = get_star_by_weight())

@app.route("/Origin/", methods=['GET', 'POST'])
def origin():
    origin = request.form['originChoice']
    return render_template("home.html", stars = get_star_by_origin(origin))

@app.route("/Safe")
def safe():
    return render_template("home.html", stars = get_safe_mode())

@app.route("/recherche", methods=['GET', 'POST'])
def recherche():
    recherche = request.form["recherche"]
    print(recherche)
    return render_template("home.html", stars = search_star(recherche))


@app.route("/editSupprimer")
def editSupprimer():
    return render_template( 'edit/editSupprimer.html' )

@app.route("/editAjouter", methods=['GET', 'POST'])
def editAjouter():
    form = CreateStar()
    if form.img.data == "":
        img = "none.png"
    else :
        img = form.img.data
    if form.submit.data:
        try:
            star = Star(
                        starNom=form.nom.data, 
                        starPrenom=form.prenom.data, 
                        starDateNaiss=form.dateNaiss.data, 
                        starImg=img, 
                        starHair=form.hairColor.data, 
                        starHeight=form.height.data, 
                        starWeight=form.weight.data, 
                        starOrigin=form.origin.data, 
                        userMail=1)
            db.session.add(star)
            db.session.commit()
        except:
            print("Erreur lors de l'insertion")
        flash('Merci pour votre Star')
        return redirect("/editAjouter")
    return render_template( '/edit/editAjouter.html', form=form )



@app.route("/editModifier/<int:id>", methods=['GET', 'POST'])
def editStar(id):
    a = get_star_detail(id)
    f = CreateStar(id=id, prenom=a.starPrenom, nom=a.starNom, img=a.starImg, height=a.starHeight, weight=a.starWeight, hairColor=a.starHair, origin=a.starOrigin, dateNaiss=a.starDateNaiss)
    if f.submitRemove.data:
        db.session.delete(a)
        db.session.commit()
        flash("Vous avez supprimé le catcheur")
        return redirect("/")
    if f.img.data == "":
        imgEdit = a.starImg
    else :
        imgEdit = f.img.data
    
    if f.submit.data:
        Star.query.filter(Star.starId == id).update({"starNom": f.nom.data,
                                                     "starPrenom": f.prenom.data, 
                                                     "starDateNaiss": f.dateNaiss.data, 
                                                     "starImg": imgEdit, 
                                                     "starHair": f.hairColor.data,
                                                     "starHeight": f.height.data,
                                                     "starWeight": f.weight.data,
                                                     "starOrigin": f.origin.data})
        db.session.commit()
    return render_template("edit/editModifier.html", star = a, formEdit = f, id=id)

@app.route("/save/author/", methods=["POST"])
def save_author():
    f = AuthorForm()
    # si on est en update d'author
    if f.id.data != "":
        id = int(f.id.data)
        a = get_star(id)
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
