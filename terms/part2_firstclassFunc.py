# First-Class Functions

def square(x):
    return x * x
f = square

print(square)
print(f(5))

def cube(x):
    return x * x *x


def my_map(func,arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(cube, [1,2,3,4,5])
print(squares)


# js

"""
function square(x) {
    return x * x
}
var f = square
console.log(square)
console.log(f(5))

function my_map(func, arg_list) {
    result = [];
    for(var i = 1,i <= arg_list.length;i++){
        result.push(func(i)
    }
    return result
}
var squares = my_map(square,[1,2,3,4,5])
console.log(squares)

function cube(x) {
    return x * x * x
}

"""


