import click
from .app import app, db
from .models import Author, Book

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
    books = yaml.load(open(filename), Loader=yaml.FullLoader)

    # Premier passage : lecture et création des auteurs
    authors = dict()
    for b in books:
        a = b["author"]
        if a not in authors:
            nouveau = Author(name=a)
            # On ajoute l'obj nouveau à la base
            db.session.add(nouveau)
            authors[a] = nouveau
    # On dit à la bd d'intégrer toutes les nouvelles données
    # Des id vont être automatiquement créés pour les auteurs
    db.session.commit()

    #Création des livres
    for b in books:
        a = authors[b["author"]]
        book = Book(price = b["price"],
                    title = b["title"],
                    url   = b["url"],
                    img   = b["img"],
                    author_id = a.id)
    #On ajoute l'objet o à la base
        db.session.add(book)
    db.session.commit()