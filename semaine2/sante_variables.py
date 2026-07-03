# =======================================================================
# MODULE FONDATEUR - Projet santé publique / AKIENI ACADEMY
# Ce fichier centralise toutes les constantes et variables métier, il sera 
# enrichi chaque semaine jusqu'à S24
# ========================================================================


# === SECTION A : CONSTANTES NATIONALES ET NORMES OMS ===
TAUX_EUR_FCFA = 655.957 
TAUX_USD_FCFA = 600.0 
SEUIL_OMS_DENSITE_MEDICALE = 2.3    # medecins pour 1000 habitants 
SEUIL_OMS_COUVERTURE_VACCIN = 95.0  # pourcentage minimum OMS 
SEUIL_MORTALITE_ALERTE = 2.0        # % deces / hospitalisations 
SEUIL_RUPTURE_STOCK_JOURS = 30      # jours minimum de stock 
Departements_CONGO = [ 'Brazzaville', 'Pointe-Noire', 'Bouenza', 'Cuvette', 'Cuvette-ouest'
     'Kouilou', 'Lekoumou', 'Likouala', 'Niari', 'Plateaux', 'Pool', 'Sangha']


# === SECTION B : VARIABLES DES 5 HOPITAUX ===
# Hopital 1 - CHU de Brazzaville
h1_nom = 'CHU de Brazzaville'
h1_ville = 'Brazzaville'
h1_departement = 'Brazzaville'
h1_type = 'CHU'
h1_nb_lits          = 320 
h1_nb_lits_occupes  = 284 
h1_nb_medecins      = 47 
h1_nb_infirmiers    = 123 
h1_population_zone  = 1_800_000

# hopital 2 - Hopital général de Pointe-Noire
h2_nom = 'HG de Pointe-Noire'
h2_ville = 'Pointe-Noire'
h2_departement = 'Pointe-Noire'
h2_type = ' HG'
h2_nb_lits          = 210 
h2_nb_lits_occupes  = 195
h2_nb_medecins      = 32
h2_nb_infirmiers    = 110 
h2_population_zone  = 1_500_000

# Hopital 3 - Hopital général de dolisie
h3_nom = 'HG de Dolisie'
h3_ville = 'Dolisie'
h3_departement = 'Niari'
h3_type = ' HG'
h3_nb_lits          = 180 
h3_nb_lits_occupes  = 160 
h3_nb_medecins      = 29
h3_nb_infirmiers    = 105 
h3_population_zone  = 900_000

# Hopital 4 - Hopital de district de Owando
h4_nom = 'HRD de Owando'
h4_ville = 'Owando'
h4_departement = 'Cuvette'
h4_type = ' HRD'
h4_nb_lits          = 110 
h4_nb_lits_occupes  = 88 
h4_nb_medecins      = 18 
h4_nb_infirmiers    = 95 
h4_population_zone  = 300_000

# Hopital 5 - Centre de santé de Impfondo
h5_nom = 'CS de Impfondo'
h5_ville = 'Impfondo'
h5_departement = 'Likouala'
h5_type = ' CS'
h5_nb_lits          = 10 
h5_nb_lits_occupes  = 6 
h5_nb_medecins      = 3 
h5_nb_infirmiers    = 15 
h5_population_zone  = 5_000


# === SECTION C : VARIABLES DES 5 MEDICAMENTS ===
# Médicament 1 - artemether-lumefantrine
m1_nom = 'artemether-lumefantrine'
m1_stock = 250
m1_seuil_rupture = 30
m1_cout_unitaire = 1000 # en franc CFA
m1_valeur_stock = m1_stock*m1_cout_unitaire # j'ai rajouté cette variable ici pour facilité le calcul de la valeur en stock

# Médicament 2 - amoxicilline
m2_nom = 'amoxicilline'
m2_stock = 500
m2_seuil_rupture = 50
m2_cout_unitaire = 500
m2_valeur_stock = m2_stock*m2_cout_unitaire


# Médicaments 3 - paracetamol
m3_nom = 'paracetamol'
m3_stock = 1200
m3_seuil_rupture = 100
m3_cout_unitaire = 200
m3_valeur_stock = m3_stock*m3_cout_unitaire


# Médicament 4 - SRO
m4_nom = 'SRO'
m4_stock = 100
m4_seuil_rupture = 25
m4_cout_unitaire = 200
m4_valeur_stock = m4_stock*m4_cout_unitaire


