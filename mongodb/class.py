class User:
    def __init__(self, name):
        self.name = name
        print(self.name)

kw = {"name": "wisdom"}
User(kw)
