# Fullstack_Projet

## Introduction ##

Les bases de données de films du type IMDB ou METACRITIC sont assez connus.
Ils permettent à tout et chacun d'avoir le maximum d'information sur un film désiré.
Notre projet a donc eu comme objectif de récupérer le maximum d'information de différents sites de base de données de films(IMDB, SENSCRITIQUE) pour ensuite construire des fiches de film les plus complètes possibles. Et puis, en comparant les différentes notes des différents sites, nous avons pu dresser des moyennes de films plus "complètes" pour guider au mieux l'utilisateur. Nous avons tenté de réaliser notre code sous python Flask (Backend) et React (Frontend), malheureusement, nous n'avions pas pu achever notre partie front sur ReactJs, c'est pourquoi le guide suivant ne s'appuie que sur les résultats obtenues à partir de Flask Python. 

## Guide Utilisateur ##

Le Lancement du dashboard

Le lancement du dashboard se fait avec l'instruction : python main.py.
(Parfois la page d'acceuil ne marche pas, il faut juste l'actualiser et le dashboard remarche, une erreur que nous n'avons pas réussi à résoudre et que nous ne comprenons pas)

## Description du Dashboard ##

Au lancement de l'API, l'utilisateur se trouve sur une page d'accueil composée d'une affiche de film choisie aléatoirement sur la base de donnée puis juste en dessous différente liste de films, une concernant les plus gros box office, une autre sur les meilleurs films entre 2013 et 2019 puis une dernière sur les films des meilleurs réalisateurs sur la même période

### Accueil ### 

<img src="capture/HOME.PNG" width="600"> \ 

### BOX OFFICE ###

<img src="capture/BOX_OFFICE.PNG" width="600"> \

### TOP 50 ###

<img src="capture/TOP_50.PNG" width="600"> \

### FILM DES MEILLEURS REALISATEURS ###

<img src="capture/Meilleur_Realisateur.PNG" width="600"> \

Il est également possible de sélectionner le genre de film pour pouvoir ensuite consulter les meilleures références cinématographiques de ce dernier

### Theme ###

<img src="capture/Exemple_Theme.PNG" width="600"> \

En cliquant sur l'affiche d'un film, on peut consulter sa fiche complète comprenant toutes les informations scrapées 

### Fiche Film ###

<img src="./capture/Fiche_Film.PNG" width="600"> \

## Difficulté avec React ##

Alors que nous comptions dans un premier temps, obtenir les données via notre api flask puis les afficher via React, nous n'avons malheureusement pas pu concevoir notre Front comme convenu pour une utilisation optimale des données. Nous n'avons réussi qu'à en implémenter un affichage Home. 

<img src="./capture/accueil_React.PNG" width="600"> \
