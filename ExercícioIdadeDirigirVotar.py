nome = input("Digite o seu nome: ")
idade= int(input("Digite a sua idade: "))

if idade >= 18:
    print('Você pode dirigir e votar')
else:
    print('Você ainda é menor de idade')
print(f"{nome} tem {idade} anos")