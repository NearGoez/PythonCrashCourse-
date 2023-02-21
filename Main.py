#Exercise 3.4
guest = ["Daniel", "Esteban", "Katy", "Lucy"]
caido = guest.pop()
for x in guest:
    print(f"Te invito a mi cena {x}")

#Exercise 3.5
guest.append("Cata")
print(f"te invito a mi cena {guest[3]} ")

#Exercise 3.6
guest.insert(0,"Pipe")
guest.insert(2,"Wilson")
guest.append("Laura")

#Exercise 3.7
for x in guest:
    print(f"te invito a mi cena {x}")

while len(guest) != 2:
    invitadoNo = guest.pop()
    print(f"Disculpa {invitadoNo}, tuve un drama con las mesas y tuve que cancelar")

for x in guest:
    print(f"{x}, ven a la cena")

