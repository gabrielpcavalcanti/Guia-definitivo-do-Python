class User:

    def __init__(self, first_name: str, last_name: str, id: str, age: int):
        
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.age = age

        self.login_attempts = 0

    
    def discribe_user(self):

        print(f"Nome: {self.first_name} {self.last_name}")
        print(f"ID: {self.id}")
        print(f"Idade: {self.age}")

    
    def greet_user(self):

        print(f"Bem-vindo, {self.first_name} {self.last_name}!")

    
    def increment_login_attempts(self):

        self.login_attempts += 1
    

    def reset_login_attempts(self):

        self.login_attempts = 0


# user1 = User("Gabriel", "Cavalcanti", "12345", 25)

# for i in range(10):
#     user1.increment_login_attempts()

# print(user1.login_attempts)

# user1.reset_login_attempts()

# print(user1.login_attempts)

class Privileges:

    def __init__(self, privileges: list[str]):
        
        self.privileges = privileges
    
    def show_privileges(self):
        """Mostra os privilégios que o admistrador possui."""

        for i in self.privileges:
            print(i)


class Admin(User):

    def __init__(self, first_name: str, last_name: str, id: str, age: int):
        super().__init__(first_name, last_name, id, age)

        self.privileges = Privileges(["priv 01", "priv 02"])


admin01 = Admin("Gabriel", "Cavalcanti", "12345", 25)

admin01.privileges.show_privileges()