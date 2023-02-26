numero1 = int(input("Insira o primeiro numero "))
numero2 = int(input("Insira o segundo numero "))

if numero1 == numero2:
    print("Os numeros são iguais")
elif numero1 > numero2:
    count = numero2 + 1
    while count < numero1:
        print(count)
        count += 1
else:
    count = numero1+1
    while count < numero2:
        print(count)
        count += 1
