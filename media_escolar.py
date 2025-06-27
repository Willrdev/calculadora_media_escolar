def calcular_media():

    nome = input('Qual o seu nome? ')
    n1 = float(input('Qual seria a nota 1? '))
    n2 = float(input('Qual seria a nota 2? '))
    n3 = float(input('Qual seria a nota 3? '))

    media = (n1 + n2 + n3) / 3

    print (f'{nome}, sua média foi {media}')

    if media >=7:
        print('Aprovado')
    elif media >= 5:
        print('Recuperação')
    else:
        print('Reprovado')

calcular_media()
       











