aniversariante = (input("Aniversariante? (Sim/Não)"))
ingresso = (input("Tem ingresso? (Sim/Não)"))

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