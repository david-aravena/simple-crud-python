import os

def find_users(funcion):
    def funcion_decorada(connect, cursor):
        name = input("Ingresa el nombre del usuario: ")
        query = f"SELECT id, username, email FROM users WHERE username='{name}'"
        cursor.execute(query)
        users = cursor.fetchall()
        if users:
            print("Los siguientes son los usuarios obtenidos:")
            for id, username, email in users:
                print(id, '-', username, '-', email)
        else:
            print("No existen usuarios con ese nombre.")
            return
        
        resultado = funcion(connect, cursor, users)
        return resultado
    
    funcion_decorada.__doc__ = funcion.__doc__
    return funcion_decorada


def clear_terminal(function):
    def wrapper(connect, cursor):
        os.system("clear")
        function(connect, cursor)
        input("Presiona enter para volver al menu principal")
        os.system("clear")

    wrapper.__doc__ = function.__doc__
    return wrapper