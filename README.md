###################
# Projet-Boulier-S2

# Auteurs (mettez vos noms j'ai peur de faire des fautes hein)
# Ana Wassaf
#
#
#

###################
import tkinter as tk 

# dimensions de base 

# fenêtre
HAUTEUR = 600
LARGEUR = 800

# cadre du boulier 
x0, y0 = 10, 10
x1, y1 = 795, 595

# 1° ligne 
xA, yA, xB, yB = 15, 50, 789, 50


###################
# fonctions 
def petit ():
    "affiche un boulier à 17 colonnes"
    canvas.config(height = 600, width = 800)
    cadre.config(x0 = 10, y0 = 10, x1 = 795, y1 = 595)
    ligne = canvas.create_line(xA = 15, yA = 50, xB = 789, yB = 50, width = 3, fill = '#F5F5DC')

def moyen () :
    "affiche un boulier à 21 colonnes"

def grand () :
    "affiche un boulier à 23 colonnes"


###################
# programme principal

# définition des widgets
racine = tk.Tk()
racine.title(' Boulier type "Soroban" ')
canvas = tk.Canvas(racine, height = HAUTEUR, width = LARGEUR, bg = 'black')
cadre = canvas.create_rectangle (x0, y0, x1, y1, width = 10, outline= 'maroon' )
ligne = canvas.create_line(xA, yA, xB, yB, width = 3, fill = '#F5F5DC')

# affichage du menu
frame = tk.Frame (racine, height = 50, width = 100, padx = 25, pady = 25)
OngletA = tk.Menubutton ( frame , text = "Nombres de colonnes" )
MNU_OptionA = tk.Menu ( OngletA )
MNU_OptionA.add_command ( label = "17 colonnes" , command = 'petit' )
MNU_OptionA.add_command ( label = "21 colonnes" , command = 'moyen' )
MNU_OptionA.add_command ( label = "23 colonnes" , command = 'grand' )
OngletA [ "menu" ] = MNU_OptionA

# placement des wdigets
frame.grid ( row = 0 , column = 0)
OngletA.grid ( row = 0 , column = 0 )
canvas.grid()

# boucle principale
racine.mainloop ( )
