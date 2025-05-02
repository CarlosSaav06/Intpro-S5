lado_1 = int(input("Ingresa el primer lado: "))
lado_2 = int(input("Ingresa el segundo lado: "))
lado_3 = int(input("Ingrese el tercer lado: "))

if lado_1 == lado_2 and lado_1 == lado_3:
    print("Es un triangulo equilatero")
elif lado_1 == lado_2 and lado_2 != lado_3 or lado_2 == lado_3 and lado_3 != lado_1 or lado_3 == lado_1 and lado_1 != lado_2 or lado_1 == lado_3 and lado_3 != lado_2:
    print("Es un triangulo isoceles")
elif lado_1 != lado_2 and lado_2 != lado_3 and lado_1 != lado_3:
    print("Es un triangulo escaleno")
else:
    print("ERROR")

    