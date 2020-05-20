import BoardUtil
# This is a class for encoding the 8 Queens problem


# State defines the board as position in the string is the column
# and the value on the position is the row
class Board:
    def __init__(self, state="01234567", transition_model=False, move=(0,1) ):
        if type(state) != list:
            self.state = list(state)
        else:
            self.state = state
        # self.state = state
        if transition_model:
            self.move(move)


    def move(self, pos):
        self.state[pos[0]] = str(pos[1])

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
        self.threats = BoardUtil.calculateAllThreats(self.state)
        for row in reversed(range(len(self.state))):
            for col in self.state:
                res += "[Q]" if int(col) == row else "[ ]"
            res += "\n"
        res += "Number of threats: " + str(self.threats)
        res += " | State : " + str(self.state)
        return res

    def heuristicRepr(self):
        print("HEURISTIC")
        h_lst = []
        for row in range(0,len(self.state)):
            temp_lst = []
            for col in range(0,len(self.state)):
                temp_state = self.state.copy()
                temp_state[col] = str(row)
                # print(temp_state)
                h_threat = BoardUtil.calculateAllThreats(temp_state)
                temp_lst.append(h_threat)
            h_lst.insert(0,temp_lst)
        
        rep = ""
        for l in h_lst:
            for k in l:
                rep += "[ " + str(int(k)) + "]" if k<10 else "[" + str(int(k)) +"]"
            rep += "\n"
        print(rep)
                    
    def get(self):
        return self.state
    
    def __sizeof__(self):
        return len(self.state)
    
    def __len__(self):
        return len(self.state)
        


# board = Board("46152030",transition_model=True,move=((7,0),(7,7)))
# print(Board("13637441"))