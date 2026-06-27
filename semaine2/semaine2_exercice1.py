# =======================================================
# AKIENI ACADEMY - Projet santé publique
# Semaine 2 - Exercice 1 : Fiche patient CHU Brazzavile
# Nom : ONGOUYA Elie Yann
# Date : 22 juin 2026
# =======================================================


# --- Section 1: variables patient ---
nom_patient = str(input("Entrez votre nom : "))
age_patient = int(input("Entrez votre âge : "))
sexe_patient = str(input("Entrez votre sexe : "))
departement_patient = str(input("Entrez votre département de résidence : "))
courveture_sociale = str(input("Entrez votre couverture sociale : "))


# --- Section 2 : Variales consultation ---
type_consultation = str(input("Quel est le type de consultation : "))
cout_consultation_fcfa = float(input("Coût de la consultation : "))
nb_consultation = int(input("Entrez le nombre de consultation :"))
remise_cnss_pct = float(input("Entrez la remise de la cnss : "))
diagnostic_principal = str(input("Entrez le diagnostique principale : "))


# --- Section 3 : Varaiable hopital ---
nom_hopital = str(input("Entrez le nom de l'hopital : "))
ville_hopital = str(input("Entrez la ville où est situé l'hopital : ")) 
nb_lits_total = int(input("Entrez le nombre de lit de l'hopital : "))
nb_lits_occupes = int(input("Entrez le nombre de lits occupés : "))
nb_medecins_actifs = int(input("Entrez le nombre de medecins actifs : "))

# nombre de consultation dans l'hopital, cette variable n'a pas été définie ici mais dans la partie calcul
# je me suis permi de la ramené ici car ke trouve qu'elle cadre mieux avec cette section
nb_consultation_hopital = int(input("Entrez le nmbre de consultation réalisé dans l'hopital ce jour : "))


# Section 4 : Calculs ---
# coût total après remise de la cnss
cout_total_fcfa = cout_consultation_fcfa*nb_consultation*(1-remise_cnss_pct/100)

# taux d'occupation
taux_occupation_pct = round(nb_lits_occupes/nb_lits_total, 1)

# ratio de consultation par medecin
ratio_consultations_medecin = round(nb_consultation_hopital/nb_medecins_actifs, 1)

# --- Section 5 : AFFICHAGE ---
print("="*60)
print(f'Fiche patient : {nom_patient}')
print(f"Age : {age_patient} \n Sexe {sexe_patient} \n Departement : {departement_patient} \n Couverture : {courveture_sociale}")
print("-"*60)
print("Consultation")
print(f"""Type : {type_consultation} \n Diagnostic : {diagnostic_principal} \n coût unitaire : {cout_consultation_fcfa} \n Remise CNSS : {remise_cnss_pct} \n
      Coût_total : {cout_total_fcfa}""")
print("-"*60)
print(f"Hopital : {nom_hopital}")
print(f"""Ville : {ville_hopital}
      Lits occupés : {nb_lits_occupes}
      Médecins actifs : {nb_medecins_actifs}
      Ratio de consultation : {ratio_consultations_medecin}""")
print("=="*60)
print("Statut : Prise en charge validée")
print("=="*60)