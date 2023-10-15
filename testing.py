from source.core.board import Board
from source.agents.smart_minimax_agent import SmartMinimaxAgent

b =  Board()
b.create((7,6))
# Vertical win for 2 
# m = [2,2,1,2,5,2,5]
# Horizontal for 1
# m = [0,6,1,6,2,1]
# Diagonal 
# negative win for 2 but in 1's turn
# m = [3,3,4,2,4,4,5,6,3,3]
# positive win for 2 in 2's turn
m = [3,3,4,2,4,4,5,6,3,3,5,5,4]


p = 2
for i in m:
    if p == 1:
        p = 2
    else:
        p = 1
    b.make_move(i,p)
#print(b)

# print(b.get_board_state(4))
a = SmartMinimaxAgent()
res = a.get_move(b,1,4)
print(res)


