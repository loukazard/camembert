# Créé par louka, le 04/03/2022 en Python 3.7
import csv

mon_fichier2 = open(input("Nom du fichier csv"),encoding="utf8") #Demande à l'utilisateur dans quel fichier il veut travailler/ouvre le fichier csv
mon_tableau2 = list(csv.reader(mon_fichier2,delimiter=";"))


def colonne(categorie):
    nouvelle_ligne = []           #Création d'un tableau pour stocker les valeurs demandées
    for i in range(0, 16):       #Création d'une variable i qui se balade dans chaque colonne
        if mon_tableau2[5][i] == categorie:
            nouvelle_ligne.append(int(mon_tableau2[len(mon_tableau2)-1][i]))
            #Si le titre de la colonne correspond à la catégorie demandée alors
            #j'ajoute le total de la catégorie dans nouvelle_ligne

    return (sum(nouvelle_ligne)) #On renvoie la somme des valeurs du tablau nouvelle_ligne nouvelle ligne




import matplotlib.pyplot as plt #Importation de la bibliothèque matplotlib pour créer un graphique

noms = 'Essence', 'Diesel', 'Gaz'        #définition noms des parties du graphique
sizes = [colonne("Essence"), colonne("Diesel"), colonne("Gaz")]         #Définition tailles des parties
couleurs = ['lightskyblue', 'gold', 'red', ]        #définition de la couleur des parcelles du camembert


plt.pie(sizes, labels=noms, colors=couleurs,       #attribution de nos variantes en paramètres de la fonction
autopct='%1.1f%%', shadow=True, startangle=90)     #définition du type de graphique (ici un camembert car "pie") puis calcul pourcentage, ombres derrière et angle de départ

plt.savefig('PieChart01.png')  #sauveragrde le graphique au même endroit que le programme
plt.show()  #Permet d'afficher le graphique
