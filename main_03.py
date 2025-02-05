# Kreirati program koji ce omoguciti korisniku unos podataka za 10 clanova grupe
# Podaci koje treba pohraniti su: ime, prezime, godina rodenja i ID clana.


for i in range(10): # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 !!! NE I 10 !!!
    # member_id = int(input(f'Upisite ID broj {i + 1}. clana: '))
    member_id = i + 1
    first_name = input(f'Upisite ime {i + 1}. clana: ')
    last_name = input(f'Upisite prezime {i + 1}. clana: ')
    year_of_birth = int(input(f'Upisite godinu rodenja {i + 1}. clana: '))
    # Nakon ove linije ubaciti unesene vrijednosti u neku kolekciju najcesce listu


print('Kraj programa')
