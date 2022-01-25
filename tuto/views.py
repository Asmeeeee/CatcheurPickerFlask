from email.mime import image
import os
from re import U
from .app import app, db
from flask import abort, flash, render_template, redirect, request, session, url_for
from .models import *
from flask_wtf import FlaskForm
from hashlib import sha256
from werkzeug.utils import secure_filename
from wtforms import StringField, HiddenField, validators, SubmitField, SelectField, DateField, FileField, PasswordField
from wtforms.validators import DataRequired
from flask_login import login_user, current_user, logout_user

class LoginForm(FlaskForm):
    username = StringField("Nom d'utilisateur")
    password = PasswordField("Mot de passe")

    def get_authenticated_user(self):
        user = Utilisateur.query.get(self.username.data)
        if user is None:
            return None
        m = sha256()
        m.update(self.password.data.encode())
        passwd = m.hexdigest()
        return user if passwd == user.userPassword else None

class CreateStar(FlaskForm):
    id = HiddenField('id')
    prenom = StringField('Prénom', validators =[validators.InputRequired()])
    nom = StringField('Nom', validators =[validators.InputRequired()])
    dateNaiss = DateField('Date de naissance')
    origin = SelectField('Nationnalité', [DataRequired()], choices =[
                                                                    ('Inconnu', 'Inconnu'),
                                                                    ('Française', 'Française'),
                                                                    ('americaine', 'Américaine'),
                                                                    ('Américaine', 'Africaine'),
                                                                    ('asiatique', 'Asiatique'),
                                                                    ('Asiatique', 'Mexicaine'),
                                                                    ('Russe', 'Russe'),
                                                                    ('Italienne', 'Italienne'),
                                                                    ('Arabe', 'Arabe')
                                                                    ])
    img = FileField("Image")
    height = StringField('Taille', validators =[validators.InputRequired()])
    weight = StringField('Poids', validators =[validators.InputRequired()])
    hairColor = SelectField('Couleur de cheveux', [DataRequired()], choices =[
                                                                             ('Blond', 'Blond'),
                                                                             ('Brun', 'Brun'),
                                                                             ('Roux', 'Roux'),
                                                                             ('Noir', 'Noir'),
                                                                             ('Chauve', 'Chauve'),
                                                                             ('Fantaisie', 'Fantaisie')
                                                                             ])
    submit = SubmitField("Save")
    submitRemove = SubmitField("Remove")

@app.route("/")
def home():
    return render_template(
        "home.html",
        stars = get_sample(),
        title="Liste des catcheurs"
    )

@app.route("/hairColor/", methods=['GET', 'POST'])
def hairColor():
    couleur = request.form['hairColorChoice']
    return render_template("home.html", stars = get_star_by_hair(couleur), title="Liste des catcheurs %s" % couleur)

@app.route("/Height")
def height():
    return render_template("home.html", stars = get_star_by_height(), title="Liste des catcheurs triés par taille croissante")

@app.route("/Weight")
def weight():
    return render_template("home.html", stars = get_star_by_weight(), title="Liste des catcheurs triés par poids croissant")

@app.route("/Origin/", methods=['GET', 'POST'])
def origin():
    origin = request.form['originChoice']
    return render_template("home.html", stars = get_star_by_origin(origin), title="Liste des catcheurs de nationnalité %s" % origin)

@app.route("/recherche", methods=['GET', 'POST'])
def recherche():
    recherche = request.form["recherche"]
    return render_template("home.html", stars = search_star(recherche), title="Résulat pour la recherche : %s" % recherche)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    f = LoginForm()
    if f.validate_on_submit():
        user = f.get_authenticated_user()
        if user:
            login_user(user)
            return redirect(url_for("home"))
    return render_template("login.html", form=f)

@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_img(form):
    imageChoice = form.img.data
    if str(imageChoice).split("'")[1] == "":
        return "none.png"
    filename = secure_filename(imageChoice.filename)
    if filename != '':
        file_extension = os.path.splitext(filename)[1]
        if file_extension not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
    imageChoice.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return str(imageChoice).split("'")[1]

@app.route("/editAjouter", methods=['GET', 'POST'])
def editAjouter():
    form = CreateStar()
    if form.submit.data:
        img = save_img(form)
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
                            starUserId=1)
            db.session.add(star)
            db.session.commit()
        except :
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
    
    if f.submit.data:
        print(f.img.data)
        if str(f.img.data).split("'")[1] == "":
            imgEdit = a.starImg
        else :
            imgEdit = save_img(f)
        print(imgEdit)
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
