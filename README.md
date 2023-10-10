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

Ceci conclut le guide d'installation et d'utilisation du cluster Cassandra à deux nœuds avec Docker et une API FastAPI. N'hésitez pas à contribuer ou à signaler des problèmes dans ce référentiel GitHub.
