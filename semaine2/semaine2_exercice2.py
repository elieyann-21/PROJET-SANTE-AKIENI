#=======================================================
# AKIENI ACADEMY - Projet santé publique
# Semaine 2 - Exercice 2 : KPIs sanitaires OMS
# Nom : ONGOUYA Elie Yann
# Date : 22 juin 2026
# =======================================================


# --- Données brutes ---
budget_fcfa = 87_450_000 # _ pour la lisibilité des grands nombre
nb_consultation_ext = 4823
nb_hospitalisation = 1247
nb_deces = 18
nb_lits_total = 180
nb_lits_occupes = 143
nb_medecins = 22
nb_infirmiers = 58
population_dept = 128_000
taux_eur_fcfa = 655.957
taux_usd_fcfa = 600.0
cout_journalier_meds = 450_000 # je préfère mettre ça avec les données brutes

# 1. Conversion devises
budget_eur = round(int(budget_fcfa)/taux_eur_fcfa,2)
budget_usd = round(int(budget_fcfa)/taux_usd_fcfa,2)

# 2. Indicateurs OMS
densite_medicale = round((nb_medecins/int(population_dept))*1000, 1)
taux_mortalite = round((nb_deces/nb_hospitalisation)*100, 1)
taux_occupation = round((nb_lits_occupes/nb_lits_total)*100, 1)

# 3. Division entier et modulo
budget_medicament = budget_fcfa*0.35
jours_stock = budget_medicament//int(cout_journalier_meds)
jours_restants = nb_consultation_ext%2 

# 4. Puissance pour projection
budget_n_plus_2 = budget_fcfa*(1.08**2) # dans l'énoncé c'est écrit 8% mais dans le calcul c'est 1,08

# 5. Alerte
if densite_medicale < 2.3:
    alerte = f"La densité médicale est critique, elle est de {densite_medicale}/1000 habts < à la norme OMS (2.3)"
else:
    alerte = "La densité médicale supérieur à la norme de l'OMS"


# === AFFICHAGE RAPPORT ===
print(f'=== Rapport trimestriel Q4 2025 - Hôpital général de Poi,te-Noire ===')
print(f"""Budget
    Dépenses Q4 en franc CFA : {budget_fcfa} franc CFA
    En euro : {budget_eur} euro
    En USD : {budget_usd} USD""") 
print(f"""Indicateurs OMS
    Densité médicale : {densite_medicale}/1000 habts [Norme OMS : >= 2.3]
    Taux de mortalité : {taux_mortalite}% [Seuil alerte : >2%]
    Taux d'occupations : {taux_occupation}%  [Optimal : 70-80%]""")
print(f"""Analyse médicament
    Budget médicaments : {int(budget_fcfa)} franc CFA
    Jours de stock : {jours_stock} jours
    jours dépassement : {jours_restants} jours""")
print(f"""Projection 
      Budget N+2 (8%/an) : {budget_n_plus_2} franc CFA""")
print(f'Alerte : {alerte}')
