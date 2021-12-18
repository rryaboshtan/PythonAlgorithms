# В алфавите языкa племени «тумба-юмба» четыре буквы: «Ы», «Ш», «Ч» и «О».
# Нужно вывести на экран все слова, состоящие из L букв, 
# которые можно построить из букв этого алфавита.

def TumbaWords ( A, w, L ):
    if len(w) == L:
        print ( w )
        return
    for c in A:
        TumbaWords ( A, w + c, L )

TumbaWords ( "ЫШЧО", "", 2 )

# Result
# ЫЫ
# ЫШ
# ЫЧ
# ЫО
# ШЫ
# ШШ
# ШЧ
# ШО
# ЧЫ
# ЧШ
# ЧЧ
# ЧО
# ОЫ
# ОШ
# ОЧ
# ОО