# Médicaments 5 - vaccin antipaludeen
m5_nom = 'vaccin antipaludeen'
m5_stock = 800 # en nombre de dose
m5_seuil_rupture = 50
m5_cout_unitaire = 0 # le vaccin est gratuit
m5_valeur_stock = m5_stock*m5_cout_unitaire


# === SECTION D : CALCULS D'INITIALISATION
nb_total_medecins = h1_nb_medecins+h2_nb_lits_occupes+h3_nb_medecins+h4_nb_medecins+h5_nb_medecins
pop_generale = h1_population_zone+h2_population_zone+h3_population_zone+h4_population_zone+h5_population_zone
densite_medicale_nationale = round((nb_total_medecins/int(pop_generale))*100,2)
# calcul intermédiaire pour le calcul du taux moyen d'occupation
nb_total_lits = h1_nb_lits+h2_nb_lits+h3_nb_lits+h4_nb_lits+h5_nb_lits  # Nombre total de lits
nb_total_lits_occupes = h1_nb_lits_occupes+h2_nb_lits_occupes+h3_nb_lits_occupes+h4_nb_lits_occupes+h5_nb_lits_occupes
taux_moyen_occupation = round((nb_total_lits_occupes/nb_total_lits)*100,2)

valeur_total_stock = m1_valeur_stock+m2_valeur_stock+m3_valeur_stock+m4_valeur_stock+m5_valeur_stock


# === SECTION E : RAPPORT D'INVENTAIRE ===
print("="*70)
print("RAPPORT INITIAL DU SYSTEME DE SANTE")
print("="*70)
print(f"""I- Situation des hôpitaux
     1- Hopital 1
          Nom de l'hopital : {h1_nom}
          Ville : {h1_ville}
          Département : {h1_departement}
          Nombre de lits : {nb_total_lits}
          Nombre de lits occupés : {h1_nb_lits_occupes}
          Nombre de médecins : {h1_nb_medecins}
          Nombre d'infirmiers : {h1_nb_infirmiers}
          Populations desservies : {h1_population_zone} habitants""")
print(f"""2- Hopital 2
          Nom de l'hopital : {h2_nom}
          Ville : {h2_ville}
          Département : {h2_departement}
          Nombre de lits : {nb_total_lits}
          Nombre de lits occupés : {h2_nb_lits_occupes}
          Nombre de médecins : {h2_nb_medecins}
          Nombre d'infirmiers : {h2_nb_infirmiers}
          Populations desservies : {h2_population_zone} habitants""")
print(f"""3- Hopital 3
          Nom de l'hopital : {h3_nom}
          Ville : {h3_ville}
          Département : {h3_departement}
          Nombre de lits : {nb_total_lits}
          Nombre de lits occupés : {h3_nb_lits_occupes}
          Nombre de médecins : {h3_nb_medecins}
          Nombre d'infirmiers : {h3_nb_infirmiers}
          Populations desservies : {h3_population_zone} habitants""")
print(f"""4- Hopital 4
          Nom de l'hopital : {h4_nom}
          Ville : {h4_ville}
          Département : {h4_departement}
          Nombre de lits : {nb_total_lits}
          Nombre de lits occupés : {h4_nb_lits_occupes}
          Nombre de médecins : {h4_nb_medecins}
          Nombre d'infirmiers : {h4_nb_infirmiers}
          Populations desservies : {h4_population_zone} habitants""")
print(f"""5- Hopital 5
          Nom de l'hopital : {h5_nom}
          Ville : {h5_ville}
          Département : {h5_departement}
          Nombre de lits : {nb_total_lits}
          Nombre de lits occupés : {h5_nb_lits_occupes}
          Nombre de médecins : {h5_nb_medecins}
          Nombre d'infirmiers : {h5_nb_infirmiers}
          Populations desservies : {h5_population_zone} habitants""")
print(f"II- Situation des médicaments")
print(f"""1- Médicament 1
     Nom : {m1_nom}
     Quantité en stock : {m1_stock}
     Stock seuil de rupture : {m1_seuil_rupture}
     Prix unitaire : {m1_cout_unitaire} franc CFA""")
print(f"""2- Médicament 2
     Nom : {m2_nom}
     Quantité en stock : {m2_stock}
     Stock seuil de rupture : {m2_seuil_rupture}
     Prix unitaire : {m2_cout_unitaire} franc CFA""")
