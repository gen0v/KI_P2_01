from collections import Counter

def calculateAllThreats(state) -> float:
    hor_threat, cross_threat = 0, 0
    # Horizontal threats
    state = state.get()
    z = state.copy()
    res = Counter(z)
    for n in res:
        # print(str(res[n]) + " --> " + str((res[n] * (res[n] - 1)) / 2) )
        hor_threat += ((res[n] * (res[n] - 1)) / 2)
    # print(hor_threat)
    # Cross threats
    for n in range(0, len(state)):
        down_list, up_list = ["X"], ["X"]
        counter = 1
        a = int(state[n])
        for right in range(n, len(state)):
            down_list.append(str(a-counter))
            up_list.append(str(a + counter))
            counter += 1
        counter = 1
        for left in range(0, n):
            down_list.insert(0, str(a-counter))
            up_list.insert(0, str(a+counter))
            counter += 1
        cross_threat += Board.matchLists(down_list, up_list, state)
        # print(up_list)
        # print(down_list)
    # print(cross_threat)
    return hor_threat + cross_threat

def calculateAllNonThreats(state) -> float:
    hor_threat, cross_threat = 0, 0
    # Horizontal threats
    state = state.get()
    z = state.copy()
    res = Counter(z)
    for n in res:
        # print(str(res[n]) + " --> " + str((res[n] * (res[n] - 1)) / 2) )
        hor_threat += ((res[n] * (res[n] - 1)) / 2)
    # print(hor_threat)
    # Cross threats
    for n in range(0, len(state)):
        down_list, up_list = ["X"], ["X"]
        counter = 1
        a = int(state[n])
        for right in range(n, len(state)):
            down_list.append(str(a-counter))
            up_list.append(str(a + counter))
            counter += 1
        counter = 1
        for left in range(0, n):
            down_list.insert(0, str(a-counter))
            up_list.insert(0, str(a+counter))
            counter += 1
        cross_threat += matchLists(down_list, up_list, state)
        # print(up_list)
        # print(down_list)
    # print(cross_threat)
    return 28 - (hor_threat + cross_threat)
    
# function matches lst1 and lst2 with the state list
# and return the # of matches / 2 because every match is counted two times

def matchLists(lst1, lst2, state) -> float:
    matches = 0
    for i in range(0, len(state),1):
        if state[i] == lst1[i] or state[i] == lst2[i]:
            matches += 1
    return matches / 2
