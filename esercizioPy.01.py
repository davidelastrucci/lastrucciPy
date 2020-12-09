giorno = int(input("quanti giorni?"))
if giorno == 1:
    print("L'importo è: 45$")
elif giorno > 1:
    print("L'importo è:", giorno * 40, "$")
else:
    print("errore, riprova")