import random
from Board import Board
import BoardUtil
from collections import Counter
import numpy

class GeneticAlgorithm:
    def __init__(self):
        self.fitness_all = 0
        self.probability = []
        self.fitness = []
        self.pop = []

    def random_selection(self, population, fitness_fn) -> Board:
        return numpy.random.choice(population,1,self.probability)[0]

    def calc_fitness(self, population, fitness_fn):
        self.fitness_all = 0
        self.probability = []
        self.pop = population.copy()
        # print(population)
        for i in range(0,len(population)):
            # print(population[i])
            temp_fitness = fitness_fn(population[i])
            self.fitness_all += temp_fitness
            self.pop[i] = (population[i],temp_fitness)
        # (BOARD,FITNESS)
        for k in self.pop:
            self.probability.append( ((100/self.fitness_all)*k[1])   )
        

    def reproduce(self, x:Board, y:Board) -> Board:
        n = len(x.get())
        c = random.randint(0,n-1)
        return (Board(x.get()[0:c] + y.get()[c:n]), Board(y.get()[0:c] + x.get()[c:n]))
        


    def mutate(self, child: Board) -> Board:
        n = len(child.get())-1
        col = random.randint(0,n)
        return Board(child.get(),True, (col,random.randint(0,n)))

    def evolution(self, population: Board, fitness_fn):
        found = False
        count,limit,count_cross = 0,100,0
        while not found and count < limit:
            new_population = []
            self.calc_fitness(population,fitness_fn)
            
            best_fitness = 0
            count_cross = 1

            for i in range(0,len(population)):

                temp_fitness = self.pop[i][1]
                if temp_fitness >= best_fitness:
                    # found with better fitness
                    if temp_fitness == 28:return self.pop[i][0]
                    best_fitness = temp_fitness
                    best_indiv = self.pop[i][0]
                
                
                # iterate through population
                # i is of type board
                if count_cross % 2 == 0:
                    x = self.random_selection(population,fitness_fn)
                    y = self.random_selection(population,fitness_fn)
                    # reproduce
                    childs = self.reproduce(x,y)
                    

                    # random probability for mutation
                    # print(child)
                    if(random.randint(0,100) <= 30):
                        child1 = self.mutate(childs[0])
                        child2 = self.mutate(childs[1])
                        childs = (child1, child2)
                    new_population.append(childs[0])
                    new_population.append(childs[1])

                count_cross += 1
            population = new_population
            print("Population: " + str(len(population)))
            # not very elegant
            # best_fitness = 0
            # for a in population:
            #     temp_fitness = fitness_fn(a)
            #     if temp_fitness >= best_fitness:
            #         # found with better fitness
            #         if temp_fitness == 28:return a
            #         best_fitness = temp_fitness
            #         best_indiv = a
            count += 1
            print("Genertation: " + str(count) + " | Best: " + str(best_indiv.state) + " | " + str(best_fitness) + " | " + str(((100/self.fitness_all)*best_fitness)))
        return best_indiv
                        
                        
                
# b1 = Board("75316401")
# b2 = Board("76543210")
# b3 = Board("40731624")
# pop = [b1,b2,b3]
population_count = 1000
pop = []
for p in range(population_count):
    r = ""
    for n in range(8):
        s = random.randint(0,7)
        # random.seed(random.randint(0,1000))
        r += str(s)
    pop.append(Board(r))

g = GeneticAlgorithm()
print(g.evolution(pop,BoardUtil.calculateAllNonThreats))
# Test mutate
# print(g.mutate(b))

# Test reproduce
# print(g.reproduce(b1,b2))

# Test
# g.calc_fitness(pop,Board.calculateAllNonThreats)
        

