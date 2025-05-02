letra_calificacion = input("Dame la letra de calificacion(A,B,C,D,F): ").upper()
if (letra_calificacion == "A"):
    print("Tu rendimiento fue excelente")
elif (letra_calificacion == "B"):
    print("Tu rendimiento fue bueno")
elif (letra_calificacion == "C"):
    print("Tu rendimiento fue satisfactorio")
elif (letra_calificacion == "D"):
    print("Aprobaste con la nota minima")
elif (letra_calificacion == "F"):
    print("reprobaste")

else:
    print("Letra no valida")