mail = "bill.gates@microsoft.de"

ergebnis = mail.split("@")

print (ergebnis[0])

mail2 = "info@bill-gates.de"

ergebnis2 = mail2.split("@")

ergebnis3 = ergebnis2[1].split(".")

print (ergebnis3[0])

email1 = "bill.gates@microsoft.com"
email2 = "stevie@warcraft.com"
email3 = "unholzer@bmw.de"
clients = []

clients.append(email1)
clients.append(email2)
clients.append(email3)

print(clients)
print(len(clients))