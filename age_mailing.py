class AgeMailing:
    def __init__(self, age, message):
        self.age = age
        self.message = message
    def print(self):
        print(f'"{self.age}", "{self.message}"')