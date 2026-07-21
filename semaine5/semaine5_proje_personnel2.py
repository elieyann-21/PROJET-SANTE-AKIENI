# ==================================================================================================================
# AKIENI ACEDEMY 
# PORJET PERSONNEL 1: SYSTEME DE GESTION DES MALADES
# DESCRIPTION: 
# ===================================================================================================================

# initialisation des listes
services = ["SPN", "BTA", "CPS", "Vaccination", "Consultation curative", "Laboratoire", "Pharmacie"]
actes_medicaux = [ "suivi prénatal", "accouchement", "consultation préscolaire", "vaccination", "consultation", 'examen de laboratoire', 'achat médicament']
tarification_actes_medicaux = {"suivi prénatal": 15000, "accouchement": 10000, "consultation préscolaire": 2000, "vaccination": 0, "consultation": 3000,}
examens_laboratoires = ['goutte épaisse', 'CRP', 'VS', 'VIH' ]
tarifications_examens_laboratoires = {'goutte épaisse': 1000, 'CRP': 5000, 'VS': 4000, 'VIH': 0}
medicaments = ['arthemeter', 'paracetamol', 'amoxiciline', 'ARV']
tarification_medicaments = {'arthemeter': 2000, 'paracetamol': 500, 'amoxiciline': 1000, 'ARV': 0}
patients = {}
dico_nom = {}
liste_motif_visite = []
liste_service_oriente = []
examens_demandes = []
medicaments_prescrits = []
cout_actes = 0
cout_laboratoire = 0
cout_medicament = 0
# définition des fonctions

def orientation():
    """Cette fonction permet de concernvoir une fiche patient contenant des informations sur son nom
    , son âge, son sexe, son poids, sa température, le motif de sa visite et le service dans lequel il est orienté"""
    # on prend les informations personnels du patients
    nom = input('Quel est votre nom ? : ').lower()
    prenom = input("Quel est votre prénom ? : ").lower()
    dico_nom[nom] = prenom # ajout du nom et du prénom au dictionnaire de noms
    age = int(input('Quel est votre age ? : ')) # voir la gestion d'erreur pour gérer les cas de valeurs abérantes 
    sexe = input('Quel est votre sexe ?: ').lower()
    while sexe != "homme" and sexe != "femme":
        print(f' Inserez : homme ou femme')
        sexe = input('Quel est votre sexe ?: ').lower()
    poids = float(input("Quel est votre poids : "))
    temp = float(input('Quel est votre température ?: '))
   
    # on oriente le patient en fonction de son motif de venu
    print(f"""Quel est le motif de votre venue au CSI ?
          1- suivi prénatal
          2- accouchement
          3- consultation préscolaire 
          4- vaccination
          5- consultation
          6- examen de laboratoire
          7- achat de médicament""")
    motif_visite = input("Choisissez parmi les options du menu:")
    liste_motif_visite.append(motif_visite)
    for i in range(len(actes_medicaux)):
        if motif_visite == actes_medicaux[i]:
            service_oriente = services[i]
            liste_service_oriente.append(service_oriente)
    patients[nom] = [age, sexe, poids, temp, motif_visite, service_oriente]
    
    #affichage de la fiche du patient
    print("="*70)
    print(f'Fiche du patient')
    print("-"*70)
    print(f'''\n Nom et prénom: {nom} \b {prenom} \n Sexe: {sexe} \n Age: {age} ans \n Poids: {poids} Kg \n Température: {temp} degré \n Motif de la visite: {motif_visite} \n Service orienté : {service_oriente} ''')
    print("-"*70)


def laboratoire():
    """ Cette fonction permet d'établir le bon d'examen du patient"""
    Identifiant = input("Entrer le nom du patient : ").lower() # ici c'est le nom du patient mais dans la réalité c'est un identifiant unique
    if Identifiant in dico_nom:
        consultant = input("Nom du consultant : ")
        nb_examens = int(input("Nombre d'examen demandé : "))
        for i in range(nb_examens):
            examens = (input(' Examens demandés : '))
            while examens not in examens_laboratoires:
                print(f"L'examen demandé n'est pas réalisé au CSI")
                examens = (input(' Examens demandés : '))
            examens_demandes.append(examens)
# affichage du bon d'examen
        print("="*50)
        print("Bon d'examen")
        print("-"*50)
        print(f'\n Consultant : {consultant} \n Nom du patient : {Identifiant} \b {dico_nom[Identifiant]} \n Examens demandés : {examens_demandes} ')
        print("="*50)

def pharmacie():
    """ Cette fonction permet d'établir l'ordonnace du patient """
    Identifiant = input("Entrer le nom du patient : ").lower()
    if Identifiant in dico_nom:
        consultant = input("Nom du consultant : ")
        nb_medicament = int(input("Nombre de médicament prescrit : "))
        for i in range(nb_medicament):
            prescription = (input(' Médicaments prescrits : '))
            while prescription not in medicaments:
                print(f"Le médicament prescrit n'est pas en stock dans la pharmacie")
                examens = (input(' Médicaments prescrits : '))
            medicaments_prescrits.append(prescription)
# affichage du bon d'examen
        print("="*50)
        print(" Ordonnance médicale")
        print("-"*50)
        print(f'\n Consultant : {consultant} \n Nom du patient : {Identifiant} \b {dico_nom[Identifiant]} \n Examens demandés : {medicaments_prescrits} ')
        print("="*50)
    

# Exécution du code
while True:
    print('Bienvenue au CSI de Nkombo matari')
    print('''Choissez parmi les tâches suivantes:
          1- Orienter un patient
          2- Faire un examen de laboratoire
          3- Acheter un médicament
          4- Arreter''')
    try:
        tache = int(input("Entrez un chiffre entre 1 et 3 :"))
        if tache == 1:
            orientation()
        elif tache == 2:
            laboratoire()
        elif tache == 3:
            pharmacie()
        elif tache == 4:
            print("Merci d'avoir utilisé le système.")
            break
        else:
            print("Choix invalide.")
    except ValueError:
            print("Veuillez entrer un nombre valide.")

