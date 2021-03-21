def is_prime(a):
    for b in range(0,a):

        if b==1 and b==a or b==0:
            continue
        if a % b==0:
            return 'false'
    return 'true'


print(is_prime(2))