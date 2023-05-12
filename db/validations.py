
def user_exists(username, email, cursor):
    query = "SELECT * FROM users WHERE username = %s AND email = %s;"
    values = (username, email)
    cursor.execute(query, values)
    result = cursor.fetchone()

    if result:
        return True
    else:
        return False
