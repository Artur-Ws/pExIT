jezyki = ['Python', 'Java', 'C#', 'Ruby']

jezyki_odwrocone = list(reversed(jezyki))
print(jezyki_odwrocone)
print(jezyki)

print()
jezyki_odwrocone = jezyki[::-1]
print(jezyki_odwrocone)

jezyki_odwrocone = []

for jezyk in jezyki:
    jezyki_odwrocone.insert(0,jezyk)

print(jezyki_odwrocone)

odwroc_mnie = ['trudne', 'takie', 'bylo', 'nie', 'To']
odwrocona = odwroc_mnie[::-1]
print(odwrocona)