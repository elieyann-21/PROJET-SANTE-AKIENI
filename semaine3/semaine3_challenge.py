# ==========================================================================================
# AKIENI ACADEMY - Projet santé publique
# Semaine 3 - Rapport d'état sanitaire départemental
# Nom : ONGOUYA Elie Yann
# Date : 26 juin 2026
# ==========================================================================================

# === VARIABLES DES 5 HOPITAUX ===
# Hopital 1 - CHU de Brazzaville
h1_nom = 'CHU de Brazzaville'
h1_ville = 'Brazzaville'
h1_departement = 'Brazzaville'
h1_type = 'CHU'
h1_nb_lits          = 320
h1_nb_lits_occupes  = 298 
h1_nb_medecins      = 47 
h1_nb_rupute = 2 
h1_nb_alerte = 2

# hopital 2 - Hopital général de Pointe-Noire
h2_nom = 'Hôpital général de Pointe-Noire'
h2_ville = 'Pointe-Noire'
h2_departement = 'Pointe-Noire'
h2_type = ' HG'
h2_nb_lits          = 180
h2_nb_lits_occupes  = 143
h2_nb_medecins      = 22
h2_nb_rupute = 0
h2_nb_alerte = 1

# Hopital 3 - Hopital général de dolisie
h3_nom = 'Hôpital général de Dolisie'
h3_ville = 'Dolisie'
h3_departement = 'Niari'
h3_type = ' HG'
h3_nb_lits          = 95 
h3_nb_lits_occupes  = 91 
h3_nb_medecins      = 8
h3_nb_rupute = 1
h3_nb_alerte = 2

# Hopital 4 - Hopital de district de Owando
h4_nom = 'Hôpital de référence de Owando'
h4_ville = 'Owando'
h4_departement = 'Cuvette'
h4_type = ' HRD'
h4_nb_lits          = 45 
h4_nb_lits_occupes  = 32
h4_nb_medecins      = 3 
h4_nb_rupute = 3
h4_nb_alerte = 0

# Hopital 5 - Centre de santé de Impfondo
h5_nom = 'CS de Impfondo'
h5_ville = 'Impfondo'
h5_departement = 'Likouala'
h5_type = ' CS'
h5_nb_lits          = 20 
h5_nb_lits_occupes  = 19 
h5_nb_medecins      = 1
h5_nb_alerte = 1
h5_nb_rupute = 2

# === CALCUL DES INDICATEURS ===
# CHU
h1_taux_occupation = round((h1_nb_lits_occupes/h1_nb_lits)*100,2)
# Niveau triage occupation
if h1_taux_occupation < 60:
    h1_niveau_occupation = 'CRITIQUE'
elif h1_taux_occupation >= 60 and h1_taux_occupation < 85:
    h1_niveau_occupation = 'OPTIMAL'
elif h1_taux_occupation >= 85 and h1_taux_occupation < 90:
    h1_niveau_occupation = 'CRITIQUE'
else:
    h1_niveau_occupation = 'RISQUE ENGORGEMENT'
# Niveau d'alerte globale
if h1_nb_rupute >= 2 or h1_taux_occupation > 95:
    h1_niveau_alerte_globale = "CRITIQUE"
elif h1_nb_rupute >= 1 or h1_taux_occupation > 85 or (h1_nb_alerte > 2 and h1_nb_medecins < 5):
    h1_niveau_alerte_globale = "PREOCUPANT"
else:
    h1_niveau_alerte_globale = "SATISFAISANT"

# Hôpital de Pointe Noire
h2_taux_occupation = round((h2_nb_lits_occupes/h2_nb_lits)*100,2)
# Niveau triage occupation
if h2_taux_occupation < 60:
    h2_niveau_occupation = 'CRITIQUE'
elif h2_taux_occupation >= 60 and h2_taux_occupation < 85:
    h2_niveau_occupation = 'OPTIMAL'
elif h2_taux_occupation >= 85 and h2_taux_occupation < 90:
    h2_niveau_occupation = 'CRITIQUE'
else:
    h2_niveau_occupation = 'RISQUE ENGORGEMENT'
# Niveau d'alerte globale
if h2_nb_rupute >= 2 or h2_taux_occupation > 95:
    h2_niveau_alerte_globale = "CRITIQUE"
elif h2_nb_rupute >= 1 or h2_taux_occupation > 85 or (h2_nb_alerte > 2 and h2_nb_medecins < 5):
    h2_niveau_alerte_globale = "PREOCUPANT"
else:
    h2_niveau_alerte_globale = "SATISFAISANT"

# Hôpital de dolisie
h3_taux_occupation = round((h3_nb_lits_occupes/h3_nb_lits)*100,2)
# Niveau triage occupation
if h3_taux_occupation < 60:
    h3_niveau_occupation = 'CRITIQUE'
