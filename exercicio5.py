"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: 
a) o produto do dobro do primeiro com metade do segundo . 
b) a soma do triplo do primeiro com o terceiro. 
c) o terceiro elevado ao cubo
"""

numero1 = int(input("Insira um numero inteiro "))
numero2 = int(input("Insira outro numero inteiro "))
numero3 = float(input("Insira um numero real "))

a = (numero1 * 2) * (numero2 / 2)
b = (numero1 * 3) + numero3
c = numero3**3

print(f'Respostas \na = {a}\nb = {b}\nc = {c} ')
