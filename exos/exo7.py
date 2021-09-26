'''
*** EXO 7: CSV De Niro ***
Créer un programme qui, à partir du fichier deniro.csv,
produira en sortie un fichier deniro-report.txt" 
affichant les informations suivantes:
Nom du film le mieux noté
Nombre de films entre 2000 et 2010
'''
print("*** EXO 7: CSV De Niro ***")

''' Votre code ici

import csv
import numpy as np # package de calcul numérique, retourne la valeur la plus élevée

with open("deniro.csv", "r") as csvFile:
    rows = csv.reader(csvFile, delimiter = ",")
    film = []
    score = []
    annee = []
    for i, r in enumerate(rows): # i pour index ligne
        if i > 0:
            score.append(int(r[1]))
            film.append(r[2])
meilleurIndexScore = np.argmax(score) # téléchargé (pip install numpy), argmax montre la plus grande valeur
nomMeilleurfilm = film[meilleurIndexScore]
#print(nomMeilleurfilm)

with open("deniro-report.txt", "w") as txtFile:
    txtFile.write(nomMeilleurfilm)
'''


#correction
   
import csv

with open("deniro.csv", "r") as csvFile :
    rows = csv.reader(csvFile, delimiter=",")
    next(rows, None) # ignore la ligne d'entêtes
    bestScore = 0
    numMovies = 0
    bestMovieTitle = ""
    for r in rows :
      year = int(r[0].strip())
      score = int(r[1].strip())
      title = r[2].strip().strip("\"")
      if score > bestScore:
        bestScore = score
        bestMovieTitle = title
      if year > 1999 and year < 2011:
        numMovies += 1

with open("deniroReport.txt", "w") as txtFile :
  txtFile.write(f"Le titre du film ayant obtenu le meilleur score est {bestMovieTitle}.\nEntre 2000 et 2010 Deniro a joué dans {numMovies} films")

