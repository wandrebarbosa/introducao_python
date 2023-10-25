# ESTRUTURAS DE DECISAO - IF, ELIF, ELSE
# x = 5
# y = 5
# if  x == y:
#     print('Mesmo valor')
# elif x > y:
#     print('x é maior que y')
# else:
#     print(f'Não sei resolver {x} e {y}')


#EXEMPLO 01
# reposta = input('Papai você comprou pão??')

# if reposta == 'sim':
#     print('Obrigado, Papai!')
# elif reposta == 'não':
#     print('Nenenzinha ta triste, buá!, buá!')
# else:
#     print('Não foi isso que eu perguntei')


# EXEMPLO DA ESPOSA DE UM GAMER
carteira = int(input('Quanto eu tenho?  '))
produto = int(input('Quanto custa o que tu quer comprar, menino?  '))
necessidade = input('Precisa mesmo disso [s/n]??  ')

if carteira >= produto and necessidade == 's':
    print('Pode comprar amor, vc merece!')
else:
    print('É melhor deixar pra depois, tem a frauda da Ana Aurora.')