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

_Source : moodboard généré via Dal-e à partir de nos réflexions._

## Palette de couleurs

![image](https://github.com/user-attachments/assets/d2573aca-1d5a-46f3-b1ec-8409b439be47)

_Palette générée via l'outil coolors._

## Police d'écriture

![image](https://github.com/user-attachments/assets/1c5d4363-9635-46e1-bee2-8fb1abc1722b)

_Source : Wikimedia Foundation_

Nous avons intégré la police Montserrat, téléchargée depuis Google Fonts, en tant que police personnalisée dans les fichiers du projet.

## Open Data

Notre requête : https://recherche-entreprises.api.gouv.fr/search?activite_principale=59.11C&categorie_entreprise=GE&minimal=true&include=siege%2Ccomplements&page=1&per_page=25

Nous avons recherché une liste d'entreprises spécialisées dans la production audiovisuelle, en France (A) et à l'international (B).

### Entreprises françaises

En France, nous avons d'abord identifié le code NAF 5911C pour les entreprises produisant des films, puis ajusté la catégorie d'entreprise entre GE, ETI et PME pour obtenir des résultats ciblés. Nous avons trouvé plus de 7000 entreprises PME, 71 ETI, et 23 grandes entreprises (GE). Nous avons retenu les grandes entreprises, car elles offrent une meilleure représentation de l'industrie nationale.

Lors de l’importation des données dans Flourish, un problème est survenu : seule l’année de création s’affichait correctement. Pour enrichir le graphique, nous avons ajouté manuellement les coordonnées de latitude et de longitude, ce qui nous a permis de créer un graphique de type Locator Map.

### Entreprises dans le monde

Pour une vue plus globale, nous avons également récupéré les informations des 10 plus grandes entreprises de dessins animés dans le monde, via ChatGPT, et créé un deuxième Locator Map.

## Web Scraping

Le script Python extrait la liste ordonnée des épisodes de la série Goldorak depuis la page https://fr.wikipedia.org/wiki/Goldorak et les enregistre dans un fichier CSV.