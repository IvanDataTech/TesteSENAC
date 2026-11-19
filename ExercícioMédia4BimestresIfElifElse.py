Nota1 = float(input("Digite a 1ª nota do aluno: "))
Nota2 = float(input("Digite a 2ª nota do aluno: "))
Média1 = (Nota1 + Nota2) / 2
print(f"Com base na 1ª e 2ª nota, {Nota1} e {Nota2}, a 1ª média do aluno será de {Média1}")
if Média1 >= 9:
    print("Conceito A - Excelente")
elif Média1 >= 7:
    print("Conceito B - Muito Bom")
elif Média1 >= 5:
    print("Conceito C - Regular")
else:
    print ("Conceito D - Reprovado")

Nota3 = float(input("Digite a 3ª nota do aluno: "))
Nota4 = float(input("Digite a 4ª nota do aluno: "))
Média2 = (Nota3 + Nota4) / 2
print(f"Com base na 3ª e 4ª nota, {Nota3} e {Nota4}, a 2ª média do aluno será de {Média2}")
if Média2 >= 9:
    print("Conceito A - Excelente")
elif Média2 >= 7:
    print("Conceito B - Muito Bom")
elif Média2 >= 5:
    print("Conceito C - Regular")
else:
    print ("Conceito D - Reprovado")

Nota5 = float(input("Digite a 5ª nota do aluno: "))
Nota6 = float(input("Digite a 6ª nota do aluno: "))
Média3 = (Nota5 + Nota6) / 2
if Média3 >= 9:
    print("Conceito A - Excelente")
elif Média3 >= 7:
    print("Conceito B - Muito Bom")
elif Média3 >= 5:
    print("Conceito C - Regular")
else:
    print ("Conceito D - Reprovado")
print(f"Com base na 5ª e 6ª nota, {Nota5} e {Nota6}, a 3ª média do aluno será de {Média3}")

Nota7 = float(input("Digite a 7ª nota do aluno: "))
Nota8 = float(input("Digite a 8ª nota do aluno: "))
Média4 = (Nota7 + Nota8) / 2
if Média4 >= 9:
    print("Conceito A - Excelente")
elif Média4 >= 7:
    print("Conceito B - Muito Bom")
elif Média4 >= 5:
    print("Conceito C - Regular")
else:
    print ("Conceito D - Reprovado")
print(f"Com base na 7ª e 8ª nota, {Nota7} e {Nota8}, a 4ª média do aluno será de {Média4}")

MédiaFinal = (Média1 + Média2 + Média3+ Média4) / 4
print(f"A sua média final foi de {MédiaFinal}")
if MédiaFinal >= 7:
    print("Parabéns! Você foi aprovado neste ano!")
else:
    print("Infelizmente, você foi reprovado neste ano!")