print(f"""3- Médicament 3
     Nom : {m3_nom}
     Quantité en stock : {m3_stock}
     Stock seuil de rupture : {m3_seuil_rupture}
     Prix unitaire : {m3_cout_unitaire} franc CFA""")
print(f"""4- Médicament 4
     Nom : {m4_nom}
     Quantité en stock : {m4_stock}
     Stock seuil de rupture : {m4_seuil_rupture}
     Prix unitaire : {m4_cout_unitaire} franc CFA""")
print(f"""5- Médicament 5
     Nom : {m5_nom}
     Quantité en stock : {m5_stock}
     Stock seuil de rupture : {m5_seuil_rupture}
     Prix unitaire : {m5_cout_unitaire} franc CFA""")
print(f"""III- Indicateurs du systèle de santé
     Densité médicale nationale : {densite_medicale_nationale}/1000 habitants
     Taux moyen d'occupation des lits : {taux_moyen_occupation}%
     Valeur total du stock des médicaments : {valeur_total_stock} franc CFA""")


# === SECTION F : Classification automatique du statut de chacun des 5 medicaments 
# Médicament 1
if m1_stock <= m1_seuil_rupture:
    m1_statut  = 'RUPTURE CRITIQUE'
    m1_couleur = '[ROUGE]'
    m1_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m1_stock <= m1_seuil_rupture * 1.5:
    m1_statut  = 'ALERTE STOCK'
    m1_couleur = '[ORANGE]'
    m1_action  = 'Commande urgente a declencher sous 72h'
elif m1_stock <= m1_seuil_rupture * 2.0:
    m1_statut  = 'STOCK LIMITE'
    m1_couleur = '[Jaune]'
    m1_action  = 'Surveillance renforcee — planifier commande'
else:
    m1_statut  = 'STOCK NORMAL'
    m1_couleur = '[VERT]'
    m1_action  = 'Situation normale — suivi standard'

# Médicament 2
if m2_stock <= m2_seuil_rupture:
    m2_statut  = 'RUPTURE CRITIQUE'
    m2_couleur = '[ROUGE]'
    m2_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m2_stock <= m2_seuil_rupture * 1.5:
    m2_statut  = 'ALERTE STOCK'
    m2_couleur = '[ORANGE]'
    m2_action  = 'Commande urgente a declencher sous 72h'
elif m2_stock <= m2_seuil_rupture * 2.0:
    m2_statut  = 'STOCK LIMITE'
    m2_couleur = '[Jaune]'
    m2_action  = 'Surveillance renforcee — planifier commande'
else:
    m2_statut  = 'STOCK NORMAL'
    m2_couleur = '[VERT]'
    m2_action  = 'Situation normale — suivi standard'

# Médicaments 3
if m3_stock <= m3_seuil_rupture:
    m3_statut  = 'RUPTURE CRITIQUE'
    m3_couleur = '[ROUGE]'
    m3_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m3_stock <= m3_seuil_rupture * 1.5:
    m3_statut  = 'ALERTE STOCK'
    m3_couleur = '[ORANGE]'
    m3_action  = 'Commande urgente a declencher sous 72h'
elif m3_stock <= m3_seuil_rupture * 2.0:
    m3_statut  = 'STOCK LIMITE'
    m3_couleur = '[Jaune]'
    m3_action  = 'Surveillance renforcee — planifier commande'
else:
    m3_statut  = 'STOCK NORMAL'
    m3_couleur = '[VERT]'
    m3_action  = 'Situation normale — suivi standard'

# Médicament 4
if m4_stock <= m4_seuil_rupture:
    m4_statut  = 'RUPTURE CRITIQUE'
    m4_couleur = '[ROUGE]'
    m4_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m4_stock <= m4_seuil_rupture * 1.5:
    m4_statut  = 'ALERTE STOCK'
    m4_couleur = '[ORANGE]'
    m4_action  = 'Commande urgente a declencher sous 72h'
elif m4_stock <= m4_seuil_rupture * 2.0:
    m4_statut  = 'STOCK LIMITE'
    m4_couleur = '[Jaune]'
    m4_action  = 'Surveillance renforcee — planifier commande'
