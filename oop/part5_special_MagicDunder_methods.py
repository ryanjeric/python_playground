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

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first,self.last,self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('ryan','sasa',50000)
emp_2 = Employee('test','user',60000)

print(len('test')) # print('test'.__len__())
print(len(emp_1)) # __len__

print(emp_1 + emp_2) # __add__

#print(emp_1)
#print(repr(emp_1)) # same as print(emp_1.__repr__())
#print(str(emp_1)) # same as print(emp_1.__str__())

#print(1+2) # print(int.__add__(1,2))
#print('a'+'b') # print(str.__add_('a','b')