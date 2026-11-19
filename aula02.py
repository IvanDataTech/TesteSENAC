nome = input("Digite o seu nome: ")
idade= float(input("Digite a sua idade: "))

if idade >= 18:
    print('Acesso permitido')
else:
    print('Acesso negado')
print(f"{nome} tem {idade} anos")