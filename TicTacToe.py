import time
import random 
from time import sleep 
import sys
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"


NUM_SQUARES = 9
winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
moves=((1,7,3,9),(5,),(2,4,6,8))

print("This is a ASCII tic-tac toe game.")
print(" ")
print("Please press 'a' and 'enter' to continue")
answer1 = input(">")

if answer1 == "a":
  board=[i for i in range(0,9)]
player, computer = '',''
moves=((1,7,3,9),(5,),(2,4,6,8))
winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
tab=range(1,10)
def print_board():
    x=1
    for i in board:
        end = ' | '
        if x%3 == 0:
            end = ' \n'
            if i != 1: end+='---------\n';
        char=' '
        if i in ('X','O'): char=i;
        x+=1
        print(char,end=end)     
def select_char():
    chars=('X','O')
    if random.randint(0,1) == 0:
        return chars[::-1]
    return chars
def can_move(brd, player, move):
    if move in tab and brd[move-1] == move-1:
        return True
    return False
def can_win(brd, player, move):
    places=[]
    x=0
    for i in brd:
        if i == player: places.append(x);
        x+=1
    win=True
    for tup in winners:
        win=True
        for ix in tup:
            if brd[ix] != player:
                win=False
                break
        if win == True:
            break
    return win
def make_move(brd, player, move, undo=False):
    if can_move(brd, player, move):
        brd[move-1] = player
        win=can_win(brd, player, move)
        if undo:
            brd[move-1] = move-1
        return (True, win)
    return (False, False)
def computer_move():
    move=-1
    for i in range(1,10):
        if make_move(board, computer, i, True)[1]:
            move=i
            break
    if move == -1:
        for i in range(1,10):
            if make_move(board, player, i, True)[1]:
                move=i
                break
    if move == -1:
        for tup in moves:
            for mv in tup:
                if move == -1 and can_move(board, computer, mv):
                    move=mv
                    break
    return make_move(board, computer, move)
def space_exist():
  return board.count('X') + board.count('O') != 9
player, computer = select_char()
print('Player is [%s] and computer is [%s]' % (player, computer))
result='You both Lost!'
while space_exist():
    print_board()
    print(' You can move now, the numbers are [1-9] in order : ', end='')
    move = int(input())
    moved, won = make_move(board, player, move)
    if not moved:
        print('That is an invalid space; please try again')
        continue
    if won:
        result='You Won! and your prise...nothing!'
        break
    elif computer_move()[1]:
        result="You Lost! Computers win again... ヽ(⌐■_■)ノ♪♬"
        break;
print_board()
print(result)
