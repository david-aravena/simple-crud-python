from controllers.user import *
from db.sentences import *
from db.config import CONNECT, OPERATIONAL_ERROR

if __name__ == "__main__":

    menu_options = {
        'a': create_user,
        'b': list_users,
        'c': update_user,
        'd': delete_user
    }

    while True:
        try:
            with CONNECT.cursor() as db:
                if not table_exists('users', db):
                    db.execute(USERS_TABLE)
                    CONNECT.commit()

                for function in menu_options.values():
                    print(function.__doc__)

                print("Q - Salir del programa")
                option_selected = input("Selecciona una opción válida: ").lower()

                if option_selected == "q":
                    break

                function_menu = menu_options.get(option_selected, default)
                function_menu(CONNECT, db)

        except OPERATIONAL_ERROR as err:
            print(f'Ha ocurrido el siguiente error: {err}')