# Python OOP


class Employee:

    num_of_emps = 0
    raise_amount = 1.04 # class variable

    def __init__(self, first,last,pay):
        # Instance variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        # Class variable
        Employee.num_of_emps += 1

    def fullname(self):
        return self.first + ' ' + self.last

    # Video 2
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_emps)
emp_1 = Employee('ryan','sad',50000)
emp_2 = Employee('test','user',60000)

emp_1.raise_amount = 1.05
print(emp_1.__dict__)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.num_of_emps)
