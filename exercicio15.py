soma = 0
count = 0

while count < 5:
    soma += float(input(f'Insira o {count+1}º numero '))
    count += 1

print(f'Soma: {soma}\nMédia: {soma/5}')
