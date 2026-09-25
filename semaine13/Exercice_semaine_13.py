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
].str.strip().str.capitalize()  # Met en majuscule la première lettre de chaque mot dans la colonne country
print(
    DataBase.loc[DataBase["iso3"] == "COG"]
)  # Vérifie si le pays "Congo" est présent dans la colonne country après la mise en majuscule

#-------------------------------------------------
# Exercice 6 - déja répondu à la question 1


#-------------------------------------------------
# Exercice 7 - déja répondu à la question 1
# a) Un collègue n'a besoin que du nom du pays, du continent et de l'espérance de vie - pas du reste du 
#fichier. Préparez cet extrait

DataBase_col = DataBase[["country", "continent", "lifeExp"]]
# b) Il vous demande ensuite un aperçu des 5 premiers pays du fichier : une fois avec toutes leurs 
# colonnes, une fois avec seulement le nom du pays et sa population. 
print(DataBase.head(5))  # Affiche les 5 premières lignes du DataFrame
print(DataBase[["country", "pop"]].head(5))  # Affiche les 5 premières lignes du DataFrame avec seulement le nom du pays et sa population

# c) Enfin, il veut la liste des pays de plus de 100 millions d'habitants, du plus peuplé au moins peuplé. 
country_pop100 = DataBase[DataBase["pop"] > 100000000][["country", "pop"]].sort_values(by="pop", ascending=False)  # Filtre les pays avec une population supérieure à 100 millions et trie par population décroissante
print(country_pop100)

# -------------------------------------------------
# Exercice 8 - La richesse « typique » d'un pays africain
DataBase_PIB_Afric = DataBase[DataBase["continent"] == "Africa"][["country", "gdpPercap"]].sort_values(by = "gdpPercap", ascending= False) # Filtre les pays d'Afrique et trie par PIB par habitant décroissant
print(sum(DataBase_PIB_Afric["gdpPercap"])/len(DataBase_PIB_Afric)) # Affiche le PIB moyen par habitant des pays d'Afrique
print(DataBase_PIB_Afric["gdpPercap"].median())

print(f"Le PIB moyen par habitant des pays d'Afrique est de {round(sum(DataBase_PIB_Afric['gdpPercap'])/len(DataBase_PIB_Afric), 2)
} $ et le PIB médian par habitant est de {round(DataBase_PIB_Afric['gdpPercap'].median(), 2)} $. soit un écart de {round(sum(DataBase_PIB_Afric['gdpPercap'])/len(DataBase_PIB_Afric) - DataBase_PIB_Afric['gdpPercap'].median(), 2)} $ entre les deux indicateurs.")

#-------------------------------------------------
# Exercice 9 - Espérance de vie moyenne et écart type
# Afrique
# Exercice 9
DataBase_lifeExp_Africa = DataBase[(DataBase["continent"] == "Africa")][["country", "lifeExp"]] 
print(DataBase_lifeExp_Africa["lifeExp"].mean())
print(DataBase_lifeExp_Africa["lifeExp"].std())

# Europe
DataBase_lifeExp_Europe = DataBase[(DataBase["continent"] == "Europe")][["country", "lifeExp"]] 
print(DataBase_lifeExp_Europe["lifeExp"].mean())
print(DataBase_lifeExp_Europe["lifeExp"].std())

print(f"L'espérance de vie moyenne en Afrique est de {round(DataBase_lifeExp_Africa['lifeExp'].mean(), 2)} ans avec un écart type de {round(DataBase_lifeExp_Africa['lifeExp'].std(), 2)} ans. En Europe, l'espérance de vie moyenne est de {round(DataBase_lifeExp_Europe['lifeExp'].mean(), 2)} ans avec un écart type de {round(DataBase_lifeExp_Europe['lifeExp'].std(), 2)} ans.")

# ---------------------------------------------------------
# Exercice 10 - Comparaison de l'espérance de vie et du PIB par habitant entre le Congo et la République Démocratique du Congo
DataBase_congo = DataBase[(DataBase["iso3"] == "COG") | (DataBase["iso3"] == "COD")][["country", "lifeExp", "gdpPercap", "pop"]]
print(DataBase_congo)   

#---------------------------------------------------------
# Exercice 11 - Espérance de vie moyenne et espérance de vie pondérée par la population
Esperance_vie_moyenne = round(DataBase["lifeExp"].mean(), 2)
Esperance_vie_ponderee = round((DataBase["lifeExp"] * DataBase["pop"]).sum() / DataBase["pop"].sum(), 2)
print(f"L'espérance de vie moyenne est de {Esperance_vie_moyenne} ans et l'espérance de vie pondérée par la population est de {Esperance_vie_ponderee} ans. L'écart entre les deux indicateurs est de {round(Esperance_vie_ponderee - Esperance_vie_moyenne, 2)} ans.")

#---------------------------------------------------------
# Exercice 12 - Corrélation entre l'espérance de vie et le PIB par habitant
corr = DataBase[["lifeExp", "gdpPercap"]].corr()
print(f"La corrélation entre l'espérance de vie et le PIB par habitant est de {round(corr.loc['lifeExp', 'gdpPercap'], 2)}. Cela indique une corrélation positive entre les deux variables, ce qui signifie que les pays avec un PIB par habitant plus élevé ont tendance à avoir une espérance de vie plus longue.")

# ---------------------------------------------------------
# Exercice 13 - Restitution écrite 
# En 5 à 8 phrases, rédigez une synthèse destinée à quelqu'un qui découvre ce jeu de données. Utilisez 
# au moins 4 chiffres que vous avez calculés vous-même, et au moins 3 des mots suivants : moyenne, 
# médiane, écart-type, biais, corrélation, valeur aberrante.
