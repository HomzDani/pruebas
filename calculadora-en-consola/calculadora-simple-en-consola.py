# calculadora simple en consola

def calculadora():
    print("calculadora simple")
    print("operadores disponibles:")
    print("1. suma (+)")
    print("2. resta (-)")
    print("3. multiplicacion (*)")
    print("4. division (/)")
    print("5. salir")

    while True:
        try:
            #solicitar operacion al usuario
            opcion = input("seleciones una operacion (1-5): ")

            if opcion == '5':
                print("hasta luego")
                break
            if opcion not in ('1', '2', '3', '4'):
                print("opcion no valida, intente de nuevo.")
                continue

            # solicitar numero al usuario
            num1 = float(input("ingresa el primer numero: "))
            num2 = float(input("ingrese el segundo numero: "))

            #realizar operacion seleccionada
            if opcion == '1':
                resultado = num1 + num2
                print(f"resultado: {num1} + {num2} = {resultado}")
            elif opcion == '2':
                resultado = num1 - num2 
                print(f"resultado: {num1} - {num2} = {resultado}")
            elif opcion == '3':
                resultado = num1 * num2
                print(f"resultado: {num1} * {num2} = {resultado}")
            elif opcion == '4':
                if num2 == 0:
                    print("error: no se puede dividir por cero")
                else:
                    resultado = num1 / num2
                    print(f"resultado: {num1} / {num2} = {resultado}")

            print() # Linea en blanco para separar operaciones

        except ValueError:
            print("error: por favor ingrese numeros validos.")
        except Exception as e:
            print(f"ocurrio un error: {e}")

# ejecutar la calculadora
if __name__ == "__main__":
    calculadora()

