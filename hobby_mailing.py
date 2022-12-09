class HobbyMailing:
    def __init__(self, hobby, message):
        self.hobby = hobby
        self.message = message
    def print(self):
        print(f'"{self.hobby}" , "{self.message}"')