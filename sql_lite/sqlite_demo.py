# https://www.youtube.com/watch?v=pd-0G0MigUA
import sqlite3
from employee import Employee

# :memory: - > Ram
# 'emp.db' - > file
conn = sqlite3.connect(':memory:')

c = conn.cursor()

# CREATE TABLE
c.execute("""CREATE TABLE employees(
        first text,
        last text,
        pay integer
        )""")


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first,:last,:pay)",{'first': emp.first, 'last': emp.last, 'pay': emp.pay})

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_pay(emp,pay):
    with conn:
        c.execute("""UPDATE employees SET pay=:pay WHERE first=:first AND last=:last""",{'first':emp.first,'last':emp.last,'pay':pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE FROM employees WHERE first=:first AND last=:last",{'first':emp.first,'last':emp.last})


emp1 = Employee('John', 'Doe', 80000)
emp2 = Employee('Jane', 'Doe', 90000)

insert_emp(emp1)
insert_emp(emp2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp2,95000)
remove_emp(emp1)

emps = get_emps_by_name('Doe')
print(emps)


conn.close()

"""c.execute("INSERT INTO employees VALUES (?,?,?)",(emp1.first,emp1.last,emp1.pay))
conn.commit()
c.execute("INSERT INTO employees VALUES (:first,:last,:pay)",{'first':emp2.first,'last':emp2.last,'pay':emp2.pay})
conn.commit()
# SELECT
c.execute("SELECT * FROM employees WHERE last=?", ('Doe',))
# print(c.fetchone())
# c.fetchmany(5)
print(c.fetchall())
c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe'})
print(c.fetchall())

conn.commit()
conn.close()"""
