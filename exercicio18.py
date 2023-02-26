numero1 = int(input("Insira o primeiro numero "))
numero2 = int(input("Insira o segundo numero "))
soma = 0
if numero1 == numero2:
    print("Os numeros são iguais")
elif numero1 > numero2:
    count = numero2 + 1
    while count < numero1:
        soma += count
        print(count)
        count += 1
    print(f'Soma : {soma}')
else:
    count = numero1+1
    while count < numero2:
        soma += count
        print(count)
        count += 1
    print(f'Soma : {soma}')
