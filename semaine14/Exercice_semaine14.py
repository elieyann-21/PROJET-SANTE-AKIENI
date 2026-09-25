# Exercice semaine 14
# Chargement des library
import numpy as np
import pandas as pd

# chargement des bases de données
Data_orders = pd.read_csv("C:/Users/HP/Documents/PROJET-SANTE-AKIENI/semaine14/Dataset/olist_orders_dataset.csv")
Data_items = pd.read_csv("C:/Users/HP/Documents/PROJET-SANTE-AKIENI/semaine14/Dataset/olist_order_items_dataset.csv")
Data_products = pd.read_csv("C:/Users/HP/Documents/PROJET-SANTE-AKIENI/semaine14/Dataset/olist_products_dataset.csv")
Data_cat_trans = pd.read_csv("C:/Users/HP/Documents/PROJET-SANTE-AKIENI/semaine14/Dataset/product_category_name_translation.csv")
Data_sellers = pd.read_csv("C:/Users/HP/Documents/PROJET-SANTE-AKIENI/semaine14/Dataset/olist_sellers_dataset.csv")
Data_customers = pd.read_csv("C:/Users/HP/Documents/PROJET-SANTE-AKIENI/semaine14/Dataset/olist_customers_dataset.csv")
Data_reviews = pd.read_csv("C:/Users/HP/Documents/PROJET-SANTE-AKIENI/semaine14/Dataset/olist_order_reviews_dataset.csv")
print('Base chargée')

for i in [Data_orders, Data_items, Data_products, Data_cat_trans, Data_sellers, Data_customers, Data_reviews]:
    print(f'{i.dtypes}')

# Exercice 1 : Créer un dataframe récapitulatif des bases de données chargées
dataframe = {"orders": Data_orders, "items": Data_items, "products": Data_products, "category_transactions": Data_cat_trans, "sellers": Data_sellers, "customers": Data_customers, "reviews": Data_reviews}
recap = pd.DataFrame(columns=['Nom de la base', 'Nombre de lignes', 'Nombre de colonnes', 'Colonnes', 'Types de données'])
for name, df in dataframe.items():
    recap = pd.concat([recap, pd.DataFrame({'Nom de la base': [name], 'Nombre de lignes': [df.shape[0]], 'Nombre de colonnes': [df.shape[1]], 'Colonnes': [list(df.columns)], 'Types de données': [list(df.dtypes)]})], ignore_index=True)
print(recap)

#Exercice 2 - Valeurs manquantes : où et combien ? 
for name, df in dataframe.items():
    print(f" {name}: \n{df.isnull().sum()} \n {df.isnull().sum().sum()/df.size*100}% de valeurs manquantes \n")

# Exercice 3 - Une clé qui ne tient pas sa promesse 
nb_doublons = Data_reviews.review_id.duplicated().sum() # compte le nombre de doublons
print(nb_doublons)

doublons = Data_reviews.iloc[Data_reviews.review_id.duplicated(keep=False)].sort_values(by='review_id') # affiche les lignes en doubles
doublons_order = doublons.groupby("review_id")["order_id"].nunique().reset_index() # affiche le nombre de review_id avec le même order_id
print(doublons_order[doublons_order["order_id"] > 1])

nb_doublons_order = nb_doublons - doublons_order.shape[0] # calcul le nombre de doublons 
print(f'Nombre de doublons avec le même order_id :{nb_doublons_order}')