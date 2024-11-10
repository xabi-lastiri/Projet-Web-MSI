# **Les dessins animés de notre enfance**

Ce projet de site internet présente nos dessins animés favoris d’enfance, en plusieurs langues (arabe, français et chinois).


## **Sites internet similaires**

Bien qu’il n’existe pas de plateformes spécifiquement dédiées à ce thème, certains articles de blog, publications sur les réseaux sociaux ou pages de sites centrées sur la cinématographie proposent des sélections de dessins animés pour susciter la nostalgie.

Quelques exemples :
- https://myanimelist.net/
- https://anilist.co/

### Myanimelist et Anilist

Ce sont des sites dynamiques : selon que l’utilisateur est authentifié ou non, le contenu des pages varie (titres recommandés, présentation de la page d'accueil, etc.).

Ils sont composés de codes HTML, CSS et JavaScript (pour les animations).

## Moodboard
![image](https://github.com/user-attachments/assets/ec1ec72d-056f-495c-aca8-9a410bff8d16)

_Source : moodboard généré à partir de nos réflexions via Dal-e._

## Palette de couleurs

![image](https://github.com/user-attachments/assets/d2573aca-1d5a-46f3-b1ec-8409b439be47)

## Police d'écriture

![image](https://github.com/user-attachments/assets/1c5d4363-9635-46e1-bee2-8fb1abc1722b)

_Source : Wikimedia Foundation_

## Open Data

Notre requête : https://recherche-entreprises.api.gouv.fr/search?activite_principale=59.11C&categorie_entreprise=GE&minimal=true&include=siege%2Ccomplements&page=1&per_page=25

Nous avons recherché une liste d'entreprises évoluant dans le secteur de la production audiovisuelle en France (A), et dans le monde (B).

### Entreprises françaises
Nous avons d'abord identifié le code NAF 5911C pour les entreprises produisant des films en France. Ensuite, nous avons ajusté la catégorie d'entreprise parmi GE, ETI et PME afin d'obtenir des résultats plus précis. Nous avons constaté qu'il existe plus de 7000 entreprises de type PME, 71 entreprises ETI et 23 entreprises GE. Nous avons choisi les grandes entreprises car elles représentent mieux l'industrie en France.

En important les données dans Flourish, un problème est apparu : seule l'année de création s’affichait correctement. Pour rendre le graphique plus intéressant, nous avons ajouté manuellement les coordonnées de latitude et de longitude. Finalement, nous avons obtenu un graphique de type Locator Map.

### Entreprises dans le monde
De plus, pour une vue d'ensemble mondiale, nous avons récupéré les informations sur les 10 plus grandes entreprises de dessins animés grâce à ChatGPT et créé un second Locator Map.

## Web Scraping
