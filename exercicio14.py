"14.  Faça um programa que leia 5 números e informe o maior número."

maior = 0
count = 0

while count < 5:
    numero = float(input(f'Insira o {count+1}º número '))
    if count == 0:
        maior = numero
    elif numero > maior:
        maior = numero
    count += 1

print(f'O maior numero inserido foi {maior}')
