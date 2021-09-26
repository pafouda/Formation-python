'''
*** Exo 5: flags => flagsBis ***
Créer un programme qui produira un dossier flagsBis
Ce dossier contiendra tous les fichier png d'origine mais
renommés en ne conservant que les deux premières lettres.
Ces lettres seront en masjuscule.
ex: 
  exos/flags/allemagne.png => exos/flagsBis/AL.png
  exos/flags/belgique.png => exos/flagsBis/BE.png
Le fichier missing.png devra être ignoré
'''
print("*** EXO 5: flags => flagsBis ***")

'''correction'''

import os, shutil

srcDir = "flags"
dstDir = "flagsBis"

if not os.path.exists(dstDir):
  os.mkdir(dstDir)
  print("Dossier %s créé" % dstDir)


for f in os.listdir(srcDir):
  if not f == "missing.png":
    shutil.copyfile(
      srcDir + "/" + f, 
      dstDir + "/" + f[:2].upper() + ".png"
    )
    print("Drapeau %s copié et renommé" % f)