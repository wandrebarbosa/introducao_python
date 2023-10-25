
# LOGICA BOOLEANA
2 > 3 # Mentira, inverdade, false
3 > 2 # Verdade, True

nome_1 = "wandreson"
idade_1 = 31
nome_2 = "amanda"
idade_2 = 30
nome_3 = "wandreson"
idade_3 = 15

testeboolean1 = nome_1 == nome_2
testeboolean2 = nome_1 == nome_3

# print(testeboolean1)
# print(testeboolean2)

# Operações com números booleano
# >, >=,  <, <=, ==
# Quando vc for trabalar com == e is vai tratar coisa diferentes na regra booleana,
# exemplo
verificar1 = 1 == 1.0
print(verificar1)

verificar2 = 1 is 1.0
print(verificar2)
# porem se eu usar 'is' no lugar do '==' (por sinal muito dificil usar o operador 'is')

# AND, OR, NOT
# EXEMPLO, 
nome_1 == nome_3
# True
nome_1 == nome_3 and idade_1 ==  idade_3
# False
nome_1 == nome_3 or idade_1 ==  idade_3
# True
nome_1 == nome_3 or idade_1 ==  idade_3
# True
nome_1 == nome_3 and idade_1 ==  idade_3
# False