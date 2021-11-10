casa = {'Comodos': 4, 'Cor': 'Azul', 'Material': 'Madeira', 'Altura':3.2}

# acessando por chave
print('Comodos: ', casa['Comodos'])
print('Cor: ', casa['Cor'])
print('Material: ', casa['Material'])
print('Altura: ', casa['Altura'])

# utilizando repeticao
for caracteristica in casa:
    print(caracteristica, ': ', casa[caracteristica])
