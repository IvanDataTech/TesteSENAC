Nota = float(input("Digite a nota do aluno: "))
if Nota >= 9:
    print("Conceito A - Excelente")
else:
    if Nota >= 7:
        print("Conceito B - Muito Bom")
    else:
        if Nota >= 5:
            print("Conceito C - Regular")
        else:
            print ("Conceito D - Reprovado")