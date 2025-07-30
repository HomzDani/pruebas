import random 

def adivina_el_numero():
    print("bienvenido a: adivina el numero")
    print("elegi un numero del 1 al 100, puedes saber cual es?")

    # generar un numero aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    # bucle principal del juego 
    while not adivinado:
        try:
            # pedir al ususario que ponga un numero 
            intento = int(input("Introduce un numero: "))
            intentos += 1

            # compara el numero escrito con el numero secreto
            if intento < numero_secreto:
                print("es bajo, intentalo de nuevo")
            elif intento > numero_secreto:
                print("es alto, intentalo de nuevo")
            else:
                adivinado = True
                print("felicidades adivinaste el numero en: {intentos} intentos.")

        except ValueError:
            print("por favor, ingrese un numero valido")

    # preguntar si quieres jugar de nuevo
    jugar_de_nuevo = input("quieres jugar de nuevo? (s/n): ").lower()
    if jugar_de_nuevo == 's':
        adivina_el_numero()
    else:
        print("gracias por jugar, asta luego")

# iniciar el juego
adivina_el_numero()