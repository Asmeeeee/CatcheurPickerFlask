Pour lancer le Flask

Si virtualenv instrallé comme sur les pc de l'IUT
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirement.txt

sinon :

$ pip install -r requirement.txt

Puis aller dans le fichier courant et taper
$ flask run 

Le fichier Flask correspond au déroulement de tous les tp, des backup sont disponible au travers des fichiers dans le dossier parents

Code Mocodo
Utilisateur: _userName, userPassword
Aime, 1N Favoris, 0N Utilisateur
Favoris: _id

Possede, 0N Utilisateur, 11 Star
Star: _starId, starName, starLastName, starOrigin, starHairColor, starHeight, starWeight
Appartenir,1N Favoris, 0N Star
