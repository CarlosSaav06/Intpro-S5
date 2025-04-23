monto_total = float(input("Ingrese el monto total: "))
satisfaccion = input("el servicio fue bueno o malo? (bueno/malo)")
if satisfaccion == "bueno":
    propina = monto_total * 0.15
elif satisfaccion == "mala":
    propina = monto_total * 0.05
else: 
    print("nivel de satisfaccion no valido")
total_pagar = monto_total + propina
print("el total es: ", total_pagar)