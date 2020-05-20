from Board import Board
import BoardUtil
import copy

class BacktrackingSearch:

    def __init__(self):
        self.sol_count = 0
        
    
    def complement_intersection(self, lst1, lst2): 
        lst3 = [value for value in lst2 if value not in lst1] 
        return lst3 

    # return col of unassigned variable
    def select_unassigned_variable(self, csp):
        for i in range(0,len(csp)):
            # print(i)
            if int(csp[i]) == -1: return i


    def order_domain_values(self, var,assignment,csp):
        domain = []
        for i in range(0,len(csp)):
            domain.append(i)
        return self.complement_intersection(assignment, domain)

    def interference(self, csp, var, value):

        cspc = copy.deepcopy(csp)
        # print(csp)
        cspc.move((var,value))
        lst = []
        for i in cspc.get():
            if i != "-1" : 
                lst.append(i)
        # we need to calculate the maximal non attacking count of queens
        maxnon = 0
        for i in range(1,len(lst)):
            maxnon += i
        non = BoardUtil.calculateAllNonThreats(lst)
        # print("lst :" + str(lst))
        # print("non :" + str(non))
        if  non == maxnon:
            return False
        else:
            return True

    # assignment : Board
    # csp : set of variables 0,1,2,...,n for n-Queens-Problem
    def backtrack(self, assignment, csp):
        # if BoardUtil.calculateAllNonThreats(assignment) == 28:
        #     return assignment
        if len(assignment) == len(csp):
            self.sol_count += 1
            print(str(assignment) + " Solution number: " + str(self.sol_count))
            # return assignment

        var = self.select_unassigned_variable(csp.get())
        # print("Unassigned var is : " + str(var))
        for value in self.order_domain_values(var,assignment,csp.get()):
            # print("Value is : " + str(value))
            # if value is consitent with assignment
            if value not in assignment:

                # assignment[var] = value
                assignment.append(value)
                # print(assignment)

                interferences = self.interference(csp,var,value)
                # print(interferences)
                if interferences == False:
                    csp.move((var,value))
                    result = self.backtrack(assignment,csp)
                    
                    if result != False:
                        return result

                    csp.move((var,-1))
            # assignment[var] = -1
            # print("-----------")
            assignment.pop()
            # print(assignment)
            # print("-----------")
        return False



b1 = Board(["-1","-1","-1","-1","-1","-1","-1","-1"])
b2 = Board("76543210")
b3 = Board("40731624")

bt = BacktrackingSearch()

print(bt.backtrack([],b1))

# print(BoardUtil.calculateAllThreats([5,3,6,0,7,1,4,2]))
# print(BoardUtil.calculateAllThreats([6, 3, 1, 4, 7, 0, 2, 5]))
# print(BoardUtil.calculateAllThreats([7, 2, 0, 5, 1, 4, 6, 3]))
        