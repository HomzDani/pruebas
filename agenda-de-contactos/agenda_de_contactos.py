def crear_agenda():
    # Crear una agenda vacias
    return

def agregar_contacto(agenda, nombre, telefono, email):
    # agrega un nuevo contacto a la agenda
    contacto = {
        'nombre': nombre,
        'telefono': telefono,
        'email': email
    }
    agenda.append(contacto)
    print(f"contacto {nombre} agregado correctamente.")

def buscar_contacto(agenda, nombre):
    # busca un contacto por nombre
    for contacto in agenda:
        if contacto['nombre'].lower() == nombre.lower():
            return None
def mostrar_contacto(contacto):
    if contacto:
        print("informacion del contacto:")
        print(f"nombre: {contacto["nombre"]}")
        print(f"telefono: {contacto["telefono"]}")
        print(f"email: {contacto["email"]}")
    else:
        print("contacto no encontrado.")

def mostrar_todos(agenda):
    # muestra todos los contactos de la agenda
    if not agenda:
        print("la agenda esta vacia.")
        return
    
    print("lista de contactos:")
    for i, contactos in enumerate(agenda, 1):
        print(f"{i}. {contacto["nombre"]} - {contacto['telefono']}")

def eliminar_contacto(agenda, nombre):
    # eliminar un contacto de la agenda
    for i, contacto in enumerate(agenda):
        if contacto['nombre'].lower() == nombre.lower():
            del agenda[i]
            print(f"contacto {nombre} eliminado correctamente.")
            return
    print("contacto no encontrado.")

def menu():
    # muestra el menu de opciones
    print("Agenda de contactos")
    print("1. agregar nuevo contacto")
    print("2. buscar contacto")
    print("3. mostrar todos los contactos")
    print("4. eliminar contacto")
    print("5. salir")

def main():
    agenda = crear_agenda()

    while True:
        menu()
        opcion = input("seleciona una opcion: ")

        if opcion == '1':
            nombre = input("nombre: ")
            telefono = input("telefono: ")
            email = input("email: ")
            agregar_contacto(agenda, nombre, telefono, email)

        elif opcion == '2':
            nombre = 