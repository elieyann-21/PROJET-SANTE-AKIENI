# ==================================================================================================================
# AKIENI ACEDEMY 
# PORJET PERSONNEL 1: SURVEILLANCE DES MALADIES A POTENTIEL EPIDEMIQUE
# DESCRIPTION: depuis l'année 2024, le district sanitaire de Djiri notifie regulièrement des cas de maladies
# à potentiel épidémique qui font l'objet d'une surveillance particulière. Pour certaines de ces maladies des 
# vaccins existent et sont disponibles dans le district sanitaire. 
# Ce système de surveillance sera chargé de suivre quotidiennement les déclarations de cas suspects des maladies
# sous surveillance, faire des croisement avec les couvertures vaccinales et données des alertes pour une prise de 
# de décision rapide et efficace.
# ===================================================================================================================

# Données dispobibles
nb_aire_sante = 8
nb_csi_leaders = 4
csi_leaders = []
aire_sante = []
maladies = []
epidemio = {}
# Déclarations des données de surveillance
def completude():
    rapport_complet = 0
    for i in range(csi_leaders):
        items_remplis = int(input("Nombre d'items remplis :"))
        completude = round((items_remplis/10)*100, 2)
        print(f"La complétude du rapport du CSI {i} est de : completude%")
        if completude == 100:
            rapport_complet +=1 
    print(f'{rapport_complet}/4 sont complets')

def enregistrement():
    for i in range(nb_csi_leaders):
        csi_leaders = input("Entrez le nom du CSI leader de l'aire de santé : ")
        aire_sante = input("Entrez le nom de l'aire de santé : ")
        maladie = input("Entrez la maladie")
        maladies.append(maladie)
        cas_suspect = int(input("Cas suspect de :"))
        cas_confirme = int(input("Cas confirmé :"))
        deces = int(input("Nombre de décès :"))
        letalite = round((deces/cas_confirme)*100, 2)
        print(letalite)
        print("-"*50)
        print(f'\n Centre de santé: {csi_leaders} \n Aire de santé: {aire_sante} \n Maladie: {maladie}, Suspects: {cas_suspect} \n Confirmé: {cas_confirme} \n Décès: {deces} \n Létalité: {letalite}')
        print("-"*50)
        epidemio[csi_leaders] = [aire_sante, maladies, cas_suspect, cas_confirme]
    print("="*50)
def prelevement():
    for i in maladies:
        print(f'Maladie : {i}')
        prelevement = input('Prélèvement réalisé :')
        if prelevement == "Oui":
            nb_prelevement = int(input("Nombre de prélèvement :"))
            resultat = input("Résultat :") # posotif/negatif/ non disponible


while True:
    print("Bienvenue dans le système de surveillance épidémiologique")
    print(f"""Que voulez vous faire : 
        1- saisir des donner
        2- Quitter le programme""")
    try:
        tache = int(input("Choisissez parmi les options du menu: "))
    except ValueError:
        print("Entrer un chiffre valide")
    
    if tache == 1:
        completude()
        enregistrement()
        prelevement()
    else:
        print("Au revoir à bientot")
        break