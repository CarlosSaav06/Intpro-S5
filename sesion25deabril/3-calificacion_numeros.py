primer_numero = int(input("Ingrese un numero: "))
segundo_numero = int(input("Ingrese un segundo numero: "))
tercer_numero = int(input("Ingrese un tercerc numero: "))

if primer_numero == segundo_numero and segundo_numero == tercer_numero:
     print("Todos los numeros son iguales")
elif primer_numero > segundo_numero and primer_numero > tercer_numero:
     print("El numero mayor es",primer_numero)
     if segundo_numero < tercer_numero:
          print("El numero menor es ", segundo_numero)
     else:
          print("El numero es", tercer_numero)
elif tercer_numero > primer_numero and tercer_numero > segundo_numero:
     print("El mayor ",tercer_numero)
     if tercer_numero < primer_numero:
          print("El menor es ",tercer_numero) 
     else:
          print("El menor es ",segundo_numero)
elif segundo_numero > primer_numero and segundo_numero > tercer_numero:
     print("El mayor es",segundo_numero)
     if primer_numero < tercer_numero:
          print("El menor es",primer_numero)
     else:
          print("El menor es",tercer_numero)
    
     
    