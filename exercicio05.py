# Exercicio 05
# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar

# 1. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# 2. A mensagem "Reprovado", se a média for menor do que sete;
# 3. A mensagem "Aprovado com Distinção", se a média for igual a dez.

print("##### AMBIENTE DE DIGITAÇÃO DE NOTA #######\n")
nota_p1 = input("Digite por favor a primeira nota parcial\n")

if nota_p1 != '':
    print("Obrigado professor(a), voce digitou a PRIMEIRA nota parcial para o Aluno(a)\n")
else:
    print("Professor, por favor, voce precisa digitar uma nota para o aluno.")

nota_p2 = input("Digite por favor a segunda nota parcial\n")

if nota_p2 != '':
    print("Obrigado professor(a), voce digitou a SEGUNDA nota parcial para o Aluno(a)")

media_parcial = (nota_p1 + nota_p2) / 2


