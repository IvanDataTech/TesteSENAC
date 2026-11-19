aniversariante = bool(input("Aniversariante? (Sim/Não)"))
ingresso = bool(input("Tem ingresso? (Sim/Não)"))

if aniversariante == "Sim":
    aniversariante = True
else:
    aniversariante = False
if ingresso == "Sim":
    ingresso = True
else:
    ingresso = False
if aniversariante == True or ingresso == True:
    print("Entrada liberada!")
else:
    print("Precisa comprar ingresso!")