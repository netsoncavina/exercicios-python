letra = input("Digite uma letra ")

vogais = ['a', 'e', 'i', 'o', 'u']

if len(letra) > 1:
    print("Digite apenas uma letra!")
elif letra.isdigit():
    print("Digite uma letra!")
else:
    if letra.lower() in vogais:
        print(f'{letra} é vogal')
    else:
        print(f'{letra} não é vogal')
