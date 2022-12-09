import pyodbc
from client import Client
from hobby_mailing import HobbyMailing
from age_mailing import AgeMailing
def connect_to_database():
    try:
        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Helga\PycharmProjects\pythonProject4000\Database.accdb;'
        conn = pyodbc.connect(con_string)
        return conn.cursor()
    except pyodbc.Error as e:
        print("Error in Connection", e)
def get_clients(cursor):
    clients= []
    cursor.execute('SELECT * FROM Client')
    for row in cursor.fetchall():
        clients.append(Client(row[0], row[1], row[2], row[3]))
    return clients
def get_hobby_messages(cursor):
    hobby_messages= []
    cursor.execute('SELECT * FROM Hobby_Mailing')
    for row in cursor.fetchall():
        hobby_messages.append(HobbyMailing(row[0], row[1]))
    return hobby_messages
def get_age_messages(cursor):
    age_messages= []
    cursor.execute('SELECT * FROM Age_Mailing')
    for row in cursor.fetchall():
        age_messages.append(AgeMailing(row[0], row[1]))
    return age_messages