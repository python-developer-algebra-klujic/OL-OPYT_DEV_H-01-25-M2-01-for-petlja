# Napisite program koji korisniku omogucava ispis tablice mnozenja
# do broja koji korisnik definira

limit = int(input('Upisite do kojeg broja zelite ispis tablice mnozenja: '))

for j in range(limit):
    # Ispis reda za broj 1
    for i in range(limit):
        print((j + 1) * (i + 1), end=' ')
    print()


# for i in range(limit):
#     # Ispis reda za broj 1
#     for j in range(limit):
#         print(i * (j + 1), end=' ')
#     print()


# # Ispis reda za broj 2
# for i in range(limit):
#     print(2 * (i + 1), end=' ')
# print()


# # Ispis reda za broj 3
# for i in range(limit):
#     print(3 * (i + 1), end=' ')
# print()


# # Ispis reda za broj 4
# for i in range(limit):
#     print(4 * (i + 1), end=' ')
# print()
