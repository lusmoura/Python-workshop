numeros = [100, 128, 76, 8728, 217, 281]
menor = 10000000000000

for numero in numeros:
    if numero < menor:
        menor = numero

print(menor)