else:
    m4_statut  = 'STOCK NORMAL'
    m4_couleur = '[VERT]'
    m4_action  = 'Situation normale — suivi standard'

# Médicament 5
if m5_stock <= m5_seuil_rupture:
    m5_statut  = 'RUPTURE CRITIQUE'
    m5_couleur = '[ROUGE]'
    m5_action  = 'Alerte immediate PNA — commande express sous 24h'
elif m5_stock <= m5_seuil_rupture * 1.5:
    m5_statut  = 'ALERTE STOCK'
    m5_couleur = '[ORANGE]'
    m5_action  = 'Commande urgente a declencher sous 72h'
elif m5_stock <= m5_seuil_rupture * 2.0:
    m5_statut  = 'STOCK LIMITE'
    m5_couleur = '[Jaune]'
    m5_action  = 'Surveillance renforcee — planifier commande'
else:
    m5_statut  = 'STOCK NORMAL'
    m5_couleur = '[VERT]'
    m5_action  = 'Situation normale — suivi standard'

# Comptage des alertes
nb_ruptures_critiques = 0 
if m1_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques = nb_ruptures_critiques + 1
if m2_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques = nb_ruptures_critiques + 1
if m3_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques = nb_ruptures_critiques + 1
if m4_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques = nb_ruptures_critiques + 1
if m5_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques = nb_ruptures_critiques + 1

nb_alertes_stock = 0
if m1_statut == 'ALERTE STOCK': nb_alertes_stock = nb_alertes_stock + 1
if m2_statut == 'ALERTE STOCK': nb_alertes_stock = nb_alertes_stock + 1
if m3_statut == 'ALERTE STOCK': nb_alertes_stock = nb_alertes_stock + 1
if m4_statut == 'ALERTE STOCK': nb_alertes_stock = nb_alertes_stock + 1
if m5_statut == 'ALERTE STOCK': nb_alertes_stock = nb_alertes_stock + 1

nb_stock_limite = 0
if m1_statut == 'STOCK LIMITE': nb_stock_limite = nb_stock_limite + 1
if m2_statut == 'STOCK LIMITE': nb_stock_limite = nb_stock_limite + 1
if m3_statut == 'STOCK LIMITE': nb_stock_limite = nb_stock_limite + 1
if m4_statut == 'STOCK LIMITE': nb_stock_limite = nb_stock_limite + 1
if m5_statut == 'STOCK LIMITE': nb_stock_limite = nb_stock_limite + 1

nb_stock_normal = 0
if m1_statut == 'STOCK NORMAL': nb_stock_normal = nb_stock_normal + 1
if m2_statut == 'STOCK NORMAL': nb_stock_normal = nb_stock_normal + 1
if m3_statut == 'STOCK NORMAL': nb_stock_normal = nb_stock_normal + 1
if m4_statut == 'STOCK NORMAL': nb_stock_normal = nb_stock_normal + 1
if m5_statut == 'STOCK NORMAL': nb_stock_normal = nb_stock_normal + 1

# Méssage d'alerte
message_alerte = f""" Attention : 
- {nb_ruptures_critiques} médicaments en rupture critique !
- {nb_alertes_stock} médicaments en alerte de stock !
- {nb_stock_limite} médicaments en limite de stock !"""

# SECTION G : Classification du niveau d'occupation de chacun des 5 hopitaux
# CHU
h1_taux_occupation = round((h1_nb_lits_occupes/h1_nb_lits)*100,2)
if h1_taux_occupation < 60:
    h1_niveau_occupation = 'CRITIQUE'
elif h1_taux_occupation >= 60 and h1_taux_occupation < 85:
    h1_niveau_occupation = 'OPTIMAL'
elif h1_taux_occupation >= 85 and h1_taux_occupation < 90:
    h1_niveau_occupation = 'CRITIQUE'
else:
    h1_niveau_occupation = 'RISQUE ENGORGEMENT'
# Hôpital de Pointe Noire
h2_taux_occupation = round((h2_nb_lits_occupes/h2_nb_lits)*100,2)
if h2_taux_occupation < 60:
    h2_niveau_occupation = 'CRITIQUE'
elif h2_taux_occupation >= 60 and h2_taux_occupation < 85:
    h2_niveau_occupation = 'OPTIMAL'
elif h2_taux_occupation >= 85 and h2_taux_occupation < 90:
    h2_niveau_occupation = 'CRITIQUE'
