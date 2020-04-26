# Idempotence = https://whatis.techtarget.com/definition/idempotence
"""Idempotence in programming and mathematics,
is a property of some operations such that no matter
how many times you execute them, you achieve the same result."""

# f(x)
# add_ten(num)
def add_ten(num):
    return num + 10


# not idempotence
print(add_ten(add_ten(10)))  # 30

#  idempotence
# abs = absolute value
# f(f(x)) = f(x)
print(abs(-10))
print(abs(abs(abs(-10))))

# SAMPLE : HTTP METHODS
# GET,PUT, DELETE - idempotence
# POST = not idempotence
"""
To illustrate, consider an elevator call button. As you press the button, 
it lights up and an elevator is sent to your floor. 
A few moments later, someone else joins you in the lobby. 
This person smiles at you and presses the illuminated button 
a second time. You smile back and chuckle to yourself as you're 
reminded that the command to call an elevator is idempotent.

Pressing an elevator call button a second, third, 
or fourth time has no bearing on the final result.
When you press the button, regardless of the number of times,
the elevator is sent to your floor. Idempotent systems, 
like the elevator, result in the same outcome no matter 
how many times identical commands are issued.
"""