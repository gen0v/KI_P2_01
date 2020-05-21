from Board import Board
import BoardUtil
import copy
import timeit


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


    # return all possible usable values
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
        # return all possible values to use where to put the queen
        for value in self.order_domain_values(var,assignment,csp.get()):
            # print("Value is : " + str(value))
            # if value is consitent with assignment
            if value not in assignment:
                # assignment[var] = value
                # print(assignment)
                # print(value)

                if len(assignment) > 2 and abs(assignment[-1]-value) < 2:
                    # print("Len assignment: " + str(assignment))
                    # print("abs(assignment[-1]-value : " + str(abs(assignment[-1]-value)))
                    # print("assignment [-1]" + str(assignment[-1]))
                    # print("Value : " + str(value))
                    continue
                
                assignment.append(value)

                # see if there is a problem
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


b8 = Board(["-1","-1","-1","-1","-1","-1","-1","-1"])
b10 = Board(["-1","-1","-1","-1","-1","-1","-1","-1","-1","-1"])
b12 = Board(["-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1"])
bt = BacktrackingSearch()
bt.backtrack([],b12)




# Test time
# b10 = Board(["-1","-1","-1","-1","-1","-1","-1","-1","-1","-1"])
# code_to_test = """
# from BacktrackingSearch import BacktrackingSearch
# from Board import Board
# bt = BacktrackingSearch()
# b8 = Board(["-1","-1","-1","-1","-1","-1","-1","-1"])
# b12 = Board(["-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1"])
# bt.backtrack([],b12)
# """

# elapsed_time = timeit.timeit(code_to_test, number=1)/1
# print(elapsed_time)
   