else:
    h2_niveau_occupation = 'RISQUE ENGORGEMENT'
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


# SECTION H : Classification de la couverture vaccinale pour 4 departements
# Données
# Département 1
dep1_nom = 'Brazzaville'
dep1_pop_cible = 450_000
dep1_personnes_vaccines = 418_500
dep1_taux_attendu = 93.0 #%
dep1_couverture = round((int(dep1_personnes_vaccines)/int(dep1_pop_cible))*100,2)
# Département 2
dep2_nom = 'Pointe-Noire'
dep2_pop_cible = 280_000
dep2_personnes_vaccines = 229_600
dep2_taux_attendu = 82.0 #%
dep2_couverture = round((int(dep2_personnes_vaccines)/int(dep2_pop_cible))*100,2)
# Département 3
dep3_nom = 'Pool'
dep3_pop_cible = 120_000
dep3_personnes_vaccines = 54_500
dep3_taux_attendu = 45.0 #%
dep3_couverture = round((int(dep3_personnes_vaccines)/int(dep2_pop_cible))*100,2)
# Département 4
dep4_nom = 'Sangha'
dep4_pop_cible = 85_000
dep4_personnes_vaccines = 35_700
dep4_taux_attendu = 42.0 #%
dep4_couverture = round((int(dep4_personnes_vaccines)/int(dep4_pop_cible))*100,2)
# Classification
# Département 1
if dep1_couverture < 50:
    dep1_statut = 'ZONE CRITIQUE'
elif dep1_couverture >= 50 and dep1_couverture < 80:
    dep1_statut = 'ZONE A RISQUE'
elif dep1_couverture >= 80 and dep1_couverture < 95:
    dep1_statut = 'ZONE INSUFFISANTE'
else:
    dep1_statut = 'ZONE OPTIMAL'
# Département 2
if dep2_couverture < 50:
    dep2_statut = 'ZONE CRITIQUE'
elif dep2_couverture >= 50 and dep2_couverture < 80:
    dep2_statut = 'ZONE A RISQUE'
elif dep2_couverture >= 80 and dep2_couverture < 95:
    dep2_statut = 'ZONE INSUFFISANTE'
else:
    dep2_statut = 'ZONE OPTIMAL'
# Département 3
if dep3_couverture < 50:
    dep3_statut = 'ZONE CRITIQUE'
elif dep3_couverture >= 50 and dep3_couverture < 80:
    dep3_statut = 'ZONE A RISQUE'
elif dep3_couverture >= 80 and dep3_couverture < 95:
    dep3_statut = 'ZONE INSUFFISANTE'
else:
    dep3_statut = 'ZONE OPTIMAL'
# Département 4
if dep4_couverture < 50:
    dep4_statut = 'ZONE CRITIQUE'
elif dep4_couverture >= 50 and dep4_couverture < 80:
    dep4_statut = 'ZONE A RISQUE'
elif dep4_couverture >= 80 and dep4_couverture < 95:
    dep4_statut = 'ZONE INSUFFISANTE'
else:
    dep4_statut = 'ZONE OPTIMAL'


# === SECTION I : Rapport d'etat global avec compteurs d'alertes et resume executif
print("="*70)
print("RAPPORT INITIAL DU SYSTEME DE SANTE")
print("="*70)
print(f"""Statut des médicaments
     {m1_nom} : {m1_statut}
     {m2_nom} : {m2_statut}
     {m3_nom} : {m3_statut}
     {m4_nom} : {m4_statut}
     {m5_nom} : {m5_statut}""")
print(message_alerte)
print(f"""Niveau d'occupation des 5 hôpitaux
     {h1_nom} : {h1_niveau_occupation}
     {h2_nom} : {h2_niveau_occupation}
     {h3_nom} : {h3_niveau_occupation}
     {h4_nom} : {h4_niveau_occupation}
     {h5_nom} : {h5_niveau_occupation}""")
print(f"""Couverture vaccinale par département
     {dep1_nom} : {dep1_couverture}% [{dep1_statut}]
     {dep2_nom} : {dep2_couverture}% [{dep2_statut}]
     {dep3_nom} {dep3_couverture}% [{dep3_statut}]
     {dep4_nom} : {dep4_couverture}% [{dep4_statut}]""")
print("-"*70)
input("Résumé exécutif :")
print("="*70)