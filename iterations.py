# une itération (boucle) consite à reproduire des instructions
# un certain nombres de fois

# affichage de "Bonjour" 5 fois. "Approche naïve"
# print ("Bonjour")
# print ("Bonjour")
# print ("Bonjour")
# print ("Bonjour")
# print ("Bonjour")

counter = 1
maxIteration = 6
while counter < 6:
    print("Bonjour", counter, "fois")
    # incrémentation du compteur (condition de sortie de boucle)
    counter += 1 # équivalent à: counter = counter + 1
    
    counter2 = 5
    while counter2 > 0:
        print("Au revoir")
    counter2 -= 1 # décrementation, équivalent à :counter = counter 
    

# boucle for..in
# boucle adaptée au parcourt de collection de données
# range renvoie ici un ensemble de 5 éléments
for i in range(5):
    print(i)
