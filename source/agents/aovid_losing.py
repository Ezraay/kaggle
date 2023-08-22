import random
import copy
from core.board import Board
from random_agent import RandomAgent

class Nolose(RandomAgent):
    def avoid_lose(self, board: Board, my_piece: int) -> int:
        move = self.immediate_win(board,my_piece)
        if move != None:
            return move
        block = self.opp_win(board,my_piece)
        if block != None:
            return block
        return random.choice(self.look_ahead_1(board,my_piece))


    def immediate_win(self,board:Board,my_piece) :
        
        options = [x for x in list(range(board.width)) if board.can_make_move(x)]
        # vertical win'
        for i in options:
            x = board.__heights[i]
            if x >= 3:
                win = True
                for j in range(3):
                    if board[x-i][i] != my_piece:
                        streak = False
                if win:
                    return i
        #horizontal win
        for i in options:
            if i - 3 >= 0:
                for j in range(3):
                    

                              

        return None
    

    def opp_win(self,board,my_piece):
        if my_piece = 1:
            opp_piece = 2
        else:
            opp_piece = 1
        return self.immediate_win(board,opp_piece)
        

    def look_ahead_1(self,board:Board,my_piece):
        c = copy.deepcopy(board)
        if my_piece = 1:
            opp_piece = 2
        else:
            opp_piece = 1
        options = [x for x in list(range(board.width)) if board.can_make_move(x)]
        no_move = []
        for i in range(len(options)):
            c.make_move(options[i])
            if self.immediate_win(c,opp_piece) != None:
                no_move.append = options[i]
            c.__board[c.__heights][options[i]] == 0
            c.__heights -= 1
        no_lose_opt = [x for x in options if x not in no_move]
        return no_lose_opt

            


        




        

        