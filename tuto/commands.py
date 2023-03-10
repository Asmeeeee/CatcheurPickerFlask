import click
from .app import app, db
from .models import Star, Utilisateur

@app.cli.command()
def syncdb():
    """
    création de tutes les tables de la BD à partir des modèles
    """
    db.create_all()

@app.cli.command()
@click.argument('filename')
def loaddb(filename):
    """
    Create all tables and populate them with data in filename
    """

    db.create_all()

    import yaml
    star = yaml.load(open(filename), Loader=yaml.FullLoader)

    # Premier passage : lecture et création des auteurs
    stars = dict()
    for s in star:
        a = s["userName"]
        if a not in stars:
            new = Utilisateur(userName = a)
            stars[a] = new
            db.session.add(new)
        # if a not in stars:
        #     nouveau = Utilisateur(userName=a)
        #     # On ajoute l'obj nouveau à la base
        #     db.session.add(nouveau)
        #     stars[a] = nouveau
    # On dit à la bd d'intégrer toutes les nouvelles données
    # Des id vont être automatiquement créés pour les auteurs
    db.session.commit()

    #Création des livres
    for b in star:
        a = stars[b["userName"]]
        diva = Star(starNom = b["LastName"],
                    starPrenom = b["Name"],
                    starDateNaiss = b["DateNaiss"],
                    starImg = b["img"],
                    starHair = b['hairColor'],
                    starHeight = b['taille'],
                    starWeight = b['poids'],
                    starOrigin = b['nationnalite'],
                    starUserName = b["userName"])
    #On ajoute l'objet o à la base
        db.session.add(diva)
    db.session.commit()

@app.cli.command()
def syncdb():
    db.create_all()

@app.cli.command()
@click.argument('username')
@click.argument('password')
def newuser(username, password):
    from .models import Utilisateur
    from hashlib import sha256
    m = sha256()
    m.update(password.encode())
    u = Utilisateur(userName=username, userPassword=m.hexdigest())
    db.session.add(u)
    db.session.commit()

@app.cli.command()
@click.argument('username')
@click.argument('password')
def passwd(username, password):
    from .models import Utilisateur
    from hashlib import sha256
    m = sha256()
    m.update(password.encode())
    Utilisateur.query.filter(Utilisateur.userName == username).update({"userPassword":m.hexdigest()})
    db.session.commit()