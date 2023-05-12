DROP_USERS_TABLE = "DROP TABLE IF EXISTS users"

USERS_TABLE = """CREATE TABLE users(
    id SERIAL,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""

def table_exists(table, cursor):
    cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = %s)", (table,))
    exists = cursor.fetchone()[0]
    if exists:
        return True
    else:
        return False
