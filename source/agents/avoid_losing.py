import random
import copy
import sys
sys.path.append('C:\\Users\\jacky\\Documents\\Uni\\y3s2\\FIT3163\\Project Kaggle\\kaggle\\source')
from core.board import Board
from random_agent import RandomAgent

class Avoid_Losing(RandomAgent):
    def get_move(self, board: Board, my_piece: int) -> int:
        move = self.immediate_win(board,my_piece)
        if move != None:
            return move
        block = self.opp_win(board,my_piece)
        if block != None:
            return block
        return random.choice(self.look_ahead_1(board,my_piece))


    def immediate_win(self,board:Board,my_piece:int) :
        options = [x for x in list(range(board.width)) if board.can_make_move(x)]
        for i in options:
            x = board.get_height_at(i)
            bo = board.to_array()
            # Vertical Win
            if x >= 3:
                if (bo[i][x-1] == my_piece 
                    and bo[i][x-2] == my_piece 
                    and bo[i][x-3] == my_piece):
                    return i
            # Horizontal left win
            win = True
            if i - 3 >= 0:
                if (bo[i-1][x] == my_piece 
                    and bo[i-2][x] == my_piece 
                    and bo[i-3][x] == my_piece):
                    return i
            # Horizontal Right Win
            if i + 3 < board.width -1:
                if (bo[i+1][x] == my_piece 
                    and bo[i+2][x] == my_piece 
                    and bo[i+3][x] == my_piece):
                    return i

            # Diagonal Win
            streak = 0
            board.make_move(i,my_piece)
            # Diagonal positive
            piece = my_piece
            # count streak go up right
            a,b = i+1,x+1
            while 0<=b<=board.height-1 and 0<=a<=(board.width -1):
                piece = bo[a][b]
                if piece != my_piece:
                    break
                streak +=1
                a +=1 
                b +=1
            # count streak go down left
            a,b = i-1,x-1
            while 0<=b<=board.height-1 and 0<=a<=(board.width -1):
                piece = bo[a][b]
                if piece != my_piece:
                    break
                streak +=1
                a -=1 
                b -=1
            # return win move
            if streak >= 3:
                board.unmake_move()
                return i
            # diagonal negative
            streak = 0
            piece = my_piece
            # count streak go up left
            a,b = i-1,x+1
            while 0<=b<=board.height-1 and 0<=a<=(board.width -1):
                piece = bo[a][b]
                if piece != my_piece:
                    break
                streak +=1
                a -=1 
                b +=1

            # count streak go down right
            a,b = i+1,x-1
            while 0<=b<=board.height-1 and 0<=a<=(board.width -1):
                piece = bo[a][b]
                if piece != my_piece:
                    break
                streak +=1
                a +=1 
                b -=1
            if streak >= 3:
                board.unmake_move()
                return i
            bo[i][x] = 0
        return None

    def opp_win(self,board,my_piece):
        if my_piece == 1:
            opp_piece = 2
        else:
            opp_piece = 1
        return self.immediate_win(board,opp_piece)
        

    def look_ahead_1(self,board:Board,my_piece):
        c = board
        if my_piece == 1:
            opp_piece = 2
        else:
            opp_piece = 1
        options = [x for x in list(range(board.width)) if board.can_make_move(x)]
        no_move = []
        for i in range(len(options)):
            ###
            p = options[i]
            board.make_move(p)
            if self.immediate_win(c,opp_piece) != None:
                no_move.append = options[i]
            ####
            board.unmake_move()
        no_lose_opt = [x for x in options if x not in no_move]
        return no_lose_opt


b =  Board()
b.create((7,6))
# m = [3,3,3,2,3,3,4,2,5,6,4,4,4,5,5]
# m = [3,3,2,3,4,3]
# m = [3,4,2,2,1,0,1,2,1,1,2,5]
# m = [4,4,3,5,2,1,4,2,3,3,4,3,4,4,3,1,5,6,5]
m = [4,3,5,6,4,4,5,5,3,6,6]
p = 2
for i in m:
    if p == 1:
        p = 2
    else:
        p = 1
    b.make_move(i,p)
print(b)

print(b.get_board_state(4))
a = Avoid_Losing()
res = a.get_move(b,2)
print(res)  




        

        