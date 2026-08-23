USE LigueFootball
--- Exercice 1: Importation des équipes
INSERT INTO equipes
VALUES ('AS Poto-Poto', 'Poto-Poto', 'Jean Malonga', 2010),
('FC Bacongo', 'Bacongo', 'Pierre Nzaou', 2008),
('Etoile de Moungali', 'Moungali', 'Serge Loubaki', 2015),
('Ouenze United', 'Ouenzé', 'Alain Mabiala', 2012),
('Talangaï FC', 'Talangaï', 'Bruno Ngouabi', 2009),
('Makélékélé Sport', 'Makélékélé', 'Rufin Massamba', 2009),
('AS Mfilou', 'Mfilou', 'Claude Ondongo', 2013),
('Djiri Football Club', 'Djiri', 'Fabrice Kimbembe', 2014);

--- Exercice 2: insertion des stades et des joueurs
--- a: insertion des stades
INSERT INTO stades
VALUES ('Stade Massambadeba', 'Makélékélé', 10000),
('Stade Ornano', 'Poto-Poto', 5000),
('Stade de la concorde', 'Djiri', 150000);

--- b: insertion des joueurs (3 joueurs par équipe)
INSERT INTO joueurs (nom, prenom, equipe_id, poste, numero_maillot, date_naissance)
VALUES(
'Ongouya', 'Elie', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'AS Poto-Poto'), 'Attaquant', 8, '2004-01-02'),
('Elenga','Précieux', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'AS Poto-Poto'), 'Gardien', 1, '2003-05-13'),
('Mahoungou', 'Richard', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'AS Poto-Poto'), 'Défenseur', 5, '2004-05-18'),

('Ngoma', 'Jemima', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'FC Bacongo'), 'Gardien', 1, '2002-08-25'),
('Mpele', 'Jean', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'FC Bacongo'), 'Défenseur', 4, '1999-11-16'),
('Aboma', 'Béni', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'FC Bacongo'), 'Milieu', 16, '2001-06-23'),

