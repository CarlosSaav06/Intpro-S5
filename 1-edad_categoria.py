edad = int(input("Ingrrese tu edad: "))
if edad >= 0 and edad < 11:
    print("Eres niño")
elif edad < 12 and edad > 18:
    print("Eres adulto")
elif edad >= 18 and edad <= 65:
    print("Eres un niño")
elif edad > 65 and edad <= 130:
    print("Eres un anciano")