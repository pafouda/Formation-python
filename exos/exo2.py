'''
*** Exo 2 ***
Ecrire un programme python qui propose à l'utilisateur
de deviner un nombre caché (exemple: 42) et
affichera en fonction de la réponse de l'utilisateur:
 - "c'est plus" si le nombre saisi est inférieur au nombre caché
 - "c'est moins" si le nombre saisi est supérieur au nombre caché
Tant que l'utilisateur n'a pas trouvé le nombre caché
on lui demande la saisie
'''
print("*** EXO 2: chiffre mystère à deviner --- version 2 --- ***")
guessNumber = 42

# Votre code ici

while True:

    playerInput = int(input("Deviner le nombre caché: "))

    if playerInput > guessNumber:
        print("c'est moins!")
    elif playerInput < guessNumber:
        print("c'est plus!")
    else:
        print("Nombre caché trouvé!") 
        break

'''
correction
inputNumber = int(input("Devine le chiffre mystère: "))

while inputNumber != guessNumber:
  if inputNumber > guessNumber:
    print("C'est moins !")
  else:
    print("C'est plus !")
  inputNumber = int(input("Devine le chiffre mystère: "))

print("Bravo !")
'''
