## Présentation du projet

Definir toutes les bases nécessaires pour une appi robuste avec python

## Idée
Après avoir eu quelques problèmes de déployement d'une api .net
 asp core sur un système linux, j'ai décidé de migrer totalement sur 
 python. 
Mon application necessitait beaucoup d'algorithme d'apprentissage 
automatique, malgré la puissance de la bibliothéque **Ml.net** pour
microsoft, j'ai pensé que python pouvais être la meilleure 
piste pour cette affaire


## Fonctionalités
- Envoie des mails
- Tests unitaires
- Crud avec sqalchemy
- Sécurité

## Caratéristique
- Utilise les bonnes pratiques du développement logiciel
- Injection des dépendances (DI)
- Migrations
- Base de données en mémoire pour les tests unitaire (sqlite)
- Séparation du code
- Bonne clarité
- Utilisation de jwt: gestions de l'authentification et l'authorisation
- Possibilité de changer l'environemment de développement en
utilisant simplement des commandes
- converage pour les tests

## Inconvenient
- Code non commenté
- Tous les tests non couvert
- l'absence des commits: Un peu difficile de comprendre tous 
les contours pour les développeur Junior

## Pourquoi tous ces inconvenients ?
En effet, à la base je voulais faire quelque chose de si vite et 
qui devait simplement me servir d'exemple pour mes  futures 
applications. Je n'avais en aucun moment pensé que je pouvais 
partager ce code. Mais quand je me rend compte en comparant
mon code à celui de plusieurs dev expérimentés python, j'ai
été convaincu que j'avais une excellente démarche pour 
des solutions flask. 
**Attention je n'ai pas dit la meilleur démarche
mais l'une des meilleures**

## Intégrer le projet 
Il y'a quelques étapes à faire avant de commencer à utiliser l'
application 
### Installations
- Clonnez l'application via la commande **git clone https://github.com/Stratege-takam/restapipythonwithflask.git**
- Installer les dépendances de l'application via la commande 
**pip install -r requirements.txt**
- Installer sqlite. vous pouvez suivre le lien **https://sqlitebrowser.org/**

### Base de données et serveur de mail
Dans le fichier app/config/config.json
- Adapter les paramètres du mail 
- Changer le repertoire racine de sqlite par le votre: Je vous 
donnerai une flexibilité pour ce changement ultérieurement
- Changer les paramètres de vos différents bd pour la prod et le dev: j'ai utilisé mysql
pour mon cas. Mais vous pouvez utiliser n'importe quel bd

### Migrations
- Changer l'environnement via les commandes respectives **python manage.py dev** ou  **python manage.py prod** 
pour le dev, prod
-  Mettre à jour la bd  via la commande
 **python manage.py db upgrade**

### Exécuter l'application
- Utilisez la commande **python manage.py run** pour démarrer l'application 

### test unitaire
- Utilisez la commande **python manage.py test** pour exécuter kes tests 

### utilitaires
Vous pouvez aussi tester l'application en utilisant nose2
- Utiliser la commande **nose2**
- Utiliser la commande  **#nose2 -v** pour plus de détail

#Couverture des tests
- Pour un fichier spécifique  la commande
**coverage run tests/modelsTest/test_student.py**
- Pour tout le projet **coverage report -m */*.py**
- Pour faire un rapport html **coverage html */*.py**




