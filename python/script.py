import requests as rq
from bs4 import BeautifulSoup as bs
import csv

# Étape 0 : créer le dictionnaire de données et le compteur d'épisodes
liste_episodes = {}
compteur = 0

# Étape 1 : récupérer le contenu de la page
url = "https://fr.wikipedia.org/wiki/Goldorak"
contenu = rq.get(url).text
soup = bs(contenu, "html.parser")

# Étape 2 : récupérer les divisions contenant les épisodes (une division = une saison)
saisons = soup.find_all('div', class_= "colonnes")

# Étape 3 : récuperer la liste des épisodes dans chaque division (une division = une saison) et les enregistrer dans le dictionnaire
for saison in saisons:
    titres_episode = saison.find_all('i')
    for titre_episode in titres_episode:
        compteur += 1
        numero_episode = "Episode " + str(compteur)
        liste_episodes[numero_episode] = titre_episode.text

# Étape 4 : exporter la liste des épisodes dans un fichier csv
with open('episodes_goldorak.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["Numéro de l'épisode", "Titre de l'épisode"])
    for numero_episode, titre_episode in liste_episodes.items():
        writer.writerow([numero_episode, titre_episode])