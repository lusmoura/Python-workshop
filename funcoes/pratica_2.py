def eh_par(numero):
    if numero % 2 == 1:
        return False
    else:
        return True

numero = 3

if eh_par(numero):
    print(numero, 'é par')
else:
    print(numero, 'é impar')