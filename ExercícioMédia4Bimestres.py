PrimeiraNota = float(input("Digite a 1ª nota do aluno: "))
SegundaNota = float(input("Digite a 2ª nota do aluno: "))
Média1 = (PrimeiraNota + SegundaNota) / 2
if Média1 >= 7:
    print("Aprovado no Bimestre")
else:
    print("Insuficiente no Bimestre")

print(f"Com base na 1ª e 2ª nota, {PrimeiraNota} e {SegundaNota}, a 1ª média do aluno será de {Média1}")

TerceiraNota = float(input("Digite a 3ª nota do aluno: "))
QuartaNota = float(input("Digite a 4ª nota do aluno: "))
Média2 = (TerceiraNota + QuartaNota) / 2
if Média2 >= 7:
    print("Aprovado no Bimestre")
else:
    print("Insuficiente no Bimestre")

print(f"Com base na 3ª e 4ª nota, {TerceiraNota} e {QuartaNota}, a 2ª média do aluno será de {Média2}")

QuintaNota = float(input("Digite a 5ª nota do aluno: "))
SextaNota = float(input("Digite a 6ª nota do aluno: "))
Média3 = (QuintaNota + SextaNota) / 2
if Média3 >= 7:
    print("Aprovado no Bimestre")
else:
    print("Insuficiente no Bimestre")

print(f"Com base na 5ª e 6ª nota, {QuintaNota} e {SextaNota}, a 3ª média do aluno será de {Média3}")

SétimaNota = float(input("Digite a 1ª nota do aluno: "))
OitavaNota = float(input("Digite a 2ª nota do aluno: "))
Média4 = (SétimaNota + OitavaNota) / 2
if Média4 >= 7:
    print("Aprovado no Bimestre")
else:
    print("Insuficiente no Bimestre")

print(f"Com base na 7ª e 8ª nota, {SétimaNota} e {OitavaNota}, a 4ª média do aluno será de {Média4}")

MédiaFinal = (Média1 + Média2 + Média3+ Média4) / 4
print(f"A sua média final foi de {MédiaFinal}")
if MédiaFinal >= 7:
    print("Parabéns! Você foi aprovado neste ano!")
else:
    print("Infelizmente, você foi reprovado neste ano!")