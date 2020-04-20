continents = ["Afrika", "Antarktis", "Asien", "Australien und Ozeanien", "Europa", "Nordamerika", "Südamerika"]

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

print("\nAufgabe 1.4")
counter = 0
for n in continents:
    if myList.count(n) == True:
        counter = counter + 1
print(counter)