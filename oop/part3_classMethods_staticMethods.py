# Python OOP
import  datetime

class Employee:
    num_of_emps = 0
    raise_amount = 1.04  # class variable

    def __init__(self, first, last, pay):
        # Instance variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        # Class variable
        Employee.num_of_emps += 1

    def fullname(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # classmethod decorator
    @classmethod
    def set_raise_amt(cls, amount):  # cls = class
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)

    # static method decorator
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


my_date = datetime.date(2020,4,20)
print(Employee.is_workday(my_date))

emp_1 = Employee('ryan', 'sasa', 50000)
emp_2 = Employee('test', 'user', 60000)

emp_str1 = 'John-Doe-70000'
emp_str2 = 'Steve-Smith-0000'
emp_str3 = 'Jane-Doe-80000'

new_emp1 = Employee.from_string(emp_str1)

print(new_emp1.email)
print(new_emp1.pay)


Employee.set_raise_amt(1.05) # same as Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)