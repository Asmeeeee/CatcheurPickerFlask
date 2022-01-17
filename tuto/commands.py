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
        a = s["idUser"]
        if a not in stars:
            nouveau = Star(starNom=a)
            # On ajoute l'obj nouveau à la base
            db.session.add(nouveau)
            star[a] = nouveau
    # On dit à la bd d'intégrer toutes les nouvelles données
    # Des id vont être automatiquement créés pour les auteurs
    db.session.commit()

    #Création des livres
    for b in star:
        a = stars[1] #b["starId"]
        diva = Star(nom = b["LastName"],
                    prenom = b["Name"],
                    dateNaiss = b["DateNaiss"],
                    img = b["img"],
                    userId = b["idUser"])
    #On ajoute l'objet o à la base
        db.session.add(diva)
    db.session.commit()