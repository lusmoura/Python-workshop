valores = {'Ana':12, 'Jão':100, 'Guilherme':120, 'Ze': 5}

soma = 0

for valor in valores.values():
    soma += valor

preco = float(input('Digite o preco do produto: '))

if soma >= preco:
    print('Dá pra comprar!!')
else:
    print('Não dá =(')
