def sumar(a, b):
  return a + b

def restar(a, b):
  return a - b

def multiplicar(a, b):
  return a * b

def dividir(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    return a / b

print("CALCULADORA")
print("Escriba un numero para seleccionar su operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

eleccion = (input("Ingrese su eleccion: "))

if eleccion not in ('1', '2', '3', '4'):
    print("Error: Debe elegir una opción válida del 1 al 4.")
else:
    try:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        
        if eleccion == '1':
            resultado = sumar(numero1, numero2)
            print("El resultado de la suma es:", resultado)
        elif eleccion == '2':
            resultado = restar(numero1, numero2)
            print("El resultado de la resta es:", resultado)
        elif eleccion == '3':
            resultado = multiplicar(numero1, numero2)
            print("El resultado de la multiplicación es:", resultado)
        elif eleccion == '4':
            resultado = dividir(numero1, numero2)
            if resultado == "No se puede dividir por cero":
              print(resultado)
            else:
              print("El resultado de la división es:", resultado)

    except ValueError:
        print("Error: Ingrese un número válido.")