temperatura = float(input("Dame la temperatura en grados celsius: "))

if temperatura <= 0:
    print("El clima esta muy frio")
elif temperatura <= 14 and temperatura > 0:
    print("El clima esta frio")
elif temperatura >=15 and temperatura <= 24:
    print("El clima esta templado")
elif temperatura >= 25 and temperatura <= 30:
    print("El clima esta calido")
elif temperatura > 30:
    print("El clima esta muy caluroso")

else:
    print("ERROR")