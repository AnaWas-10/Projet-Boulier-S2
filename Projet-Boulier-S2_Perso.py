###########################
# Auteur : Ana Wassaf
###########################

import tkinter as tk 

# paramètres du boulier
n = 17
r_boule = 50
# dimensions du canevas
HAUTEUR = 600
LARGEUR = r_boule * n + 115
# coordonnées barre médiane
xA, yA, xB, yB = 10, 120, r_boule * 17 + 115, 120
# dimension cadre
xCadre, yCadre, x1Cadre, y1Cadre = 10, 10, r_boule * 17 + 115, 600
# dimension lignes
xTige1, yTige1, x1Tige1, y1Tige1 = 45, 12, 45, HAUTEUR-10
xTige2, yTige2, x1Tige2, y1Tige2 = 100, 12, 100, HAUTEUR-10
# dimension boules
xBoule1, yBoule1, x1Boule1, y1Boule1 = 20, HAUTEUR-5, 70, HAUTEUR-55
xBoule6, yBoule6, x1Boule6, y1Boule6 = 20 , 10, 70, 60

########## fonctions ##########
# variable globale
boule={}

# MODE SIMULATION

def init_boulier():
    """affiche un boulier avec les boules désactivées"""
    canvas.delete()
    for i in range(n):
            canvas.create_line(xTige1 + i*55, yTige1, x1Tige1+ i*55, y1Tige1, fill = '#F5F5DC', width = 3, tags="tiges" )
            liste1 = []
            for a in range(5):
                x0,y0,x1,y1= xBoule1 + i*55, yBoule6, x1Boule1 + i*55, y1Boule6
                canvas.create_oval(xBoule1 + i*55, yBoule1-a*55, x1Boule1 + i*55, y1Boule1-a*55, fill = 'black')
                liste1.append(canvas.create_oval( x0,y0,x1,y1, fill = 'black')) 
    canvas.create_rectangle (xCadre, yCadre, 20+n*55, y1Cadre, width = 6, outline = 'maroon', tags = "cadre")
    canvas.create_line(xA, yA, 20+n*55, yB, fill = 'maroon', width = '10', tags="cadre")               


def affiche_boulier(n) :
    """affiche un boulier avec la dimension à la demande de l'utilisateur
    et création d'un dictionnaire de boules"""

    global boule
    gestion(n)
    
    n = int(input("choisir la dimension du boulier"))
    da=(17,21,23)
    if n in da :

    # matrice faisant apparaitre le nombre de tiges et de boules à la demande de l'utilisateur
        for i in range(n): 
            liste1 = []
            canvas.create_line(xTige1 + i*55, yTige1, x1Tige1+ i*55, y1Tige1, fill = '#F5F5DC', width = 3, tags="tiges" )
            for a in range(5):
                x0,y0,x1,y1= xBoule1 + i*55, yBoule1-a*55, x1Boule1 + i*55, y1Boule1-a*55
                tag=str(i+1)+"00"+str(a+1)
                liste1.append(canvas.create_oval( x0,y0,x1,y1, fill = 'black', tags=tag))
                boule[f"{xBoule1 + i*55},{yBoule1-a*55},{x1Boule1 + i*55},{y1Boule1-a*55}"]=[tag]

            x0,y0,x1,y1= xBoule1 + i*55, yBoule6, x1Boule1 + i*55, y1Boule6
            tag=str(i+1)+"00"+str("e")
            liste1.append(canvas.create_oval( xBoule1 + i*55, yBoule6, x1Boule1 + i*55, y1Boule6, fill = 'black', tags=str(i+1)+"00"+"e" ))
            boule[f"{xBoule1 + i*55},{yBoule6},{x1Boule1 + i*55},{y1Boule6}"]=[tag]

        canvas.config(height = HAUTEUR, width = 70+n*55)
        canvas.itemconfigure(tagOrId='cadre', fill= "white") 
        canvas.create_rectangle (xCadre, yCadre, 20+n*55, y1Cadre, width = 6, outline = 'maroon', tags = "cadre")
        canvas.create_line(xA, yA, 20+n*55, yB, fill = 'maroon', width = '10', tags="cadre")        


def gestion(n):
    """le dictionnaire de boule"""
    global boule
    for i in range(n):
        for a in range(11):
            boule[f"{xBoule1 + i*55},{yBoule1-a*55},{x1Boule1 + i*55},{y1Boule1-a*55}"]=[None]


def ev_boules(e) : 
    """active les boules quand on clique dedans"""
    global z_texte,n,boule
    px, py =e.x, e.y
    a,b=0,0
    if px < 20+int(z_texte.get("1.0", "end"))*55:
        a=int((px//55)*55+20)
        b=int((py//55+1)*55-10)
        if boule[f"{a},{b},{a+50},{b-50}"] != None:
            ahhhhhhhhhh()


def ahhhhhhhhhh():
    """movement de chaque balle"""
    """je recherche encore, preneuse de conseils"""
    pass


def ohhhhhh():
    """calcul l'ensemble des balle impliquer dans le mouvement et les change de couleur avec ehhhhhhhhhhhhhhhhhhhhhh()"""
    """je recherche encore, preneuse de conseils"""
    pass


def ehhhhhhhhhhhhhhhhhhhhhh():
    """"change de couleur les balles et les fait bouger"""  
    pass

def sauvegarde():
    """ Ecrit les coordonnées de chaque boule et le nombre de tiges
        dans le fichier simulation_boulier.txt
    """
    fic = open("simulation_boulier2.txt", "w")
    fic.write(str(f"{xBoule1 + i*55},{yBoule1-a*55},{x1Boule1 + i*55},{y1Boule1-a*55}"))
    for i in range(n):
        for a in range(11):
            boule[f"{xBoule1 + i*55},{yBoule1-a*55},{x1Boule1 + i*55},{y1Boule1-a*55}"]
    fic.close()    


def load():
    """Lit le fichier simulation_boulier.txt et met à jour les variables
     N et terrain en conséquence, et modifie l'affichage
    """
    fic = open("simulation_boulier2.txt", "r")
    ligne = fic.readline()
    init_boulier()
    for ligne in fic: 
        n = int(ligne)
        for i in range(n):
            fic.write(str(canvas.create_line(xTige1 + i*55, yTige1, x1Tige1+ i*55, y1Tige1, fill = '#F5F5DC', width = 3, tags="tiges" )))
            for a in range(5):
                fic.write((boule[f"{xBoule1 + i*55},{yBoule1-a*55},{x1Boule1 + i*55},{y1Boule1-a*55}"]) + "\n")
        pass
    fic.close()
    affiche_boulier()

# MODE OPÉRATION
def calcul_e():
    "affiche les étapes des opérations"

########## affichage de base ##########
racine = tk.Tk()
racine.title(' Boulier type "Soroban" ')
canvas = tk.Canvas(racine, height = HAUTEUR, width = LARGEUR, bg = 'white')
racine.bind("<Button-1>", ev_boules)
# pour changer la dimension du boulie
z_texte = tk.Text(racine, width = 10, height = 3 )
z_texte.bind("Enter", ahhhhhhhhhh())
res = tk.Button(racine, text = "reset", command = init_boulier())
# positionnement des widgets
canvas.grid(rowspan= 10, column = 2, row = 0)
z_texte.grid(row = 0)
res.grid(row = 7)
racine.mainloop()