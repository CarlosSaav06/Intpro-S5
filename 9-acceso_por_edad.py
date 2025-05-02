edad = int(input("Ingresa tu edad: "))

if edad <= 0 and edad > 120:
    print("Edad invalida")
elif edad < 12:
    print("Puedes entrar a una pelicula para niños")
elif edad < 18:
    print("Puedes entrar a una peicula para adolescentes")
elif edad > 18:
    print("Puedes entrar a una pelicula para adultos")
