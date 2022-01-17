DROP TABLE IF EXISTS Star;
DROP TABLE IF EXISTS Utilisateurs;

create table Star (
	id INTEGER PRIMARY KEY AUTOINCREMENT, 
	nom varchar(20),
	prenom varchar(20),
	dateNaiss date,
	img varchar(20),
	idUser INTEGER,
	FOREIGN KEY(idUser) references Utilisateurs(userId) 
);

CREATE TABLE Utilisateurs (
	userId INTEGER PRIMARY KEY AUTOINCREMENT,
	userName varchar(30),
	userLastName varchar(30),
	userMail varchar(30),
	userPassword varchar(20)
);

INSERT INTO STAR(nom, prenom, dateNaiss, img, idUser) VALUES
	("Blu", "Jewelz", "21-09-1994", "jewelzBlu.jpg", 2),
	("Knight", "Nathalie", "17-05-2000", "nathalieKnight.jpg", 2),
	("Love", "Brandi", "29-03-1973", "brandiLove.jpg", 3),
	("Danger", "Abella", "19-11-1995", "abellaDanger.jpg", 3),
	("Khalifa", "Mia", "10-02-1993", "miaKhalifa.jpg", 3),
	("Reid", "Riley", "09-07-1991", "rileyReid.jpg", 2);

INSERT INTO Utilisateurs(userName, userLastName, userMail, userPassword) VALUES
	("admin", "admin", "admin", "admin"),
	("Sevot", "Maxime", "max.sevot@gmail.com", "azerty"),
	("Bettini", "Jeremy", "jeremy.bettini@gmail.com", "azerty");