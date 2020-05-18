import Board, BoardUtil

class BacktrackingSearch:

    def __init__(self):
        pass
    
    # TODO better choice ?
    def select_unassigned_variable(self, csp):
        # res = csp[0] if len(csp) > 0 else None
        return csp[0] if len(csp) > 0 else None

    # assignment : Board
    # csp : set of variables 0,1,2,...,n for n-Queens-Problem
    def backtrack(self, assignment: Board, csp):
        if BoardUtil.calculateAllNonThreats(assignment) == 28:
            return assignment
        var = self.select_unassigned_variable(csp)