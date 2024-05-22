import sqlite3


# Connect to SQLite and create a database file
conn = sqlite3.connect("my_database")


# Create a cursor object using the connection
cursor = conn.cursor()


# create user table
def create_user_table() -> bool:
    query = "CREATE TABLE user (ID INTEGER PRIMARY KEY  AUTOINCREMENT, name TEXT, surname TEXT, email TEXT, phone TEXT,profile_description TEXT, address TEXT,birthdate NUMERIC)"
    try:
        cursor.execute(query)
        conn.commit()
        return True
    except Exception as error:
        print("An exception occurred:", error.__name__)
    finally:
        conn.close()


def add_user(user: tuple) -> bool:
    query = "INSERT INTO user(name,surname,email,phone,profile_description,birthdate,address) VALUES(?,?,?,?,?,?,?)"
    try:
        cursor.execute(query, user)
        conn.commit()
        return True
    except Exception as error:
        print("An exception occurred:", error)
    finally:
        conn.close()


user = (
    "asgar",
    "ismayilov",
    "esger21@gmail.com",
    "+994775685605",
    "Python,Java,JS",
    "21.02.1997",
    "Nakhchivan",
)

# add_user(user)


def showAllUserInfo() -> list:
    query = "SELECT * FROM user"
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        conn.commit()

        return data
    except Exception as error:
        print("An exception occurred:", error)
    finally:
        conn.close()


# print(showAllUserInfo())


def showUserByID(id: int) -> list:
    query = "SELECT * FROM user WHERE ID = ?"
    try:
        cursor.execute(query, (id,))
        data = cursor.fetchall()
        conn.commit()

        return data
    except Exception as error:
        print("An exception occurred:", error)
    finally:
        conn.close()


# print(showUserByID(1))


def update_user_by_id(user: tuple, id: int) -> bool:
    query = f"UPDATE user SET name =?,surname=?,email=?,phone=?,profile_description=?,birthdate=?,address=? WHERE ID = {id}"
    try:
        cursor.execute(query, (user))
        conn.commit()
        return True
    except Exception as error:
        print("An exception occurred:", error)
        return False
    finally:
        conn.close()


user2 = (
    "asgar",
    "ismayilov",
    "esger21@gmail.com",
    "+99477xxxxxxx",
    "Python-Java-JS Developer",
    "21.02.1997",
    "Nakhchivan",
)
id = 1
# print(update_user_by_id(user2, id))


def update_user_by_property(property: str, value: str, id: int) -> bool:
    query = f"UPDATE user SET {property} = ? WHERE ID = ?"
    try:
        cursor.execute(query, (value, id))
        conn.commit()
        return True
    except Exception as error:
        print("An exception occurred:", error)
        return False
    finally:
        conn.close()


# print(update_user_by_property("surname", "ISMAYILOV", 1))


def delete_user_by_id(id: int) -> bool:
    query = "DELETE FROM user WHERE ID = ?"
    try:
        cursor.execute(query, (id,))
        conn.commit()
        return True
    except Exception as error:
        print("An exception occurred:", error)
        return False
    finally:
        conn.close()
