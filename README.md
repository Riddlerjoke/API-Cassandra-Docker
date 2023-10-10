# Guide de configuration d'un cluster Cassandra à deux nœuds avec Docker et une API FastAPI

Ce guide explique comment configurer un cluster Cassandra à deux nœuds à l'aide de Docker et comment le connecter à une API FastAPI. Le cluster Cassandra contient deux nœuds, node1 et node2, pour la réplication des données. L'API FastAPI permet d'accéder et de manipuler les données stockées dans le cluster Cassandra.

## Configuration du projet

Le projet comprend les fichiers et dossiers suivants :

- `docker-compose.yaml`: Le fichier Docker Compose pour déployer le cluster Cassandra.
- `files-directory.py`: Un script Python pour gérer les fichiers dans le cluster.
- `main.py`: Le fichier principal de l'API FastAPI.
- `node1` et `node2`: Les répertoires contenant la configuration des nœuds Cassandra.
- `restaurants.csv` et `restaurants_inspections.csv`: Les fichiers de données pour le cluster Cassandra.
- `test_main v1.py`: Un script de test pour l'API FastAPI.
- `test_main.http`: Un fichier HTTP pour tester l'API à l'aide de l'extension REST Client de VSCode.
- `venv`: L'environnement virtuel Python (si utilisé).
- `__pycache__`: Dossiers de fichiers Python mis en cache.
- `.idea`: Répertoire de configuration pour l'IDE (peut être ignoré).

## Instructions d'installation

1. Assurez-vous d'avoir Docker installé sur votre système.

2. Clonez ce référentiel GitHub sur votre machine locale :

   ```bash
   git clone <URL_du_referentiel>
Accédez au répertoire du projet :

```
cd <nom_du_projet>
```
Démarrez le cluster Cassandra à l'aide de Docker Compose :
```
docker compose up -d
```
Configuration du cluster Cassandra
Étape 1 : Création des nœuds Cassandra
Pour créer les nœuds Cassandra, utilisez Docker Compose pour démarrer les conteneurs. Exécutez la commande suivante :


```
docker compose up -d
```
Étape 2 : Importation des données des restaurants
Connectez-vous au nœud Cassandra 1 en utilisant un shell Bash dans le conteneur :

```
docker exec -it cassandra1 /bin/bash
```
Connectez-vous à la base de données Cassandra en utilisant cqlsh.

Créez un nouveau keyspace appelé resto et définissez la réplication.

Utilisez le keyspace resto et créez les tables restaurant et inspection.

Créez des index sur les colonnes appropriées.

Étape 3 : Copie des fichiers de données dans le conteneur Docker
Copiez le fichier de données des restaurants dans le conteneur Cassandra 1 :


```
docker cp restaurants.csv cassandra1:/
```
Copiez le fichier de données des inspections dans le conteneur Cassandra 1 :

```
docker cp restaurants_inspections.csv cassandra1:/
```

Étape 4 : Importation des données dans la base de données Cassandra
Connectez-vous au nœud Cassandra 1 en utilisant un shell Bash dans le conteneur :

```
docker exec -it cassandra1 /bin/bash
```

Connectez-vous à la base de données Cassandra en utilisant cqlsh.

Utilisez le keyspace resto et copiez les données des restaurants dans la table restaurant.

Copiez les données des inspections dans la table inspection.

Étape 5 : Exécution de requêtes de base
Utilisez cqlsh pour exécuter des requêtes de base sur la base de données Cassandra.

Utilisation de l'API FastAPI
L'API FastAPI fournit des endpoints pour interagir avec le cluster Cassandra. Vous pouvez consulter la documentation de l'API à l'adresse http://localhost:8000/docs pour plus d'informations sur les endpoints disponibles et les requêtes acceptées.

N'hésitez pas à adapter ces étapes en fonction de votre configuration et de vos besoins spécifiques.

Nettoyage
Pour arrêter et supprimer le cluster Cassandra, exécutez la commande suivante dans le répertoire du projet :

```
docker compose down
```
Assurez-vous de toujours nettoyer le cluster après utilisation pour libérer les ressources Docker.

#voici les etapes pour la creation des cluster Cassandra dans Docker

Étape 2 : Importer les données des restaurants
```
# Créez un shell Bash dans le conteneur Cassandra.
docker exec -it cassandra1 /bin/bash

# Connectez-vous à la base de données Cassandra.
cqlsh

# Créez un keyspace `resto` avec réplication.
CREATE KEYSPACE IF NOT EXISTS resto WITH REPLICATION = {'class':'SimpleStrategy', 'replication_factor': 1};

# Utilisez le keyspace `resto`.
USE resto;

# Créez les tables `restaurant` et `inspection`.
CREATE TABLE IF NOT EXISTS restaurant (
  id int PRIMARY KEY,
  name varchar,
  borough varchar,
  buildingnum varchar,
  street varchar,
  zipcode int,
  phone text,
  cuisinetype varchar
);

CREATE TABLE IF NOT EXISTS inspection (
  idrestaurant int,
  inspectiondate date,
  violationcode varchar,
  violationdescription varchar,
  criticalflag varchar,
  score int,
  grade varchar,
  PRIMARY KEY (idrestaurant, inspectiondate)
);

# Créez des index sur les colonnes appropriées.
CREATE INDEX IF NOT EXISTS restaurant_cuisinetype_idx ON restaurant (cuisinetype);
CREATE INDEX IF NOT EXISTS inspection_grade_idx ON inspection (grade);
```

Étape 3 : Copier les fichiers de données dans le conteneur Docker
```
# Copiez le fichier de données des restaurants dans le conteneur Cassandra.
docker cp restaurants.csv cassandra1:/

# Copiez le fichier de données des inspections dans le conteneur Cassandra.
docker cp restaurants_inspections.csv cassandra1:/

```

Étape 4 : Importer les données dans la base de données Cassandra
```
# Connectez-vous à la base de données Cassandra.
docker exec -it cassandra1 cqlsh

# Utilisez le keyspace `resto`.
USE resto;

# Copiez les données des restaurants dans la table `restaurant`.
COPY restaurant (id, name, borough, buildingnum, street, zipcode, phone, cuisinetype) FROM '/restaurants.csv' WITH DELIMITER=',';

# Copiez les données des inspections dans la table `inspection`.
COPY inspection (idrestaurant, inspectiondate, violationcode, violationdescription, criticalflag, score, grade) FROM '/restaurants_inspections.csv' WITH DELIMITER=',';

```
Étape 5 : Exécutez quelques requêtes de base
```
# Sélectionnez seulement 1 entrée de la table restaurant.
SELECT * FROM restaurant LIMIT 1;

# Sélectionnez le nombre de restaurants dans la base de données.
SELECT COUNT(*) FROM restaurant;

# Sélectionnez le nombre d'inspections dans la base de données.
SELECT COUNT(*) FROM inspection;
```
Requêtes CQL supplémentaires
```
# Pour obtenir des informations sur un restaurant en fonction de son ID.
SELECT * FROM restaurant WHERE id = <restaurant_id>;

# Pour obtenir le nom des restaurants en fonction du type de cuisine.
SELECT name FROM restaurant WHERE cuisinetype = 'American';

# Pour obtenir une entrée aléatoire de la table restaurant.
SELECT * FROM restaurant LIMIT 1;

# Pour obtenir les ID des restaurants ayant une note 'A' dans les inspections (limité à 10 résultats).
SELECT idrestaurant FROM inspection WHERE grade = 'A' LIMIT 10;
```

N'hésitez pas à adapter ces étapes en fonction de votre configuration et de vos besoins spécifiques.
