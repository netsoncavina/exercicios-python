"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para 
controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de 
peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que 
você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o 
valor da multa que João deverá pagar. Imprima os dados do programa com as 
mensagens adequadas.
"""

LIMITE = 50

quantidade_peixes_kg = float(input("Insira a quantidade de kilos de peixe "))

excesso = 0
multa = 0

if (quantidade_peixes_kg > LIMITE):
    excesso = quantidade_peixes_kg - LIMITE

if excesso > 0:
    multa = excesso * 4

print(
    f'O Sr trouxe {quantidade_peixes_kg}kgs de peixe\nO excesso foi de {excesso}kgs\nA multa é de R${multa} ')
