theBoard = { 'top-l': ' ', 'top-M': ' ', 'top-r' : ' ',
             'mid-l': ' ', 'mid-M': ' ', 'mid-r' : ' ',
             'low-l': ' ', 'low-M': ' ', 'low-r' : ' '}

def printboard(board):
    print(board['top-l'] + '|' + board['top-M'] + '|' + board['top-r'])
    print('-+-+-')
    print(board['mid-l'] + '|' + board['mid-M'] + '|' + board['mid-r'])
    print('-+-+-')
    print(board['low-l'] + '|' + board['low-M'] + '|' + board['low-r'])



turn = 'X'

for i in range(9):
    printboard(theBoard)
    print('trun for ' + turn + ' move to which space')
    move = input()
    theBoard[move] = turn
    if move != turn:
        print('wtf try again dumbo')
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printboard(theBoard)
    

    

