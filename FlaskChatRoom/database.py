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


def save_message(roomid, email, name, message):
    switcher = {
        1:
            cursor.execute("INSERT INTO room1 (name, email, message) VALUES ( %s, %s, %s);", (name, email, message)),
        2:
            cursor.execute("INSERT INTO room2 (name, email, message) VALUES ( %s, %s, %s);", (name, email, message)),
        3:
            cursor.execute("INSERT INTO room3 (name, email, message) VALUES ( %s, %s, %s);", (name, email, message)),
        4:
            cursor.execute("INSERT INTO room4 (name, email, message) VALUES ( %s, %s, %s);", (name, email, message)),
        5:
            cursor.execute("INSERT INTO room5 (name, email, message) VALUES ( %s, %s, %s);", (name, email, message)),
        6:
            cursor.execute("INSERT INTO room6 (name, email, message) VALUES ( %s, %s, %s);", (name, email, message)),
        7:
            cursor.execute("INSERT INTO room7 (name, email, message) VALUES ( %s, %s, %s);", (name, email, message)),
        8:
            cursor.execute("INSERT INTO room8 (name, email, message) VALUES ( %s, %s, %s);", (name, email, message)),
        9:
            cursor.execute("INSERT INTO room9 (name, email, message) VALUES ( %s, %s, %s);", (name, email, message)),
        10:
            cursor.execute("INSERT INTO room10 (name, email, message) VALUES ( %s, %s, %s);", (name, email, message)),
    }
    mydb.commit()

