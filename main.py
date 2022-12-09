from pick import pick
from mail import sendmessage
import database
cursor = database.connect_to_database()
clients = database.get_clients(cursor)
hobby_messages= database.get_hobby_messages(cursor)
age_messages= database.get_age_messages(cursor)
hobby_options=[]
age_options=[]

def get_age_range(age):
    return age.split('-')

for client in clients:
    hobby_options.append(client.hobby)
    client.print()
for hobby_message in hobby_messages:
    hobby_message.print()
for age_message in age_messages:
    age_options.append(age_message.age)
    age_message.print()

while True:
    title = 'Please choose:'
    mailing_options = ['Hobby', 'Age']
    option = pick(mailing_options + ['Exit'], title, indicator="=>")
    if (option[0] == "Exit"):
        break
    if(option[0] == "Hobby"):
        title = 'Please choose:'
        option = pick(list(set(hobby_options)) + ['Back'], title, indicator="=>")
        if (option[0] == "Back"):
            continue
        emails = []
        for client in clients:
            if (client.hobby == option[0]):
                emails.append(client.email)
        for hobby_message in hobby_messages:
            if (hobby_message.hobby == option[0]):
                sendmessage(emails, hobby_message.message)
    if(option[0] == "Age"):
        title = 'Please choose:'
        option = pick(age_options + ['Back'], title, indicator="=>")
        if (option[0] == "Back"):
            continue
        emails = []
        age_range = get_age_range(option[0])
        for client in clients:
            if (int(age_range[0]) <= int(client.age) < int(age_range[1])):
                emails.append(client.email)
        for age_message in age_messages:
            if (age_message.age == option[0]):
                sendmessage(emails, age_message.message)

