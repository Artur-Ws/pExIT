age = 450

class User:
    age = 0
    name = ""

    def print_age(self, message):
        print(f"name: {self.name}, age: {self.age}, message: {message}")
    
    def another_method(self):
        pass

user_1 = User()
user_2 = User()

user_1.name = "Areczek"
user_1.age = 21
user_1.print_age("sample text")

user_2.name = "Mireczek"
user_2.age = 37
user_2.print_age("sample text")
