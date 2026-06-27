# ==========================================================================================
# AKIENI ACADEMY - Projet santé publique
# Semaine 2 - Challenge : Demande urgente du responsable DSS
# Nom : ONGOUYA Elie Yann
# Date : 24 juin 2026
# ==========================================================================================

# SECTION 1 - Variable de chaque hopital
# Hopital de Kinkala
h1_budget_trimestre = 12_500_000 # _ pour les grands nombre
h1_Consultation_ext = 1847
h1_hospitalisation = 312
h1_deces = 8
h1_total_lits = 45
h1_total_lits_occupes = 41
h1_medecins_actifs = 3
h1_pop_desservie = 85_000 

# CMS de Vindza
h2_budget_trimestre = 6_800_000
h2_Consultation_ext = 923
h2_hospitalisation = 87
h2_deces = 2
h2_total_lits = 20
h2_total_lits_occupes = 14
h2_medecins_actifs = 1
h2_pop_desservie = 42_000 

# Hopital de Kindamba
h3_budget_trimestre = 9_200_000
h3_Consultation_ext = 1234
h3_hospitalisation = 201
h3_deces = 11
h3_total_lits = 35
h3_total_lits_occupes = 33
h3_medecins_actifs = 2
h3_pop_desservie = 67_000 


# Section 2 - Calcul des KPI
# Hopital de Kinkala
h1_cout_moyen = round(int(h1_budget_trimestre)/h1_Consultation_ext, 2)
h1_taux_occupation = round((h1_total_lits_occupes/h1_total_lits)*100,2)
h1_densite_mediacle = round(((h1_medecins_actifs/int(h1_pop_desservie))*1000),2)
h1_taux_mortalite =  round((h1_deces/h1_hospitalisation)*100,2)

# CMS de Vindza
h2_cout_moyen = round(int(h2_budget_trimestre)/h2_Consultation_ext, 2)
h2_taux_occupation = round((h2_total_lits_occupes/h2_total_lits)*100,2)
h2_densite_mediacle = round(((h2_medecins_actifs/int(h2_pop_desservie))*1000),2)
h2_taux_mortalite =  round((h2_deces/h2_hospitalisation)*100,2)

# Hopital de Kindamba
h3_cout_moyen = round(int(h3_budget_trimestre)/h3_Consultation_ext, 2)
h3_taux_occupation = round((h3_total_lits_occupes/h3_total_lits)*100,2)
h3_densite_mediacle = round(((h3_medecins_actifs/int(h3_pop_desservie))*1000),2)
h3_taux_mortalite =  round((h3_deces/h3_hospitalisation)*100,2) # le résultat en %

# SECTION 3 - Identification de l'hopital critique
# Hopital de Kinkale
if h1_taux_mortalite > 2 or h1_densite_mediacle < 0.05:
    h1_situation ="L'hopital de Kinkala est dans un situation critique"
else: 
    h1_situation = "L'hopital de Kinkala n'est pas dans un situation critique"

# CMS de Vondza
if h2_taux_mortalite > 2 or h2_densite_mediacle < 0.05:
    h2_situation = "Le CMS de Vindza est dans une situation critique"
else: 
    h2_situation = "Le CMS de Vindza n'est pas dans une situation critique"

# Hopital de Kindamba
if h3_taux_mortalite > 2 or h3_densite_mediacle < 0.05:
    h3_situation = "L'hoîtal de Kindamba est dans une situation critique"
else:
    h3_situation = "L'hoîtal de Kindamba est dans une situation critique"

# SECTION 4 - Calcul si le budget total des 3 hopitaux suffit pour passer à 5 medecins
# Hopital de Kinkala
h1_cout_5medecins = (1200000*5) # nous permet de calculer le cout pour les 5 medecins
if h1_cout_5medecins < h1_budget_trimestre:
    h1_ajout_5medeins ="L'hopital de Kinkala a le budget suffisant pour passer à 5 médecins"
else:
    h1_ajout_5medecins = "L'hôpital de Kinkala n'a pas le budget necessaire pour passer à 5 médecins"

# CMS de Vindza
h2_cout_5medecins = (1200000*5)
if h2_cout_5medecins < h2_budget_trimestre:
    h2_ajout_5medeins = "Le CMS de Vindza a le budget suffisant pour passer à 5 médecins"
else:
    h2_ajout_5medeins = "Le CMS de Vindza n'a pas le budget necessaire pour passer à 5 médecins"

# Hopital de Kindamba
h3_cout_5medecins = (1200000*5)
if h3_cout_5medecins < h3_budget_trimestre:
    h3_ajout_5medecins = "L'hopital de Kibdamba a le budget suffisant pour passer à 5 médecins"
else:
    h3_ajout_5medecins = "L'hôpital de Kindamba n'a pas le budget necessaire pour passer à 5 médecins"

# SECTION 5 - Rapport 
print("="*65)
print(f'Rapport sur la situation des 3 hôpitaux du département du Pool')
print("="*65)
# Hôpital de Kinkala 
print(f"I- Hopital de Kinkala \n 1- Niveau des indicateurs" )
print(f'''- Coût moyen par patient : {h1_cout_moyen} franc CFA;
- Taux d'occupation de l'hôpital : {h1_taux_occupation}%;
- Densité médicale : {h1_densite_mediacle} pour 1000 habitants;
- Taux de mortalité de l'hôpital : {h1_taux_mortalite}%.''')
print(f"""2- Situation de l'hôpital
    {h1_situation}""")
print(f"3- Possibilité d'augmenter à 5 le nombre de médecins \n {h1_ajout_5medeins}" )

# CMS de Vindza
print(f"II- CMS de Vindza \n 1- Niveau des indicateurs" )
print(f'''- Coût moyen par patient : {h2_cout_moyen} franc CFA;
- Taux d'occupation de l'hôpital : {h2_taux_occupation}%;
- Densité médicale : {h2_densite_mediacle} pour 1000 habitants;
- Taux de mortalité de l'hôpital : {h2_taux_mortalite}%.''')
print(f"""2- Situation de l'hôpital
    {h2_situation}""")
print(f"3- Possibilité d'augmenter à 5 le nombre de médecins \n {h2_ajout_5medeins}" )

# Hopital de Kindamba
print(f"III- Hopital de Kindamba \n 1- Niveau des indicateurs" )
print(f'''- Coût moyen par patient : {h3_cout_moyen} franc CFA;
- Taux d'occupation de l'hôpital : {h3_taux_occupation}%;
- Densité médicale : {h3_densite_mediacle} pour 1000 habitants;
- Taux de mortalité de l'hôpital : {h3_taux_mortalite}%.''')
print(f"""2- Situation de l'hôpital
    {h3_situation}""")
print(f"3- Possibilité d'augmenter à 5 le nombre de médecins \n {h3_ajout_5medecins}" )
print("="*70)
