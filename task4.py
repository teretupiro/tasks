def bank(a,years):
    result=0
    for summ in range(0,years):
        print(a)
    a=a*1.1
    result=a
    return result
print(bank(1000,3))
