"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a 
média alcançada por aluno e apresentar: 
a. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; 
b. A mensagem "Reprovado", se a média for menor do que sete; 
c. A mensagem "Aprovado com Distinção", se a média for igual a dez
"""

nota1 = float(input("Insira a primeira nota "))
nota2 = float(input("Insira a terceira nota "))
nota3 = float(input("Insira a segunda nota "))

media = (nota1 + nota2 + nota3) / 3

if media < 7:
    print("Reprovado")
elif media == 10:
    print("Aprovado com Distinção")
else:
    print("Aprovado")
