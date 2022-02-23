from abc import ABC, abstractmethod


class AbstractEmployee(ABC):
    new_id = 1

    def __init__(self):
        self.id = AbstractEmployee.new_id
        AbstractEmployee.new_id += 1

    @abstractmethod
    def say_id(self):
        pass


# Write your code below
class Employee(AbstractEmployee):
    def say_id(self):
        return self.id


e1 = Employee()
print(f"The id of the Employee is, {e1.say_id()}")
