from tkinter import *
from random import randrange
from copy import deepcopy
from time import time

class ForestFire(Canvas):


    def __init__(self,boss =None, cote =30, arbreFeu =5, timeTick =100, densite =5):	#constructeur

        Canvas.__init__(self)

        self.cote =cote          #nombre de case d'un coté du carré
        cellSize =10
        self.timeTick =timeTick

        self.config(width =cellSize*self.cote, height =cellSize*self.cote)

        #variable d'état des cellules
        self.rien =0
        self.cendre =1
        self.brule =2
        self.vivant =3

        #Création des espaces de stockage
        self.cell =[ [0 for row in range(self.cote)] for col in range(self.cote) ]   #stockage des cellules
        self.etat =[ [self.rien for row in range(self.cote)] for col in range(self.cote)] #stockage des états des cellules à l'état t
        self.temp =[ [self.rien for row in range(self.cote)] for col in range(self.cote)] #stockage des états des cellules a l'état t+1
        self.brulePoint =[]
        self.cendrePoint =[]

        print(len(self.cell[0]))

        #initialisation des tableau
        for y in range(self.cote):
            for x in range(self.cote):
                self.etat[x][y] =self.rien
                self.temp[x][y] =self.rien
                self.cell[x][y] =self.create_rectangle((x*cellSize, y*cellSize, (x+1)*cellSize, (y+1)*cellSize), 
                                                        outline ='black', fill ='white')


        #création de la foret
        for i in range(cote*cote//1):
            x =randrange(cote)
            y =randrange(cote)
            self.etat[x][y] =self.vivant
            self.temp[x][y] =self.vivant

        #création des arbres qui brule
        for i in range(arbreFeu):
            x =randrange(cote)
            y =randrange(cote)
            self.etat[x][y] =self.brule
            self.temp[x][y] =self.brule

            self.brulePoint.append([x, y])
                    
        self.dessin()

        


    def dessin(self): #fonction qui dessine la grille
        for y in range(self.cote):
            for x in range(self.cote):
                if self.etat[x][y] == self.vivant:
                    coul ="green"
                elif self.etat[x][y] == self.brule:
                    coul ="red"
                elif self.etat[x][y] == self.cendre:
                    coul ="grey"
                else:
                    coul ="white"
                self.itemconfig(self.cell[x][y], fill =coul)
        
    def calculer(self):

            #print(len(self.bruleX), len(self.bruleY))

            l =[]
            bru =deepcopy(self.brulePoint)
            cen =deepcopy(self.cendrePoint)

            for xy in cen:
            
                x =xy[0]
                y =xy[1]

                self.etat[x][y] =self.rien

                self.cendrePoint.remove(xy)

            
                self.itemconfig(self.cell[x][y], fill ='white')
        
            for xy in bru:

                    x =xy[0]
                    y =xy[1]
                
                    self.etat[x][y] =self.cendre

                    self.cendrePoint.append([x, y])

                
                    self.itemconfig(self.cell[x][y], fill ='grey')

                    self.entoure2(x, y)

                
                    self.brulePoint.remove(xy)
                    #if self.etat[x][y] == self.brule:

    def entoure2(self, x, y):

            if y+1<self.cote:
                if x-1>=0:
                    if self.etat[x-1][y+1] == self.vivant:

                        self.etat[x-1][y+1] =self.brule

                        self.brulePoint.append([x-1, y+1])

                    
                        self.itemconfig(self.cell[x-1][y+1], fill ='red')
                    
                    else:
                        None
                if x+1<self.cote:
                    if self.etat[x+1][y+1] == self.vivant:

                        self.etat[x+1][y+1] =self.brule

                        self.brulePoint.append([x+1, y+1])

                        self.itemconfig(self.cell[x+1][y+1], fill ='red')

                    else:
                        None

                if self.etat[x][y+1] == self.vivant:

                    self.etat[x][y+1] =self.brule

                    self.brulePoint.append([x, y+1])

                    self.itemconfig(self.cell[x][y+1], fill ='red')

                else:
                    None

            if y-1>=0:
                if x-1>=0:
                    if self.etat[x-1][y-1] == self.vivant:

                        self.etat[x-1][y-1] =self.brule

                        self.brulePoint.append([x-1, y-1])

                        self.itemconfig(self.cell[x-1][y-1], fill ='red')

                    else:
                        None
                if x+1<self.cote:
                    if self.etat[x+1][y-1] == self.vivant:

                        self.etat[x+1][y-1] =self.brule

                        self.brulePoint.append([x+1, y-1])

                        self.itemconfig(self.cell[x+1][y-1], fill ='red')

                    else:
                        None

                if self.etat[x][y-1] == self.vivant:

                    self.etat[x][y-1] =self.brule

                    self.brulePoint.append([x, y-1])

                    self.itemconfig(self.cell[x][y-1], fill ='red')
                
                else:
                    None


            if x-1>=0:
                if self.etat[x-1][y] == self.vivant:

                    self.etat[x-1][y] =self.brule

                    self.brulePoint.append([x-1, y])

                    self.itemconfig(self.cell[x-1][y], fill ='red')

                else:
                    None
            if x+1<self.cote:
                if self.etat[x+1][y] == self.vivant:
                    self.etat[x+1][y] =self.brule

                    self.brulePoint.append([x+1, y])

                    self.itemconfig(self.cell[x+1][y], fill ='red')
                else:
                    None

    def move(self): #mise à jour du tableau suivant
        self.calculer() #calcul du nouveau tableau
        #self.dessin() #dessin du tableau
        self.after(self.timeTick, self.move) 

if __name__ == '__main__':
    print("entré")
    fen =Tk()
    can =Canvas(fen)
    auto =ForestFire(boss =can, cote =80)
    auto.pack()
    auto.move()
    fen.mainloop()