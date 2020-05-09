# This is a class for encoding the 8 Queens problem
from collections import Counter

class Board:
    def __init__(self, state="11222255", transition_model=False):
        self.state = list(state)
        self.moveQueen((0,0),(0,4))
        self.calculateAllThreats()
        print(self)
    
    #TODO
    # tuple position should be like (col,row)
    def calculateThreat(self, pos: tuple):
        pass

    #TODO
    def calculateAllThreats(self):
        z = self.state.copy()
        res = Counter(z)
        for t in res:
            print(res[t])
        print(res)
        # for i in range(len(self.state)):
        #     for j in range(i,len(self.state),1):
        #         print(str(i) + " " + str(j))



    # TODO
    # tuple position should be like (col,row)
    def moveQueen(self, pos_from: tuple, pos_to: tuple):
        if int(self.state[pos_from[0]]) == pos_from[1] and pos_to[0] == pos_from[0]:
            self.state[pos_to[0]] = str(pos_to[1])
            print(self.state)
        else:
            print("Something went wrong moving the Queen! \
            \n[Queens can only be moved in their colums.]")

    def __repr__(self):
        res = ""
        for row in reversed(range(len(self.state))):
            for col in self.state:
                res += "[Q]" if int(col) == row else "[ ]"
            res += "\n"
        return res


            
        
            


board = Board()
