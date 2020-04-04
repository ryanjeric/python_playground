print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats')
    elif int(numCats) < 0:
        print('Number should be greater than zero.')
    else:
        print('That is not that many cats.')
except ValueError:
    print('Not a number')