--- Exercice 1: création de la base de données
CREATE DATABASE LigueFootball;

--- Exercice 2: création des tables racines
 USE LigueFootball; 
 CREATE TABLE equipes(equipe_id INT PRIMARY KEY IDENTITY(1,1),
 nom_equipe VARCHAR(50) NOT NULL,
 quartier VARCHAR(50) NOT NULL,
 entraineur VARCHAR(50) NOT NULL,
 annee_creation INT);

 CREATE TABLE stades(stade_id INT PRIMARY KEY IDENTITY(1,1),
 nom_stade VARCHAR(50) NOT NULL,
 quartier VARCHAR(50),
 capacite INT);

 --- Exercice 3: création des tables dépendantes
 CREATE TABLE joueurs(joueur_id INT PRIMARY KEY IDENTITY(1,1),
 nom VARCHAR(50) NOT NULL,
 prenom VARCHAR(50) NOT NULL,
 equipe_id INT, FOREIGN KEY (equipe_id) REFERENCES equipes(equipe_id),
 poste VARCHAR(20) NOT NULL,
 numero_maillot INT,
 date_naissance DATE);

 CREATE TABLE matchs(match_id INT PRIMARY KEY IDENTITY(1,1),
 equipe_domicile_id INT, FOREIGN KEY (equipe_domicile_id) REFERENCES equipes(equipe_id),
 equipe_exterieur_id INT, FOREIGN KEY (equipe_exterieur_id) REFERENCES equipes(equipe_id),
 stade_id INT, FOREIGN KEY(stade_id) REFERENCES stades(stade_id),
 date_match DATE NOT NULL,
 score_domicile INT DEFAULT 0,
 score_exterieur INT DEFAULT 0);

 CREATE TABLE buts(but_id INT PRIMARY KEY IDENTITY(1,1),
 match_id INT FOREIGN KEY REFERENCES matchs(match_id),
 joueur_id INT FOREIGN KEY REFERENCES joueurs(joueur_id),
 minute INT,);

 --- Exercice 4: ajout des contraintes
 ALTER TABLE joueurs
 ADD CONSTRAINT poste
 CHECK (poste IN ('Gardien', 'Défenseur', 'Milieu', 'Attaquant'));

 --- Exercice 5: ajout colonne calcul
 ALTER TABLE matchs
 ADD diff_buts AS(score_domicile - score_exterieur);

 --- Exercice 6: modification de la structure des données
 ALTER TABLE joueurs
 ADD capitaine BIT DEFAULT 0,
 telephone VARCHAR(20);

 --- Exercice 7: Renommer et supprimer
 --- a: création de la table temporaire
 CREATE TABLE test_saison(id INT, nom CHAR(10), prenom CHAR(10));
 --- b: renommination 
 EXEC sp_rename "test_saison", "test_saison_v2"; 
 --- c: suppression
 DROP TABLE test_saison_v2; 

 --- Exercice 8: création d'un index et vérification
 --- a: création de l'index
 CREATE NONCLUSTERED INDEX IX_date_match
 ON matchs(date_match);
 --- b: vérification 
SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE, IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_CATALOG = 'LigueFootball'
ORDER BY TABLE_NAME, ORDINAL_POSITION;




