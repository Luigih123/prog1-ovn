svar = input('Antal sekunder: ')
sek = int(svar)
print('Inmatningen:', sek)
dekad = sek // 315_569_260
sek = sek % 315_569_260
print('Rest från decad:', sek)
år = sek // 31_556_926
sek = sek % 31_556_926
print('Rest från år', sek)
månad = sek // 2_629_744
sek = sek % 2_629_744
print('Rest från månader', sek)
vecka = sek // 604_800
sek = sek % 604_800
print('Rest från veckor', sek)
dag = sek // 86400
sek = sek % 86400
print('Rest från dagar', sek)
tim = sek // 3600
sek = sek % 3600
print('Rest från timmar:', sek)
min = sek // 60
sek = sek % 60
print('Rest från minuter', sek)
print('Dekader:', dekad)
print('År:', år)
print('Månader:', månad)
print('Veckor:', vecka)
print('Dagar:', dag)
print('Timmar:', tim)
print('Minuter:', min)
print('Sekunder:', sek)