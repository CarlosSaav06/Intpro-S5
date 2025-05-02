print("Calculadora básica")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Elige una opción (1-4): ")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if opcion == "1":
    resultado = num1 + num2
    print("La suma es:", resultado)
elif opcion == "2":
    resultado = num1 - num2
    print("La resta es:", resultado)
elif opcion == "3":
    resultado = num1 * num2
    print("La multiplicación es:", resultado)
elif opcion == "4":
    if num2 != 0:
        resultado = num1 / num2
        print("La división es:", resultado)
    else:
        print("No se puede dividir entre cero.")
else:
    print("Opción no válida.")
