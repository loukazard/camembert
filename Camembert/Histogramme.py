# Créé par louka, le 04/03/2022 en Python 3.7

import csv #importation de la bibliothèque csv pour lire les fichiers csv

liste_fichiers=["auvergne_rhone_alpes.csv", "bourgogne_franche_comte.csv", "bretagne.csv", "centre_val_de_loire.csv", "hauts_de_france.csv", "corse.csv", "grand_est.csv", "normandie.csv",
"nouvelle_aquitaine.csv", "occitanie.csv", "pays_de_la_loire.csv", "provence_alpes_cotes_dazur.csv"]
giga_liste=[] #contiendra tous les fichiers csv



for i in liste_fichiers:

    mon_fichier = open(i,encoding="utf8")
    giga_liste.append(list(csv.reader(mon_fichier, delimiter=";"))) #liste qui contienent tous les fichiers csv
    totaux = [int(giga_liste[i][len(giga_liste[i])-1][len(giga_liste[i][1])-1]) for i in range(len(giga_liste))] #liste du nombre de voitures total (fichier i, dernière ligne, dernière case)

import matplotlib.pyplot as plt #importation bibliothèque matplotlib pour créer un graphique



names = ['ARA', 'BFC', 'Bretagne', 'CVL', 'Hauts-De-France', "Corse", "Grand-Est", "Normandie", "NA",
"Occitanie", "Pays-De-La-Loire", "PACA"]    #noms donnés au parties du graphiques

for i in range(1, len(totaux)):  #tri des valeurs par insertion

    j = i

    while j != 0 and totaux[j] < totaux[j-1]:
        totaux[j], totaux[j-1] = totaux[j-1], totaux[j]   #tri par insertion plus rangement des régions par ordre croissant dans l'histogramme
        names[j], names[j-1] = names[j-1], names[j]
        j = j-1

plt.figure(figsize=(50, 3)) #taille de l'histogramme
plt.title("Histogramme du total de voitures dans chaque régions de France") #titre du graphique
plt.bar(names, totaux, width=0.8) #fonction pour créer les barres de l'histogramme
plt.show() #montrer l'histogramme
