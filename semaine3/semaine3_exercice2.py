# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — Exercice 2 : Triage Patient Urgences CHU Brazzaville
# ============================================================
print('=== SYSTEME DE TRIAGE — URGENCES CHU BRAZZAVILLE ===')
print('Protocole Manchester adapte — DSS Congo 2026')
print()
# --- SAISIE DES DONNEES PATIENT --
nom_patient   = input('Nom du patient : ')
age_patient   = int(input('Age (annees) : '))
temperature   = float(input('Temperature : '))
spo2          = float(input('Saturation O2 en % : '))
tension_syst  = int(input('Tension systolique en mmHg : '))
douleur       = int(input('Cotation de la douleur : '))

# --- VALIDATION DES ENTREES ---
# Validation de la plage de la température 
if temperature < 35.0 or temperature > 43.0:
    print("Valeur de temperature impossible. Vérifier la saisie.")
if temperature == -temperature: # cas d'une valeur négative
    print("La valeur de température ne peux être négatif. Vérifier la valeur.")
# Validation de la plage saturation en oxygène
if spo2 < 50.0 or spo2 > 100:
    print("SpO2 hors plage. Vérifier le capteur.") 
if spo2 == -spo2:
    print("La saturation ne peut être négative. Vérifier votre valeur.")
# Validation de la plage de la tension systolique
if tension_syst < 50 or tension_syst > 250:
    print("Tension hors plage. Vérifier le brassard.")
if tension_syst == -tension_syst:
    print("La tension systolique ne peux être négative. Vérifier la valeur.")
#Validation de la douleur
if douleur < 0 or douleur > 10:
    print("La douteur doit être entre 0 et 10.")
# Vérification de l'âge
if age_patient < 0 or age_patient > 120:
    print("Age invalide. Vérifier la saisie.")


# Statut du paramètre
# statut de la température
if temperature < 36:
    statut_t = 'Hypothermie'
elif temperature > 39.5:
    statut_t = 'Fièvre'
else:
    statut = 'Normal'
# statut de la saturation
if spo2 < 90:
    statut_s = 'Hypoventilation'
elif spo2 > 95:
    statut_s = 'Hyperventilation'
else:
    statut_s = 'Normal'
# statut de la tension systolique
if tension_syst < 110:
    statut_sys = 'Hypotension systolique'
elif tension_syst > 140:
    statut_sys = 'Hypertension systolique'
else:
    statut_sys = 'Normal'


# Protocole de triage
# Niveau 1: immédiat
if temperature > 39.5 or spo2 < 90 or tension_syst > 180:
    niveau_triage  = 'IMMEDIAT'
    couleur_triage = '[ROUGE]'
    delai_pec      = '0 minute'
    action_triage  = 'Medecin present immediatement — code ROUGE active'

# Niveau 2: urgent
elif temperature > 38.5 or spo2 < 94.0 or tension_syst > 140:
    niveau_triage = 'URGENT'
    couleur_triage = 'ORANGE'
    delai_pec = '< 10 minutes'
    action_triage = 'Appeler un médecin sénior'

# Niveau 3: urgent différée
elif temperature > 37.5 or douleur > 6:
    niveau_triage = 'URGENT DIFFERE'
    couleur_triage = 'JAUNE'
    delai_pec = '< 30 minutes'
    action_triage = 'Surveillance par un infirmier'

# Niveau 4: pas urgent
else:
    niveau_triage = 'Pas urgent'
    couleur_triage = 'VERTE'
    delai_pec = "< 120 minutes"
    action_triage = "File d'attente standard"


# --- Affichage de la fiche de triage ---
print("="*60)
print(f"Résultat triage :{nom_patient}")
print("="*60) 
print(f""" Parametres vitaux :
Température : {temperature}c  [{statut_t}]
Saturation en oxygène : {spo2}%  [{statut_s}]
Tension systolique : {tension_syst}mmHg  [{statut_sys}]
Douleur : {douleur}""")
print("-"*60)
print(f"""Niveau de triage : {niveau_triage}
Couleur : {couleur_triage}
Délai de prise en charge : {delai_pec}
Action : {action_triage}""")
print("="*60)