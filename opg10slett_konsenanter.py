setning = input("Skriv inn en setning: ")

def fjern_konsonanter(setning):
    konsonanter = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    return "".join(c for c in setning if c not in konsonanter)

resultat = fjern_konsonanter(setning)
print(resultat)
