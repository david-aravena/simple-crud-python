from controllers.user import *
from db.sentences import *
from db.config import CONNECT, OPERATIONAL_ERROR

if __name__ == "__main__":

    options = {
        'a': create_user,
        'b': list_users,
        'c': update_user,
        'd': delete_user
    }

    try:
        with CONNECT.cursor() as cursor:

            if not table_exists('users', cursor):
                cursor.execute(USERS_TABLE)
                CONNECT.commit()

            while True:
                for function in options.values():
                    print(function.__doc__)

                print("Q - Salir del programa")
                option = input("Selecciona una opcion valida: ").lower()

                if option == "q":
                    break

                function = options.get(option, default)
                function(CONNECT, cursor)

    except OPERATIONAL_ERROR as err:
        print(f'Ha ocurrido el siguiente error: {err}')