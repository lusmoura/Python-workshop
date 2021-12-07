def calcula_media(notas):
    soma = 0

    for nota in notas:
        soma += nota

    media = soma/len(notas)
    return media

media = calcula_media([1, 2, 3, 4, 5, 6])
print(media)