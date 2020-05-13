import random
from Board import Board
from collections import Counter

class GeneticAlgorithm:
    def __init__(self):
        pass

    def reproduce(self, par_x: list, par_y: list):
        # print("-- PARENTS --")
        # print(par_x)
        # print(par_y)
        c = random.randint(0,len(par_x)-1)
        child = par_x[0:c] + par_y[c:len(par_x)]
        # print("== CHILD ==")
        # print(child)
        return child
    
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

    # TODO not so random 
    def random_selection(self, population, fitness_fn):
        fitness = 100
        for indiv in population:
            temp_fitness = fitness_fn(indiv)
            if(temp_fitness < fitness):
                best = indiv
                fitness = temp_fitness
        while True:
            res = population[random.randint(0,len(population)-1)]
            res_fit = fitness_fn(res)
            if(res_fit <= fitness and res_fit > fitness/2):break
        return res
        # return best


    def mutate(self, lst):
        print(lst)
        lst[random.randint(0,len(lst)-1)] = str(random.randint(0,len(lst)-1))
        return lst

    def evolution(self, population:list, fitness_fn, lim):
        limit = lim
        count = 0
        found = False
        while True:
            new_population = []
            for i in range(0,len(population)):
                x = self.random_selection(population, fitness_fn)
                y = self.random_selection(population, fitness_fn)
                child = self.reproduce(x,y)
                if(random.randint(0,10) < 3):
                    child = self.mutate(child)
                new_population.append(child)
            population = new_population
            for individual in population:
                print(individual)
                if(fitness_fn(individual) == 0 or count >= limit):
                    found = True
                    break
            if found : break
            count += 1
            print("-- Next --")
            print(count)
        # TODO return best individual
        return individual


ga = GeneticAlgorithm()
# print(ga.reproduce(list("01234567"),list("76543210")))
lst = []
lst.append(list("01234567"))

for k in range(10):
    r = ""
    for n in range(8):
        s = random.randint(0,7)
        random.seed(random.randint(0,1000))
        r += str(s)
    lst.append(list(r))

res = ga.evolution(lst ,ga.calculateAllThreats, 200)
print(res)
print(ga.calculateAllThreats(res))
b = Board(res)
# print(b)