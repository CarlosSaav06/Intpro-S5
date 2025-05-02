dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

if mes == 2 and dia > 29:
    print("Error: Febrero no puede tener más de 29 días.")
else:
    print("Fecha ingresada:", dia, "/", mes, "/", año)
