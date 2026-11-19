PrimeiraNota = float(input("Digite a 1ª nota do aluno: "))
SegundaNota = float(input("Digite a 2ª nota do aluno: "))
Média = (PrimeiraNota + SegundaNota) / 2
if Média >= 7:
    print("Aprovado no Bimestre")
else:
    print("Insuficiente no Bimestre")

print(f"Com base na 1ª e 2ª nota, {PrimeiraNota} e {SegundaNota}, a média do aluno será de {Média}")