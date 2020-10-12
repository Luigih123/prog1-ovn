minuter = int(input('Hur många minuter ringer du per månad?'))
if minuter <= 32:
    print('Kontant')
elif minuter >= 67:
        print('plus')
else:
    print('normal')