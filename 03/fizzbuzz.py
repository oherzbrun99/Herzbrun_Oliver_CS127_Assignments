n = 1
for n in range(100):
    if n % 3 == 0 and n % 5 == 0:
        print('HellYeah!')
    elif n % 3 == 0:
        print('All is better in threes.')
    elif n % 5 == 0:
        print('The power of five compells you.')
    else:
        print(n)