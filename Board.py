# This is a class for encoding the 8 Queens problem
from collections import Counter

# State defines the board as position in the string is the column
# and the value on the position is the row
class Board:
    def __init__(self, state="75316427", transition_model=False):
        self.state = list(state)
        # self.moveQueen((0,0),(0,4))
        self.threats = self.calculateAllThreats(self.state)
        print(self)
        self.heuristicFunction()

    def calculateAllThreats(self, state) -> float:
        hor_threat, cross_threat = 0, 0
        # Horizontal threats
        z = state.copy()
        res = Counter(z)
        for n in res:
            # print(str(res[n]) + " --> " + str((res[n] * (res[n] - 1)) / 2) )
            hor_threat += ((res[n] * (res[n] - 1)) / 2)
        # print(hor_threat)
        # Cross threats
        for n in range(0,len(state)):
            down_list, up_list = ["X"],["X"]
            counter = 1
            a = int(state[n])
            for right in range(n,len(state)):
                down_list.append(str(a-counter))
                up_list.append(str(a + counter))
                counter += 1
            counter = 1
            for left in range(0,n):
                down_list.insert(0,str(a-counter))
                up_list.insert(0,str(a+counter))
                counter += 1
            cross_threat += self.matchLists(down_list, up_list, state)
            # print(up_list)
            # print(down_list)
        # print(cross_threat)
        return hor_threat + cross_threat

    # function matches lst1 and lst2 with the state list
    # and return the # of matches / 2 because every match is counted two times
    def matchLists(self, lst1, lst2, state) -> float:
        matches = 0
        for i in range(0,len(state),1):
            if state[i] == lst1[i] or state[i] == lst2[i]:
                matches += 1
        return matches / 2


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
        res += "Number of threats: " + str(self.threats)
        return res

    def heuristicFunction(self):
        print("HEURISTIC")
        h_lst = []
        for row in range(0,len(self.state)):
            temp_lst = []
            for col in range(0,len(self.state)):
                temp_state = self.state.copy()
                temp_state[col] = str(row)
                # print(temp_state)
                h_threat = self.calculateAllThreats(temp_state)
                temp_lst.append(h_threat)
            h_lst.append(temp_lst)
        
        rep = ""
        for l in h_lst:
            for k in l:
                rep += "[ " + str(int(k)) + "]" if k<10 else "[" + str(int(k)) +"]"
            rep += "\n"
        print(rep)
                    

        
            


board = Board()