('Ngoulou', 'Marco', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Etoile de Moungali'), 'Gardien', 16, '2001-10-12'),
('Ngolo', 'Bonheur', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Etoile de Moungali'), 'Milieu', 12, '2000-12-10'),
('Mpion', 'Jule', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Etoile de Moungali'), 'Attaquant', 20, '2000-02-15'),

('Tsiba', 'Luc', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Ouenze United'), 'Gardien', 1, '1999-11-25'),
('Goma', 'Paul',(SELECT equipe_id FROM equipes WHERE nom_equipe = 'Ouenze United'), 'Défenseur', 5, '1998-08-07'),
('Ndila', 'Samuel', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Ouenze United'), 'Milieu', 6, '2000-09-14'),

('Tika', 'Pierre', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Talangaï FC'), 'Gardien', 20, '2000-12-17'),
('Elenga', 'Benoit',(SELECT equipe_id FROM equipes WHERE nom_equipe = 'Talangaï FC'), 'Milieu', 10, '2001-11-28'),
('Bikouma', 'Gad', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Talangaï FC'), 'Attaquant', 11, '2002-05-17'),

('Kiba', 'Gaston', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Makélékélé Sport'), 'Gardien', 1, '2002-12-23'),
('Tila', 'Igor', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Makélékélé Sport'), 'Défenseur', 4, '2003-06-18'),
('Ekouya', 'Boris', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Makélékélé Sport'), 'Milieu', 6, '2002-05-26'),

('Ndinga', 'Amour', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'AS Mfilou'), 'Gardien', 32, '2002-10-19'),
('Kaya', 'Alex', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'AS Mfilou'), 'Défenseur', 5, '2000-05-14'),
('Mbongo', 'Sagesse', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'AS Mfilou'), 'Attaquant', 12, '2003-11-28'),

('Kolela', 'Evans', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Djiri Football Club'), 'Gardien', 1, '2004-08-28'),
('Tendart', 'Van', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Djiri Football Club'), 'Défenseur', 6, '2003-11-01'),
('Nkoua', 'Emmanuel', (SELECT equipe_id FROM equipes WHERE nom_equipe = 'Djiri Football Club'), 'Milieu', 8, '2003-09-12');

--- Exercice 3: insertion des matchs
INSERT INTO matchs (equipe_domicile_id, equipe_exterieur_id, stade_id, date_match)
VALUES (
(SELECT equipe_id FROM equipes WHERE nom_equipe = 'AS Poto-Poto'),
(SELECT equipe_id FROM equipes WHERE nom_equipe = 'FC Bacongo'), 
(SELECT stade_id FROM stades WHERE nom_stade = 'Stade Massambadeba'), '2026-10-07'),
(
(SELECT equipe_id FROM equipes WHERE nom_equipe = 'Etoile de Moungali'),
(SELECT equipe_id FROM equipes WHERE nom_equipe = 'Ouenze United'),
(SELECT stade_id FROM stades WHERE nom_stade = 'Stade Ornano'),
'2026-10-10'),
(
(SELECT equipe_id FROM equipes WHERE nom_equipe = 'Talangaï FC'),
(SELECT equipe_id FROM equipes WHERE nom_equipe = 'Makélékélé Sport'),
(SELECT stade_id FROM stades WHERE nom_stade = 'Stade Massambadeba'),
'2026-10-11'),
(
(SELECT equipe_id FROM equipes WHERE nom_equipe = 'Djiri Football Club'),
(SELECT equipe_id FROM equipes WHERE nom_equipe = 'AS Mfilou'),
(SELECT stade_id FROM stades WHERE nom_stade = 'Stade de la concorde'),
'2026-10-13');

--- Exercice 4: enregistrement des résultats
--- a: Mise à jour des scores
UPDATE matchs
SET equipe_domicile_id = 2,
	equipe_exterieur_id = 1
WHERE match_id = 1;

UPDATE matchs
SET equipe_domicile_id = 3,
	equipe_exterieur_id = 1
WHERE match_id = 2

UPDATE matchs 
SET equipe_domicile_id = 1,
	equipe_exterieur_id = 1
WHERE match_id = 3

UPDATE matchs 
SET equipe_domicile_id = 2,
	equipe_exterieur_id = 1
WHERE match_id = 4

--- b: correction du stade
UPDATE matchs
SET stade_id = (SELECT stade_id FROM stades WHERE nom_stade = 'Stade Ornano')
WHERE date_match = '2026-10-11';

--- Exercice 5: enregistrement des butteurs
INSERT INTO buts (match_id, joueur_id, minute)
Values(
--- match1
(SELECT match_id FROM matchs WHERE date_match = '2026-10-07'),
(SELECT joueur_id FROM joueurs WHERE date_naissance = '2004-01-02'), 10),
(
(SELECT match_id FROM matchs WHERE date_match = '2026-10-07'),
(SELECT joueur_id FROM joueurs WHERE date_naissance = '2002-08-25'), 60),
(
(SELECT match_id FROM matchs WHERE date_match = '2026-10-07'),
(SELECT joueur_id FROM joueurs WHERE date_naissance = '2004-01-02'), 85),
--- match 2
(
(SELECT match_id FROM matchs WHERE date_match = '2026-10-10'),
(SELECT joueur_id FROM joueurs WHERE date_naissance = '2000-12-10'),15),
(
(SELECT match_id FROM matchs WHERE date_match = '2026-10-10'),
(SELECT joueur_id FROM joueurs WHERE date_naissance = '2000-02-15'), 40),
(
(SELECT match_id FROM matchs WHERE date_match = '2026-10-10'),
(SELECT joueur_id FROM joueurs WHERE date_naissance = '1998-08-07'), 60),
(
(SELECT match_id FROM matchs WHERE date_match = '2026-10-10'),
(SELECT joueur_id FROM joueurs WHERE date_naissance = '2000-02-15'),85),
--- match 3
(
(SELECT match_id FROM matchs WHERE date_match = '2026-10-11'),
(SELECT joueur_id FROM joueurs WHERE date_naissance = '2002-05-17'), 45),
(
(SELECT match_id FROM matchs WHERE date_match = '2026-10-11'),
(SELECT joueur_id FROM joueurs WHERE date_naissance = '2002-05-26'), 60),
--- match 4
(
(SELECT match_id FROM matchs WHERE date_match = '2026-10-13'),
(SELECT joueur_id FROM joueurs WHERE date_naissance ='2003-09-12'),53),
(
(SELECT match_id FROM matchs WHERE date_match = '2026-10-13'),
(SELECT joueur_id FROM joueurs WHERE date_naissance = '2003-11-28'), 77),
(
(SELECT match_id FROM matchs WHERE date_match = '2026-10-13'),
(SELECT joueur_id FROM joueurs WHERE date_naissance = '2003-11-01'), 86);

--- Exercice 6: suppresion des doublons
SELECT * FROM joueurs 
DELETE FROM joueurs 
WHERE joueur_id = 29

--- Exercice 7:
--- a: nombre d'équipe enregistré
SELECT COUNT(*) AS Nb_equipe
FROM equipes 

--- b: nombre de joueurs 
SELECT COUNT(*) AS Nb_joueur
FROM joueurs
--- nombre de joueurs par équipe
SELECT equipe_id,
COUNT(joueur_id) AS Nb_joueur_equipe
FROM joueurs 
GROUP BY equipe_id 

--- c: nombre de but marqué sur la journée
SELECT match_id,
COUNT(but_id) AS Nb_but_jour
FROM buts 
GROUP BY match_id 

--- Exercice 8: 
--- attaquants
SELECT COUNT(*) AS Nb_attaquant 
FROM joueurs
WHERE poste = 'Attaquant'; 

--- match à plus de 3 buts
SELECT COUNT(*) AS buts_3
FROM matchs
WHERE (score_domicile + score_exterieur >3) 

--- Nombre de joueurs par équipe
SELECT equipe_id,
COUNT(joueur_id) AS Nb_joueur_equipe
FROM joueurs 
GROUP BY equipe_id
ORDER BY Nb_joueur_equipe ASC 

--- score par match du plus grand au plus petit
SELECT match_id,
COUNT(but_id) AS Nb_but_jour
FROM buts 
GROUP BY match_id 
ORDER BY Nb_but_jour DESC