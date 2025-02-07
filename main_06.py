# ZADATAK za DZ
# Kreirajte program koji od korisnika trazi visinu bozicnog drvca i simbol te ga iscrtajte
# Primjer: za visinu = 11 i simbol = *
'''
   12345678901
1  -----*
2      ***
3     *****
4    *******
5   *********
6  ***********
       **
       **
'''



height = int(input('Upisite visinu bozicnog drvca: '))
symbol = input('Upisite znak koji ce biti iscrtano drvce: ')

# print((height // 2) + 1)

for i in range((height // 2) + 1):
   print(f' ' * ((height // 2) - i), end='')
   print(f'{symbol}' * ((i*2) + 1))

for j in range(2):
   print(f' ' * ((height // 2) - 1), end='')
   print(f'|' * 3)









# Rjesenje kolege: Mario Vojić

# razmak=int(input("Unesite visinu drvca: "))
# print()

# postolje_razmak=razmak-1



# for i in range(razmak):
#     print(f' '*(razmak-i)+f'*'*((i*2)+1))

# for j in range(2):
#     print(f' '*postolje_razmak+f'#'*2)

# print()