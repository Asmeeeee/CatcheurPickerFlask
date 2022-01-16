DROP TABLE IF EXISTS Star;

create table Star (
	id INTEGER PRIMARY KEY AUTOINCREMENT, 
	nom varchar(20),
	prenom varchar(20),
	dateNaiss date,
	img varchar(20)
	);

INSERT INTO STAR(nom, prenom, dateNaiss, img) VALUES
	("Blu", "Jewelz", "21-09-1994", "jewelzBlu.jpg"),
	("Knight", "Nathalie", "17-05-2000", "nathalieKnight.jpg"),
	("Love", "Brandi", "29-03-1973", "brandiLove.jpg"),
	("Danger", "Abella", "19-11-1995", "abellaDanger.jpg"),
	("Khalifa", "Mia", "10-02-1993", "miaKhalifa.jpg"),
	("Reid", "Riley", "09-07-1991", "rileyReid.jpg");