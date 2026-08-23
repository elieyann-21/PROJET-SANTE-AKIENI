--- Partie 0: importation des bases de données
--- Insertion des données des tables primaires
BULK INSERT sellers
FROM 'C:\Users\HP\Documents\PROJET-SANTE-AKIENI\semaine10\Ecommerce\archive\olist_sellers_dataset.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    CODEPAGE = '65001',
    TABLOCK
);

--- Importation de la table product_category_name_translation
BULK INSERT product_category_name_translation
FROM 'C:\Users\HP\Documents\PROJET-SANTE-AKIENI\semaine10\Ecommerce\archive\product_category_name_translation.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    CODEPAGE = '65001',
    TABLOCK
);

--- Imporation de la table producs
CREATE TABLE products_import ( --- la table product import a été créer pour que le nombre de colonne du CSV corresponde avec celle de la table
    product_id VARCHAR(32),
    product_category_name VARCHAR(100),
    product_name_lenght INT,
    product_description_lenght INT,
    product_photos_qty INT,
    product_weight_g INT,
    product_length_cm INT,
    product_height_cm INT,
    product_width_cm INT
);

BULK INSERT products_import --- les données ont été importé dans la table ayant le même nombre de fichier que le CSV
FROM 'C:\Users\HP\Documents\PROJET-SANTE-AKIENI\semaine10\Ecommerce\archive\olist_products_dataset.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    CODEPAGE = '65001',
    TABLOCK
);

INSERT INTO products ( --- les données ont été transféré de la table ayant le bon nombre de colonne vers la table ayant plus de colonne
    product_id,
    product_category_name,
    product_name_lenght,
    product_description_lenght,
    product_photos_qty,
    product_weight_g,
    product_length_cm,
    product_height_cm,
    product_width_cm,
    product_brand,
    is_active
)
SELECT
    product_id,
    product_category_name,
    product_name_lenght,
    product_description_lenght,
    product_photos_qty,
    product_weight_g,
    product_length_cm,
    product_height_cm,
    product_width_cm,
    NULL AS product_brand,
    1 AS is_active
FROM dbo.products_import;

SELECT * FROM products
DROP TABLE products_import --- suppresion de la table d'importation

--- Importation de la table customer
BULK INSERT customers
FROM 'C:\Users\HP\Documents\PROJET-SANTE-AKIENI\semaine10\Ecommerce\archive\olist_customers_dataset.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    CODEPAGE = '65001',
    TABLOCK
);
SELECT * FROM customers;

--- Importation des tables dépendantes
--- Importation de la table orders
BULK INSERT orders
FROM 'C:\Users\HP\Documents\PROJET-SANTE-AKIENI\semaine10\Ecommerce\archive\olist_orders_dataset.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    CODEPAGE = '65001',
    TABLOCK
);
SELECT * FROM orders;

--- Importation de la table order_items
CREATE TABLE order_items_import(
order_id VARCHAR(50), FOREIGN KEY (order_id) REFERENCES orders(order_id),
order_item_id INT PRIMARY KEY(order_id, order_item_id),
product_id VARCHAR(50), FOREIGN KEY (product_id) REFERENCES products(product_id),
seller_id VARCHAR(50), FOREIGN KEY(seller_id) REFERENCES sellers(seller_id),
shipping_limit_date DATETIME,
price DECIMAL(10,2) NOT NULL,
freight_value DECIMAL(10,2) NOT NULL);

BULK INSERT order_items_import
FROM 'C:\Users\HP\Documents\PROJET-SANTE-AKIENI\semaine10\Ecommerce\archive\olist_order_items_dataset.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    CODEPAGE = '65001',
    TABLOCK
);
SELECT * FROM order_items_import;

INSERT INTO order_items(
    order_id,
    order_item_id,
    product_id,
    seller_id,
    shipping_limit_date,
    price,
    freight_value)
SELECT 
    order_id,
    order_item_id,
    product_id,
    seller_id,
    shipping_limit_date,
    price,
    freight_value
FROM order_items_import;

SELECT * FROM order_items
DROP TABLE order_items_import

--- Importation de la table order_payments
BULK INSERT order_payments
FROM 'C:\Users\HP\Documents\PROJET-SANTE-AKIENI\semaine10\Ecommerce\archive\olist_order_payments_dataset.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    CODEPAGE = '65001',
    TABLOCK);

--- Importation de la table order_reviews
--- Importation de la base de données csv sous forme de flat file dénommé order_reviews_import
SELECT * FROM order_reviews_import
--- Ajout de la colonne review_comment_message à order_reviews
ALTER TABLE order_reviews
ADD review_comment_message VARCHAR(500)

INSERT INTO order_reviews(--- insertion des données de order_review_import vers order_reviews
    review_id,
    order_id,
    review_score,
    review_comment_title,
    review_creation_date,
    review_answer_timestamp,
    review_comment_message)

SELECT DISTINCT 
    review_id,
    order_id,
    review_score,
    review_comment_title,
    review_creation_date,
    review_answer_timestamp,
    review_comment_message
    FROM (--- gestion des doublons 
    SELECT *,
           ROW_NUMBER() OVER (--- Attribution d'un numéro de ligne à chaque doublon
               PARTITION BY review_id --- regroupe les lignes ayant le même review_id
               ORDER BY review_id
           ) AS rn
    FROM order_reviews_import
) AS t
WHERE rn = 1;

SELECT * FROM order_reviews;

DROP TABLE order_reviews_import;

--- Vérification de l'import
SELECT 'customers' AS Nom_table, COUNT(*) AS Nombre_ligne 
FROM customers
UNION ALL 
SELECT 'sellers' AS Nom_table, COUNT(*) AS Nombre_ligne 
FROM sellers
UNION ALL
SELECT 'products' AS Nom_table, COUNT(*) AS Nombre_ligne 
FROM products
UNION ALL
SELECT 'product_category_name_translation' AS Nom_table, COUNT(*) AS Nombre_ligne 
FROM product_category_name_translation
UNION ALL
SELECT 'orders' AS Nom_table, COUNT(*) AS Nombre_ligne 
FROM orders
UNION ALL
SELECT 'order_items' AS Nom_table, COUNT(*) AS Nombre_ligne 
FROM order_items
UNION ALL
SELECT 'order_payments' AS Nom_table, COUNT(*) AS Nombre_ligne 
FROM order_payments
UNION ALL
SELECT 'order_reviews' AS Nom_table, COUNT(*) AS Nombre_ligne 
FROM order_reviews;
