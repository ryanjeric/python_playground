theBoard = {
    'top-L':' ','top-M':' ','top-R':'X',
    'mid-L': 'X', 'mid-M': 'X', 'mid-R': ' ',
    'low-L': 'O', 'low-M': 'O', 'low-R': 'O'
}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(theBoard)