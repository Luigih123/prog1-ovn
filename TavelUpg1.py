inmatning = int(input('skriv in ett heltal:'))

svar = inmatning % 2

if svar == 1:
    print(f'talet {inmatning} är ojämt')
else:
        print(f'talet {inmatning} är jämt')