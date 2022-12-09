class Client:
    def __init__(self, fullName, age, hobby, email):
        self.fullName = fullName
        self.age = age
        self.hobby = hobby
        self.email = email
    def print(self):
        print(f'"{self.fullName}" , "{self.age}" ,"{self.hobby}" ,"{self.email}" ')
