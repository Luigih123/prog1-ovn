Dagens_mätarställning = float(input('Dagens mätarställning: '))
Mätarställning_för_ett_år_sedan = float(input('Mätarställning för ett år sedan: '))
Total_liter_bensin = float(input('Antal liter bensin: '))
print('Mätarställning i dag?:', Dagens_mätarställning)
print('Mätarställning för ett år sedan?:', Mätarställning_för_ett_år_sedan)
Total_mil_körd = Dagens_mätarställning - Mätarställning_för_ett_år_sedan
print('Antal körda mil:', Total_mil_körd)
print('Antal liter bensin:', Total_liter_bensin)
Förbrukning_liter_per_mil = Total_liter_bensin / Total_mil_körd
print(f'Förbrukning per mil: {Förbrukning_liter_per_mil:.2f}')