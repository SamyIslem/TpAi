from aima.logic import *
from aima.utils import * 

KB = FolKB()

KB.tell(expr('Color(Blanc)'))
KB.tell(expr('Color(Bleu)'))
KB.tell(expr('Color(Vert)'))

KB.tell(expr('Sport(Football)'))
KB.tell(expr('Sport(Natation)'))
KB.tell(expr('Sport(Tennis)'))

KB.tell(expr('Emplacement(Debut)'))
KB.tell(expr('Emplacement(Milieu)'))
KB.tell(expr('Emplacement(Bout)'))