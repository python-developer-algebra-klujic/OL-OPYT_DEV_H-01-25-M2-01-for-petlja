'''
Ako automobil troši 5.3 litara na 100 km i ako je cijena goriva 9.56 kn po litri 
(nije važno kojeg goriva), izračunajte koliko košta 1 km vožnje automobilom. 
Prikažite mjesečni trošak (30 dana) odlaska na posao automobilom koji 
je udaljen 20 km u jednom smjeru.
'''

CHARS = 80


print()
print('\t\tKalkulator potrosnje goriva')
print()
print('-'*CHARS)

fuel_consumption = float(input('Upisite potrosnju goriva vozila (l/100km): '))
fuel_price = float(input('Cijena goriva (EUR/l): '))
commuting_distance_km = int(input('Upisite udaljenost u km do posla u jednom smijeru: '))

price_per_km = (fuel_consumption / 100) * fuel_price
daily_distance_km = 2 * commuting_distance_km
monthly_distance_km = 30 * daily_distance_km

# daily_costs = round(daily_distance_km * price_per_km, 2)
# monthly_costs = round(monthly_distance_km * price_per_km, 2)
daily_costs = daily_distance_km * price_per_km
monthly_costs = monthly_distance_km * price_per_km

display_daily_costs = f'Dnevni trosak odlaska na posao autom iznosi: {daily_costs:.2f} EUR.'
display_monthly_costs = f'Mjesecni trosak odlaska na posao autom iznosi: {monthly_costs:.2f} EUR.'

print()
print('-'*CHARS)
print()
print(display_daily_costs)
print(display_monthly_costs)
print()
print('-'*CHARS)
print()
