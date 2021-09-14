class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@email"

    def fullname(first, last):
        return first + " " + last

    def get_email(first, last):
        print(f"{first}.{last}@email.com")


class Manager(Employee):
    pass


class Security(Employee):
    pass


class Branch(Manager):
    pass


class Tech(Manager):
    pass


# emp1 = Employee("Joe", "Biden")
# emp2 = Employee("Anita", "Mohan")
# print(emp1.fullname())
# print(emp2.fullname())
# print(emp1.email)
# emp1.get_email()

print(Employee.fullname("Joe", "Biden"))
print(Employee.fullname("Anita", "Mohan"))
Employee.get_email("Joe", "Biden")
Employee.get_email("Anita", "Mohan")
