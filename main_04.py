# Ispisati brojeve od 1 do 10
# for i in range(10):
#     print(i + 1, end=', ')


# # Ispisati brojeve od 10 do 20
# for i in range(10, 21):
#     print(i, end=', ')


# Ispisati brojeve od 10 do 50, ali svaki 5.
# for i in range(10, 51, 5):
#     print(i, end=', ')


# Ispisati brojeve od 10 do 21, ali svaki 1/2. NE RADI JER argumenti moraju biti INT
for i in range(10, 21, 0.5):
    print(i, end=', ')


# range(start, stop, step)
# range(10) - start=0, stop=10, step=1 - start je UKLJUCEN u raspon, STOP NIJE
# range(10, 21) - start=10, stop=21, step=1 - start je UKLJUCEN u raspon, STOP NIJE
# range(10, 51, 5) - start=10, stop=51, step=5 - start je UKLJUCEN u raspon, STOP NIJE
