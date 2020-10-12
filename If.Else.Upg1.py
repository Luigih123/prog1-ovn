print('Välj mellan:\nSpela dator\nSova\nÄta\nToa')
hemma = input('Vad vill du göra?').capitalize()
if hemma == 'Spela dator':
    print('Gud vad roligt det är att spela')
elif hemma == 'Sova':
    print('Jag är jätte trött')
elif hemma == 'Äta':
    print('Mhmmm mackor smasskens')
elif hemma == 'Toa':
    print('Måste tömma blåsan')
else:
    print('Du tog dig aldrig hem LMAO')