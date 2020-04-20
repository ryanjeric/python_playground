# Python OOP
# Subclasses

class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        # Instance variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):  # inherit Employee class
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # same as #Employee.__init__(self,first,last,pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('sasa', 'meow', 50000, 'Python')
dev_2 = Developer('test', 'user', 60000, 'Java')
mgr_1 = Manager('sue','smith',9000,[dev_1])

# isinstance() - check if object an instance of a class
print(isinstance(mgr_1,Manager))
print(isinstance(mgr_1,Employee))
print(isinstance(mgr_1,Developer))
# issubclass() - check class is a subclass of another
print(issubclass(Manager,Employee))
print(issubclass(Developer,Employee))
print(issubclass(Employee,Employee))



#print(mgr_1.email)
#mgr_1.add_emp(dev_2)
#mgr_1.print_emps()


# print(help(Developer))
#print(dev_1.email)
print(dev_1.prog_lang)
# print(dev_2.email)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
