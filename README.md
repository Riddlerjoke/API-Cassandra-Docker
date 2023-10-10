#Guide de configuration d'un cluster Cassandra à deux nœuds avec Docker et une API FastAPI


Ce guide explique comment configurer un cluster Cassandra à deux nœuds à l'aide de Docker et comment le connecter à une API FastAPI. Le cluster Cassandra contient deux nœuds, node1 et node2, pour la réplication des données. L'API FastAPI permet d'accéder et de manipuler les données stockées dans le cluster Cassandra.

Configuration du projet
Le projet comprend les fichiers et dossiers suivants :

docker-compose.yaml: Le fichier Docker Compose pour déployer le cluster Cassandra.
files-directory.py: Un script Python pour gérer les fichiers dans le cluster.
main.py: Le fichier principal de l'API FastAPI.
node1 et node2: Les répertoires contenant la configuration des nœuds Cassandra.
restaurants.csv et restaurants_inspections.csv: Les fichiers de données pour le cluster Cassandra.
test_main v1.py: Un script de test pour l'API FastAPI.
test_main.http: Un fichier HTTP pour tester l'API à l'aide de l'extension REST Client de VSCode.
Instructions d'installation
Assurez-vous d'avoir Docker installé sur votre système.

Clonez ce référentiel GitHub sur votre machine locale :

bash
Copy code
git clone <URL_du_referentiel>
Accédez au répertoire du projet :

bash
Copy code
cd <nom_du_projet>
Démarrez le cluster Cassandra à l'aide de Docker Compose :

bash
Copy code
docker-compose up -d
Créez un environnement virtuel (si nécessaire) et installez les dépendances Python :

bash
Copy code
python -m venv venv
source venv/bin/activate  # Sur Windows, utilisez venv\Scripts\activate
pip install -r requirements.txt
Lancez l'API FastAPI :

bash
Copy code
python main.py
Vous pouvez maintenant accéder à l'API FastAPI à l'adresse http://localhost:8000 dans votre navigateur ou via des requêtes HTTP.

Utilisation de l'API FastAPI
L'API FastAPI fournit des endpoints pour interagir avec le cluster Cassandra. Vous pouvez consulter la documentation de l'API à l'adresse http://localhost:8000/docs pour plus d'informations sur les endpoints disponibles et les requêtes acceptées.

Nettoyage
Pour arrêter et supprimer le cluster Cassandra, exécutez la commande suivante dans le répertoire du projet :

bash
Copy code
docker-compose down
Assurez-vous de toujours nettoyer le cluster après utilisation pour libérer les ressources Docker.

Ceci conclut le guide d'installation et d'utilisation du cluster Cassandra à deux nœuds avec Docker et une API FastAPI. N'hésitez pas à contribuer ou à signaler des problèmes dans ce référentiel GitHub.
