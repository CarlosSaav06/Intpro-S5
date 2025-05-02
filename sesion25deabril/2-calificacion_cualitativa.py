calificacion = int(input("Ingrese tu calificacion: "))
if calificacion >= 0 and calificacion < 70:
    print("Estas reprobado")
elif calificacion >= 70 and calificacion <= 79:
    print("Estas aprobado")
elif calificacion >= 80 and calificacion <= 89:
    print("Usted tiene una calificacion buena")
elif calificacion >= 90 and calificacion <= 95:
    print("Usted tiene una calificacion muy buena")
elif calificacion >= 96 and calificacion <= 100:
    print("Usted tiene una calificacion excelente")