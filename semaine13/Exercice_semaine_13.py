# =================================================
# ANALYSE DES DONNEES AVEC PENDAS
# ==================================================
# Partie A: charger et explorer les données
# -------------------------------------------------
# Exercice 1 - Premier contact

import pandas as pd

DataBase = pd.read_csv(
    "C:/Users/HP/Documents/PROJET-SANTE-AKIENI/semaine13/monde_2023_academy.csv"
)

print(DataBase.head())  # Affiche les 5 premières lignes du DataFrame

print(
    " Nombre de lignes et de colonnes:"
    + str(DataBase.shape[0])
    + " lignes et "
    + str(DataBase.shape[1])
    + " colonnes"
)

print("Nature des variables:")
print(DataBase.info())

# La colonne pop est de type str alors qu'elle devrait être de type int.
print(DataBase["pop"].iloc[0:20])  # Affiche les 20 premières valeurs de la colonne pop
# Certaines valeurs contiennent des virgules.

# Convertir la colonne pop en type int
DataBase["pop"] = (
    DataBase["pop"].str.replace(",", "").astype(int)
)  # le str.replace(",", "") supprime les virgules dans les valeurs de la colonne pop

print(DataBase.info())  # Vérifie que la colonne pop est maintenant de type int

# -------------------------------------------------
# Exercice 2 - Un résumé pour le comité
print("Résumé statistique des variables numériques:")
print(DataBase.describe())
print(
    "La population totale est de " + str(round(DataBase["pop"].sum(), 2)) + " habitants"
)
print(
    "Le PIB médiant par habitant est de "
    + str(round(DataBase["gdpPercap"].median(), 2))
    + " alors que le PIB moyen par habitant est de "
    + str(round(DataBase["gdpPercap"].mean(), 2))
    + " $."
    + "L'écart de plus de 10000$ entre les deux témoigne de la dysymétrie de cette indicateur et d'un grand écart entre les extrêmes avec aussi des valeurs manquantes."
)

print("Résumé statistique des variables catégorielles:")
print(DataBase.describe(include=["object"]))  # Résumé des variables catégorielles
print("Mode des variables catégorielles:")

# ==================================================
# Partie B: netoyer les données
# -------------------------------------------------
# Exercice 3 - Des données incomplètes

print(
    "Nombre de valeurs manquantes par colonne:"
    + "\n"
    + "Valeur absolue"
    + "\n"
    + str(DataBase.isnull().sum())
    + "\n"
    + "Valeur relative (en %)"
    + "\n"
    + str(DataBase.isnull().sum() * 100 / len(DataBase))
)  # Affiche le nombre de valeurs manquantes
print(
    "Les variables lifeExpa et gdpPercap ont respectivement"
    + str(round(DataBase["lifeExp"].isnull().sum() * 100 / len(DataBase), 2))
    + "%"
    + " et "
    + str(round(DataBase["gdpPercap"].isnull().sum() * 100 / len(DataBase), 2))
    + "%"
    + " de valeurs manquantes."
    + "qui sont inférieur à 5% des valeurs de ces variables. Nous allons donc les imputater par leurs médianes respectives."
)

DataBase["lifeExp"] = DataBase["lifeExp"].fillna(
    DataBase["lifeExp"].median(), inplace=True
)  # Impute les valeurs manquantes de la colonne lifeExp par la médiane
DataBase["gdpPercap"] = DataBase["gdpPercap"].fillna(
    DataBase["gdpPercap"].median(), inplace=True
)  # Impute les valeurs manquantes de la colonne gdpPercap par la médiane

print(
    "Nombre de valeurs manquantes après imputation:"
    + "\n"
    + "lifeExp: "
    + str(DataBase["lifeExp"].isnull().sum())
    + "\n"
    + "gdpPercap: "
    + str(DataBase["gdpPercap"].isnull().sum())
)  # Vérifie le nombre de valeurs manquantes dans la colonne lifeExp

# -------------------------------------------------
# Exercice 4 - Un doublon dans l'export

print(
    "Nombre de doublons: " + str(DataBase.duplicated().sum())
)  # Affiche le nombre de doublons

DataBase = DataBase.drop_duplicates()  # Supprime les doublons
print(
    "Nombre de doublons après suppression: " + str(DataBase.duplicated().sum())
)  # Affiche le nombre de doublons après suppression

print(
    DataBase.info()
)  # Vérifie la structure du DataFrame après suppression des doublons
print(
    DataBase.shape
)  # Vérifie le nombre de lignes et de colonnes après suppression des doublons


# -------------------------------------------------
# Exercice 5 - Un pays introuvable
print(
    DataBase["country"] == "Congo"
)  # Vérifie si le pays "Congo" est présent dans la colonne country

print(
    DataBase.loc[DataBase["iso3"] == "COG"]
)  # Rechercher la ligne correspondant au pays "Congo" dans la colonne iso3
DataBase["country"] = DataBase[
    "country"
].str.capitalize()  # Met en majuscule la première lettre de chaque mot dans la colonne country
print(
    DataBase["country"] == "Congo"
)  # Vérifie si le pays "Congo" est présent dans la colonne country après la mise en majuscule