elif h3_taux_occupation >= 60 and h3_taux_occupation < 85:
    h3_niveau_occupation = 'OPTIMAL'
elif h3_taux_occupation >= 85 and h3_taux_occupation < 90:
    h3_niveau_occupation = 'CRITIQUE'
else:
    h3_niveau_occupation = 'RISQUE ENGORGEMENT'
# Niveau d'alerte globale
if h3_nb_rupute >= 2 or h3_taux_occupation > 95:
    h3_niveau_alerte_globale = "CRITIQUE"
elif h3_nb_rupute >= 1 or h3_taux_occupation > 85 or (h3_nb_alerte > 2 and h3_nb_medecins < 5):
    h3_niveau_alerte_globale = "PREOCUPANT"
else:
    h3_niveau_alerte_globale = "SATISFAISANT"

# Hôpital d'Owando
h4_taux_occupation = round((h4_nb_lits_occupes/h4_nb_lits)*100,2)
# Niveau triage occupation
if h4_taux_occupation < 60:
    h4_niveau_occupation = 'CRITIQUE'
elif h4_taux_occupation >= 60 and h4_taux_occupation < 85:
    h4_niveau_occupation = 'OPTIMAL'
elif h4_taux_occupation >= 85 and h4_taux_occupation < 90:
    h4_niveau_occupation = 'CRITIQUE'
else:
    h4_niveau_occupation = 'RISQUE ENGORGEMENT'
# Niveau d'alerte globale
if h4_nb_rupute >= 2 or h4_taux_occupation > 95:
    h4_niveau_alerte_globale = "CRITIQUE"
elif h4_nb_rupute >= 1 or h4_taux_occupation > 85 or (h4_nb_alerte > 2 and h4_nb_medecins < 5):
    h4_niveau_alerte_globale = "PREOCUPANT"
else:
    h4_niveau_alerte_globale = "SATISFAISANT"

# CMS de Impfondo
h5_taux_occupation = round((h5_nb_lits_occupes/h5_nb_lits)*100,2)
# Niveau triage occupation
if h5_taux_occupation < 60:
    h5_niveau_occupation = 'CRITIQUE'
elif h5_taux_occupation >= 60 and h5_taux_occupation < 85:
    h5_niveau_occupation = 'OPTIMAL'
elif h5_taux_occupation >= 85 and h5_taux_occupation < 90:
    h5_niveau_occupation = 'CRITIQUE'
else:
    h5_niveau_occupation = 'RISQUE ENGORGEMENT'
# Niveau d'alerte globale
if h5_nb_rupute >= 2 or h2_taux_occupation > 95:
    h5_niveau_alerte_globale = "CRITIQUE"
elif h5_nb_rupute >= 1 or h5_taux_occupation > 85 or (h5_nb_alerte > 2 and h5_nb_medecins < 5):
    h5_niveau_alerte_globale = "PREOCUPANT"
else:
    h5_niveau_alerte_globale = "SATISFAISANT"


# === Rupture de stock à l'échelle nationale ===
nb_total_rupture = h1_nb_rupute+h2_nb_rupute+h3_nb_rupute+h4_nb_rupute+h5_nb_rupute
cout_commande_urgente = nb_total_rupture*int(450_000)

# === Tableau de bord ===
print("="*70)
print(f""" MINISTERE DE LA SANTE - TABLEAU DE BORD SANITAIRE
    Date : 26/06/2026""")
print("="*70)
print(f"""{h1_nom}
    Occupation : {h1_taux_occupation} [{h1_niveau_occupation}]
    Alerte : {h1_nb_rupute}R + {h1_nb_alerte}A
    Niveau global : {h1_niveau_alerte_globale}""")
print(f"""{h2_nom}
    Occupation : {h2_taux_occupation} [{h2_niveau_occupation}]
    Alerte : {h2_nb_rupute}R + {h2_nb_alerte}A
    Niveau global : {h2_niveau_alerte_globale}""")
print(f"""{h3_nom}
    Occupation : {h3_taux_occupation} [{h3_niveau_occupation}]
    Alerte : {h3_nb_rupute}R + {h3_nb_alerte}A
    Niveau global : {h3_niveau_alerte_globale}""")
print(f"""{h4_nom}
    Occupation : {h4_taux_occupation} [{h4_niveau_occupation}]
    Alerte : {h4_nb_rupute}R + {h4_nb_alerte}A
    Niveau global : {h4_niveau_alerte_globale}""")
print(f"""{h5_nom}
    Occupation : {h5_taux_occupation} [{h5_niveau_occupation}]
    Alerte : {h5_nb_rupute}R + {h5_nb_alerte}A
    Niveau global : {h5_niveau_alerte_globale}""")
print("-"*70)
input("Commentaire :")
input("Recommandation prioritaire:")
print("="*70) 