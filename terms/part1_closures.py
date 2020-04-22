# CLOSURES
def outer_func(msg):
    message = msg

    def inner_func(msg2):
        print(message + ' ' + msg2)

    return inner_func


hi_func = outer_func('Hi')
hello_func = outer_func('Hello')

hi_func('World')
hello_func('World')
