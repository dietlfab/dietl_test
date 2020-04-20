continents = ["Afrika", "Antarktis", "Asien", "Australien und Ozeanien", "Europa", "Nordamerika", "Südamerika"]
counter = 0

print("Aufgabe 1.1")
for x in continents:
    print (x)

print("\nAufgabe 1.2")
for y in continents:
    if y == 'Antarktis':
        continue
    print (y)

print("\nAufgabe 1.3")
myList = ["Asien", "Max", 101, "Monika", "China", "Simbabwe", "Antarktis"]

for z in myList:
    if z not in continents:
        continue
    print (z)
    counter = counter +1
print("\nAufgabe 1.4")
print (counter)