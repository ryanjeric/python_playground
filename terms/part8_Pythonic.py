"""
 https://www.youtube.com/watch?v=x3v9zMX1s4s
 Pythonic is an adjective that describes an approach to computer programming
 that agrees with the founding philosophy of the Python programming language"""


# DUCK typing and Easier to ask forgiveness than permission (EAFP)
class Duck:

    def quack(self):
        print('Quack,Quack')

    def fly(self):
        print('Flap,Flap!')


class Person:

    def quack(self):
        print("I'm Quacking like a duck")

    def fly(self):
        print("I'm Flapping my Arms!")


def quack_and_fly(thing):
    """
    # Not Duck-Typed (NON PYTHONIC)

    if isinstance(thing,Duck):
        thing.quack()
        thing.fly()
    else:
        print('This has to be a duck')

     # LBYL(Look Before You Leap) (NON PYTHONIC)
     # Before the writing the code statements, we need to check conditions;
     # if the conditions are met, our code will run and we won’t handle any exceptions.

    if hasattr(thing,'quack'):
        if callable(thing.quack):
            thing.quack()
    if hasattr(thing,'fly'):
        if callable(thing.fly):
            thing.fly()

    # Duck typing in computer programming is an application of the duck test
    #—"If it walks like a duck and it quacks like a duck, then it must be a duck

    thing.quack()
    thing.fly()
    """
    # EAFP - Easier to ask forgiveness than permission (PYTHONIC)
    try:
        thing.quack()
        thing.fly()
        # thing.bark() - prints error msg
    except AttributeError as e:
        print(e)


d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)
