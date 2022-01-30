
Copyright © 2021 SEVOT Maxime et BETTINI Jérémy étudiants à l'IUT d'Orléans au département informatique
Toutes utilisations à des fins lucratives de cette application peut-etre sanctionné selon Art 514-5 du Code pénale
Sous la juridiction de M.ROZSAVOLGYI

# ======================================================================== #

  # ------------------------------------------ #
    Voici notre site Flask remplit de 
        de bonnes intentions
  # ------------------------------------------ #


# ======================================================================== #

Pour installer : 
1) $ git clone https://gitlab.com/maxime.sevot/projet-flask.git

2) Pour lancer le Flask

Si virtualenv instrallé comme sur les pc de l'IUT
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirement.txt

sinon :

$ pip install -r requirement.txt

3) Dans le répertoire courant : $ flask run (--host=0.0.0.0) (vérifiez bien d'avoir les packages pip, dans le cas contraire référez vous à l'étape 1)
4) Dans votre navigateur préféré : localhost:5000

Vous pouvez naviguer et profiter du site

# ======================================================================= #

Bienvenu sur Catcheur Picker 

Si vous venez d'arriver, le fichier tuto.db fonctionne, mais n'arrivant pas à le mettre dans le gitignore, vous l'aurez après avoir cloner le projet
Si vous voulez une bd propre avec un jeu d'essaie : 
	Supprimez tuto.db
	Dans le même répertoire (courant) lancez : $ flask loaddb ./tuto/catcheuse.yml --> cela vous créera une nouvelle bd.
	2 utilisateurs seront créer : maxime et jeremy et n'auront pas de mot de passe : pour leur en donner ou changer 
		$ flask passwd <user> <nouveau mdp>
	Pour créer un utilisateur : 
		$ flask newuser <nomUser> <password>
		ou bien aller sur localhost:5000 et procédez à la création d'un compte

Voila vous avez un compte
Sur ce site vous pouvez consulter la liste de tout les catcheurs de la base de donnée ou bien consulter uniquement les catcheurs que vous avez créer (grâce aux bouttons plus haut)
	Des filtres sont disponible (uniquement pour vos catcheurs)
	Trie par :
		Poids (croissant)
		Taille (croissante)
		Nationnalité (en fonction du paramètre)
		Couleur de cheuveux (en fonctione du paramètre)
		Barre de recherche (Supporte le nom et le prénom)
Pour ajouter un catcheur : appuyer sur le boutton et remplissez les champs (attention tous les champs nécessitant du texte sont obligatoire) (le format est préinscrit dans les champs) (en l'absence de photo une par défault est mise)
	Pour ajouter une photo : NOUVEAU vous pouvez prendre n'importe quelle photo de votre appareil, celle ci sera automatiquement importé dans le repertoire d'image du projet (Erreur à l'IUT qui possède un proxy)
	Si l'envie vous prends, connectez vous au site via un smartphone ($ flask run --host=0.0.0.0  --> pour lancer sur le reseau) et vous pourrez directement prendre une photo avec votre appareil. Génial ça non ? 

Une fois votre catcheur créer vous pouvez le consulter soit en consultant l'intégralité des catcheurs, soir en consultant les votres. Vous verrez que sous vos catcheurs un bouton de modification est disponible 
	Vous pourrez modifier tous les champs et même l'image 
	Ou bien vous pouvez la supprimer en appuyant sur le bouton remove (action irréverssible)

Le bouton se battre est actuellement en cours de déploiement (il permettra d'accéder à un combat avec votre catcheur) pour le moment il vous renvoie sur la page wikipédia, si elle existe
La fonctionnalité de favoris n'ayant pas réussis à être implémenter sera absente du projet pour le moment (le bouton est toujours disponible en revanche) (Dans l'idée, un catcheurs pourra appartenir au favoris de 0_N utilisateurs et un utilisateur pourra ajouté 0_N catcheur en favoris)

Enfin, tous les utilisateurs du site peuvent consulter les catcheurs ajouté dans la bd, mais ne pourront pas les modifiés


SUPER UTILISATEUR : Créer un utilisateur admin (soit par la commande soit par le formulaire) vous permet d'accéder et modifier l'intégralité des catcheurs.

# ======================================================================= #

Merci et amusez vous bien !
