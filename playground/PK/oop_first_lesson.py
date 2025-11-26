age = 450

class User:
    age = 0
    name = ""
    def __init__(self, x, y):
        print("initialization")

        self.age = x
        self.name = y

    def print_age(self, message):
        print(f"name: {self.name}, age: {self.age}, message: {message}")
    
user_1 = User(21, 'Areczek')
user_2 = User(37, "Mireczek")

# user_1.name = "Areczek"
# user_1.age = 21
# user_1.print_age("sample text")

# user_2.name = "Mireczek"
# user_2.age = 37
# user_2.print_age("sample text")

# userList = [User(), User()]

# userList[0].age = 21
# userList[1].age = 37
# user_1.print_age("sample text")

# userList[0].name = 'Areczek'
# userList[1].name = "Mireczek"
# user_2.print_age("sample text")

user_1.print_age("sample text")

user_2.print_age("sample text")