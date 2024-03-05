from aima.logic import *
from aima.utils import *


KB = FolKB()

KB.tell(expr('Adjacent(f1, f2)'))
KB.tell(expr('Adjacent(f1, f3)'))
KB.tell(expr('Adjacent(f1, f5)'))
KB.tell(expr('Adjacent(f1, f6)'))

KB.tell(expr('Adjacent(f5,f6)'))
KB.tell(expr('Adjacent(f5,f2)'))

KB.tell(expr('Adjacent(f2,f4)'))
KB.tell(expr('Adjacent(f2,f3)'))
KB.tell(expr('Adjacent(f2,f6)'))

KB.tell(expr('Adjacent(f4,f3)'))

KB.tell(expr('Adjacent(f6,f3)'))


KB.tell(expr('Adjacent(x,y)'))
KB.tell(expr('Adjacent(x,y) ==> Adjacent(y,x) '))

KB.tell(expr('Color(Blue)'))
KB.tell(expr('Color(Green)'))
KB.tell(expr('Color(White)'))
KB.tell(expr('Color(Black)'))



KB.tell(expr('Diffcolor(Blue,Black)'))
KB.tell(expr('Diffcolor(Blue,White)'))
KB.tell(expr('Diffcolor(Blue,Green)'))
KB.tell(expr('Diffcolor(White,Green)'))
KB.tell(expr('Diffcolor(Black,Green)'))
KB.tell(expr('Diffcolor(White,Green)'))
KB.tell(expr('Diffcolor(White,Black)'))

KB.tell(expr('Diffcolor(x,y) ==> Diffcolor(y,x)'))

KB.tell(expr('Adjacent(x,y) ==> Diff(x,y) '))
KB.tell(expr('Diff(x,y) ==> Diffcolor(x,y)'))


KB.tell(expr('Diffcolor(f1,f2) & Diffcolor(f1,f5) & Diffcolor(f1,f3) & Diffcolor(f1,f6) & Diffcolor(f2,f4) & Diffcolor(f2,f5) & Diffcolor(f2,f3) & Diffcolor(f2,f6) & Diffcolor(f3,f6) &  Diffcolor(f5,f6) & Diffcolor(f3,f4) ==> Carte(f1,f2,f3,f4,f5,f6) '))

R=fol_fc_ask(KB, expr('Carte(c1,c2,c3,c4,c5,c6)'))

print(list(R))


