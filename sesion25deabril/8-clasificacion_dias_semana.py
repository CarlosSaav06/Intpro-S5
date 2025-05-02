dia = input("Ingrese el dia de la semana (Lunes, Martes, Miercoles, Jueves, Viernes, Sabado, Domingo): ").lower()

if dia in ["lunes", "martes", "miercoles", "jueves", "viernes"]:
    print("Es un dia laboral")
elif dia in ["sabado","domingo"]:
    print("Es fin de semana")

else:
    print("ERROR")