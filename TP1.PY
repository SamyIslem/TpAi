from aima.logic import *
from aima.utils import *


KB = FolKB()

KB.tell(expr('Homme(Jean)'))
KB.tell(expr('Homme(Franck)'))
KB.tell(expr('Homme(Fabien)'))
KB.tell(expr('Homme(Jerome)'))
KB.tell(expr('Homme(Bruno)'))

KB.tell(expr('Femme(Louise)'))
KB.tell(expr('Femme(Eve)'))
KB.tell(expr('Femme(Marie)'))
KB.tell(expr('Femme(Evelyne)'))
KB.tell(expr('Femme(Sophie)'))

KB.tell(expr('Parent(Jean,Fabien)'))
KB.tell(expr('Parent(Fabien,Louise)'))
KB.tell(expr('Parent(Louise,Jerome)'))
KB.tell(expr('Parent(Louise,Sophie)'))
KB.tell(expr('Parent(Louise,Marie)'))
KB.tell(expr('Parent(Jerome,Franck)'))
KB.tell(expr('Parent(Sophie,Bruno)'))
KB.tell(expr('Parent(Sophie,Marie)'))
KB.tell(expr('Parent(Sophie,Eve)'))

KB.tell(expr('Parent(x,y) & Femme(x) ==> Mere(x,y)'))
KB.tell(expr('Parent(x,y) & Homme(x) ==> Pere(x,y)'))
KB.tell(expr('Parent(z,x) & Parent(z,y) ==> FrereSoeur(x,y) '))
# M1: 
KB.tell(expr('Parent(z,x) & Parent(z,y) & Homme(x) ==> Frere(x,y) '))
# M2:
KB.tell(expr('FrereSoeur(x,y) & Homme(x) ==> Frere(x,y) '))
KB.tell(expr('FrereSoeur(x,y) & Femme(x) ==> Soeur(x,y) '))

# Oncle :
KB.tell(expr('Parent(z,y) & Frere(x,z) ==> Oncle(x,y)'))
KB.tell(expr('Parent(z,y) & Soeur(x,z) ==> Tante(x,y)'))

# cousin: 
KB.tell(expr("Parent(z,y) & FrereSoeur(i,z) & Parent(x,i)  ==> Cousin(x,y)"))

#Ancetre :
KB.tell(expr('Parent(x,y)==> Ancetre(x,y)'))
KB.tell(expr('Parent(z,y) & Ancetre(x,z) ==> Ancetre(x,y)'))

a=KB.ask(expr('Mere(Louise,Jerome)'))
b=KB.ask(expr('Ancetre(Jean,Franck)'))

print(b)


# ----exo 2 :------




