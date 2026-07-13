# ======================================================
# AKIENI ACADEMY
# SEMAINE 5 - EXERCICE : CALCULATRICE 
# DESCRIPTION : creer une calculatrice qui permet d'effectuer les 4 operations de base
# addition, soustraction, multiplication et division.
# ======================================================

# choix de l'operation par l'utilisateur
print("="*70)
print("Bonjour\n Bienvenue dans votre calcultatrice")
print("-"*70)
print("Choisissez parmis les operations suivants pour réaliser votre opération\n add : Addition\n sous: Soustraction\n mul: Multiplication\n div: Division")
print("-"*70)
operateur = str(input("Saisissez l'opérateur :"))

# vérifie si l'opérateur saisit correspond à un opérateur valide
while operateur not in ['add','sous','mul','div']:
        print("Erreur : L'operateur saisit doit correspondre a celui du menu")
        operateur = str(input("Saisissez l'opérateur :"))

# définition de la fonction d'addition
def addition():
    """La fonction addition permet 
    d'additionner deux entiers naturel"""
    num1 = float(input("chiffre 1 :"))
    num2 = float(input("chiffre 2 :"))
    addition = num1 + num2
    print("Résultat :",addition)

# définition de la fonction de soustraction
def soustraction():
    """La fonction soustraction permet de soustraire deux entiers"""
    num1 = float(input("chiffre 1 :"))
    num2 = float(input("chiffe 2 "))
    soustraction = num1 - num2
    print("Résultat :", soustraction)

# définition de la fonction de multification
def multiplication():
    """La fonction multiplication permet de multiplier deux entiers"""
    num1 = float(input("chiffre 1 :"))
    num2 = float(input("chiffre 2 :"))
    multiplication = num1 * num2
    print("Résultat :", multiplication)

# définition de la fonction de division
def division():
    """La fonction division permet de multiplier deux entiers"""
    num1 = float(input("chiffre 1"))
    num2 = float(input("chiffre 2 :"))
    while num2 == 0: # pour le cas où le dénominateur est 0
        print("Erreur : 0 ne peut etre un diviseur\n Veuillez saisir une nouvelle valeur")
        num2 = float(input("chiffre 2 :"))
    division = num1/num2
    print('Divion :', division)

# Execution de la calculatrice
if operateur == "add":
    print("Opération : addition")
    addition()
elif operateur == "sous":
    print("Opération : soustraction")
    soustraction()
elif operateur == "mul":
    print("Opération : multiplication")
    multiplication()
else:
    print("Opération : division")
    division()

       



