# raise Exception('This is the Error message.')

def boxPrint(symbol, width, height):

    if len(symbol)!=1:
        raise  Exception('Symbol should be length 1')
    if (width < 2) or (height < 2):
        raise  Exception('Width and Height must be greater or equal to 2')


    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)


boxPrint('*', 15, 5)
boxPrint('0x', 5, 16)
boxPrint('0', 1, 1)