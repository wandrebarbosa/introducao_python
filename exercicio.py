# EXERCICIO 04
#  Faça um programa que mostra 2 numero inteiro e um numero float, Calcule e mostre
# 1. O produto do dobro do primeiro com metade do segundo
# 2. A soma do triplo do primeiro com o terceiro
# 3. O terceiro elevado ao cubo.

entrada1 = int(input("digite o primeiro número: "))
entrada2 = int(input("digite um segundo número: "))
entrada3 = float(input("digite um terceiro numero podendo esse ser fracionado."))

print(type(entrada1))
print(type(entrada2))
print(type(entrada3))

dobro_primeiro = (entrada1 * 2) * (entrada2 / 2)
soma_triplo = (entrada1 * 3) + entrada3
terceiro_cubo = entrada3 ** 3

print(dobro_primeiro)
print(soma_triplo)
print(terceiro_cubo)

# transformando os valores da minha variavel para inteiro(int).






