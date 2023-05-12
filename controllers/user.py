from decorators.user_decorators import *
from db.validations import user_exists


@clear_terminal
def create_user(connect, cursor):
    """A - Crear usuario"""

    username = input("Ingresa un nombre: ")
    email = input("Ingresa un email: ")
    if not user_exists(username, email, cursor):
        query = "INSERT INTO users(username, email) VALUES (%s, %s)"
        values = (username, email)
        cursor.execute(query, values)
        connect.commit()
        print("Usuario creado")
    else:
        print("El usuario ya existe")


@clear_terminal
def list_users(connect, cursor):
    """B - Listar usuarios"""

    query = "SELECT id, username, email FROM users"
    cursor.execute(query)

    print("Listado de usuarios")

    for id, username, email in cursor.fetchall():
        print(id, '-', username, '-', email)
    

@clear_terminal
@find_users
def update_user(connect, cursor):
    """C - Actualizar usuario"""

    user = int(input("Ingresa el número del usuario a actualizar: "))
    query = "SELECT id FROM users WHERE id = %s"
    cursor.execute(query, (user,))

    user_selected = cursor.fetchone()
    if user_selected:
        username = input("Ingresa un nuevo username: ")
        email = input("Ingresa un nuevo email: ")

        query = "UPDATE users SET username = %s, email = %s WHERE id = %s"
        values = (username, email, user)
        cursor.execute(query, values)
        connect.commit()
        print("Usuario actualizado exitosamente")
    else:
        print("No existe un usuario con ese número.")

@clear_terminal
@find_users
def delete_user(connect, cursor, users):
    """D - Eliminar usuario"""
    
    user = int(input("Ingresa el número del usuario a eliminar: "))
    query = "SELECT id FROM users WHERE id = %s"
    cursor.execute(query, (user,))

    user_selected = cursor.fetchone()
    if user_selected:
        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (user,))
        connect.commit()
        print("Usuario eliminado exitosamente")
    else:
        print("No existe un usuario con ese número.")


def default():
    print("Opción no valida")