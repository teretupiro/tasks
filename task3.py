def season(a):
    if a<=12 and a<=2:
        return ('зима')
    if a>=3 and a<=5:
        return('весна')
    if a>=6 and a<=8:
        return('лето')
    if a>=9 and a<=11:
        return('осень')



print(season(5))
