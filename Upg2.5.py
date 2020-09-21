pris = float(input('skriv varans pris'))
moms = float(input('skriv varans moms i procent'))

emoms = pris / (moms / 100 + 1)

print(f'priset exkulsive moms: {emoms}')
print(f'momsen är: {pris - emoms}')