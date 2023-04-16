#Il faut mettre un espace entre chque nombre et opérateur.
#Le bouton notation permet de passer de l'écriture polonaise inversé à l'écriture polonaise et inversement.

from Pile import Pile_lst as Pile
from tkinter import *
class Expression:
    def __init__(self, val, gauche, droit):
        self.val = val
        self.gauche = gauche
        self.droite = droit

    def evalue(self):
        if self.val == "+":
            return self.gauche.evalue() + self.droite.evalue()
        elif self.val == "-":
            return self.gauche.evalue() - self.droite.evalue()
        elif self.val == "*":
            return self.gauche.evalue() * self.droite.evalue()
        elif self.val == "/":
            return self.gauche.evalue() / self.droite.evalue()
        elif self.val == "^":
            return self.gauche.evalue() ** self.droite.evalue()
        else:
            return int(self.val)

    def __str__(self):
        if type(self.val) == int:
            return str(self.val)
        return "(" + str(self.gauche.__str__()) + str(self.val) + str(self.droite.__str__()) + ")"

class Calcul:
    def __init__(self, ch):
        self.ch = ch
        self.type_notation = "polonaise inversée"
        
    def ajout(self, val):
        self.ch += val
        expression['text'] = self.ch
        
    def retour(self):
        self.ch = self.ch[:-1]
        expression['text'] = self.ch
        
    def effacer(self):
        self.ch = ""
        expression['text'] = ""
        
    def notation(self):
        if self.type_notation == "polonaise inversée":
            self.type_notation = "polonaise"
        elif self.type_notation == "polonaise":
            self.type_notation = "polonaise inversée"
        b_type['text'] = "Notation : " + self.type_notation
    

def npi2tree(lst):
    pile = Pile()
    for i in range(len(lst)):
        if lst[i] == "+" or lst[i] == "-" or lst[i] == "*" or lst[i] == "/" or lst[i] == "^":
            s = pile.depiler()
            pile.empiler(Expression(lst[i], pile.depiler(), s))
        else:
            pile.empiler(Expression(lst[i],None,None))
    return pile.sommet()

def np2tree(lst):
    pile = Pile()
    for i in range(len(lst)):
        n=len(lst)-i-1
        if lst[n] == "+" or lst[n] == "-" or lst[n] == "*" or lst[n] == "/" or lst[n] == "^":
            s = pile.depiler()
            pile.empiler(Expression(lst[n], pile.depiler(), s))
        else:
            pile.empiler(Expression(lst[n],None,None))
    return pile.sommet()

def calculer():
    lst = calcul.ch.split()
    if calcul.type_notation == "polonaise inversée":
        exp = npi2tree(lst)
    elif calcul.type_notation == "polonaise":
        exp = np2tree(lst)
    res = exp.evalue()
    resultat['text'] = str(res) 
    
calcul= Calcul("")
fenetre=Tk()
fenetre.title("Calculatrice")

expression = Label(fenetre, text="")
expression.grid(row=0,column=0, columnspan=5)
resultat = Label(fenetre, text="")
resultat.grid(row=1,column=0, columnspan=5)

b1 = Button(fenetre, text ="1", command = lambda: calcul.ajout("1"))
b1.grid(row=4, column=0)
b2 = Button(fenetre, text ="2", command = lambda: calcul.ajout("2"))
b2.grid(row=4, column=1)
b3 = Button(fenetre, text ="3", command = lambda: calcul.ajout("3"))
b3.grid(row=4, column=2)
b4 = Button(fenetre, text ="4", command = lambda: calcul.ajout("4"))
b4.grid(row=3, column=0)
b5 = Button(fenetre, text ="5", command = lambda: calcul.ajout("5"))
b5.grid(row=3, column=1)
b6 = Button(fenetre, text ="6", command = lambda: calcul.ajout("6"))
b6.grid(row=3, column=2)
b7 = Button(fenetre, text ="7", command = lambda: calcul.ajout("7"))
b7.grid(row=2, column=0)
b8 = Button(fenetre, text ="8", command = lambda: calcul.ajout("8"))
b8.grid(row=2, column=1)
b9 = Button(fenetre, text ="9", command = lambda: calcul.ajout("9"))
b9.grid(row=2, column=2)
b0 = Button(fenetre, text ="0", command = lambda: calcul.ajout("0"))
b0.grid(row=5, column=1)
b_virgule = Button(fenetre, text =",", command = lambda: calcul.ajout("."))
b_virgule.grid(row=5, column=0)
b_plus = Button(fenetre, text ="+", command = lambda: calcul.ajout("+"))
b_plus.grid(row=3, column=3)
b_moins = Button(fenetre, text ="-", command = lambda: calcul.ajout("-"))
b_moins.grid(row=3, column=4)
b_fois = Button(fenetre, text ="x", command = lambda: calcul.ajout("*"))
b_fois.grid(row=4, column=3)
b_divise = Button(fenetre, text ="/", command = lambda: calcul.ajout("/"))
b_divise.grid(row=4, column=4)
b_puissance = Button(fenetre, text ="^", command = lambda: calcul.ajout("^"))
b_puissance.grid(row=5, column=4)


b_retour = Button(fenetre, text ="Retour", command = lambda: calcul.retour())
b_retour.grid(row=6, column=1)
b_effacer = Button(fenetre, text ="Effacer", command = lambda: calcul.effacer())
b_effacer.grid(row=6, column=2)
b_resultat = Button(fenetre, text ="Résultat", command = lambda: calculer())
b_resultat.grid(row=6, column=4)
b_type = Button(fenetre, text ="Notation: polonaise inversée", command = lambda: calcul.notation())
b_type.grid(row=2, column=3, columnspan=2)
b_espace = Button(fenetre, text ="Espace", command = lambda: calcul.ajout(" "))
b_espace.grid(row=6, column=3)
b_quitter = Button(fenetre, text ="Quitter", command = lambda: fenetre.destroy())
b_quitter.grid(row=6, column=0)