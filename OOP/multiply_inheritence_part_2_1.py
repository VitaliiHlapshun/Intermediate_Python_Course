class Employee():
    new_id = 1

    def __init__(self, surname):
        self.surname = surname
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print("My id is {}.".format(self.id))


class User:
    def __init__(self, username, role="Customer"):
        self.username = username
        self.role = role

    def say_user_info(self):
        print("My username is {}".format(self.username))
        print("My role is {}".format(self.role))


# Write your code below
class Admin(Employee, User):
    def __init__(self):
        super().__init__(self)
        self.age = self.id
        user = User(self.surname)
        a = User.__init__(self, 'self.surname', user.username.upper())

    def say_id(self):
        super().say_id()
        print("I am an admin.")


e1 = Employee('Hlapshun')
print(e1.__dict__)
e2 = User(e1.surname, role="Notcustomer")
print(e2.__dict__)
print(e2.say_user_info())
