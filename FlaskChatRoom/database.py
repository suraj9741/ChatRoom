import os
import mysql.connector

from user import User

mydb = mysql.connector.connect(host="localhost", user="suraj", password="1234", auth_plugin='mysql_native_password', database="chatroom")

cursor = mydb.cursor()

def save_user(name, email, password):
    cursor.execute("select * from user")
    result = cursor.fetchall()
    for i in result:
        count = i[0]
        if i[0] == email:
            flag = False
            return 'Email already exist.'
        else:
            flag = True
    if flag == True:
        cursor.execute("INSERT INTO user(email, name, password) VALUES(%s, %s, %s)", (email, name, password))
        mydb.commit()
        return True

def get_user(email):
    cursor.execute("select * from user where email = %s ", (email,))
    result = cursor.fetchall()
    return User(result[0][0], result[0][1], result[0][2]) if result else None

def check_user(email, password):
    cursor.execute("select * from user where email = %s and password = %s ", (email, password))
    result = cursor.fetchall()
    if result:
        return True
    else:
        return False


def save(roomid):

    switcher = {
        1: "INSERT INTO room1 (name, email, message) VALUES ( %s, %s, %s);",

        2: "INSERT INTO room2 (name, email, message) VALUES ( %s, %s, %s);",

        3: "INSERT INTO room3 (name, email, message) VALUES ( %s, %s, %s);",

        4: "INSERT INTO room3 (name, email, message) VALUES ( %s, %s, %s);",

        5: "INSERT INTO room3 (name, email, message) VALUES ( %s, %s, %s);",

        6: "INSERT INTO room3 (name, email, message) VALUES ( %s, %s, %s);",

        7: "INSERT INTO room3 (name, email, message) VALUES ( %s, %s, %s);",

        8: "INSERT INTO room3 (name, email, message) VALUES ( %s, %s, %s);",

        9: "INSERT INTO room3 (name, email, message) VALUES ( %s, %s, %s);",

        10: "INSERT INTO room3 (name, email, message) VALUES ( %s, %s, %s);"
    }
    return switcher.get(roomid, "nothing")


def save_message(roomid, email, name, message):
    data = save(roomid)
    value = (name, email, message)
    cursor.execute(data, value)
    mydb.commit()
