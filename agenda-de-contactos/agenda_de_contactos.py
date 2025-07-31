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
