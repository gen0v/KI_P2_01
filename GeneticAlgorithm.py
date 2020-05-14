import random
from Board import Board
from collections import Counter
import numpy

class GeneticAlgorithm:
    def __init__(self):
        self.fitness_all = 0
        self.probability = []

    def random_selection(self, population, fitness_fn) -> Board:
        return numpy.random.choice(population,1,self.probability)[0]

    def calc_fitness(self, population, fitness_fn):
        self.fitness_all = 0
        self.probability = []
        pop = population.copy()
        # print(population)
        for i in range(0,len(population)):
            # print(population[i])
            temp_fitness = fitness_fn(population[i])
            self.fitness_all += temp_fitness
            pop[i] = (population[i],temp_fitness)
        # (BOARD,FITNESS)
        for k in pop:
            self.probability.append( ((100/self.fitness_all)*k[1])   )
        

    def reproduce(self, x:Board, y:Board) -> Board:
        n = len(x.get())
        c = random.randint(0,n-1)
        return Board(x.get()[0:c] + y.get()[c:n])


    def mutate(self, child: Board) -> Board:
        n = len(child.get())-1
        col = random.randint(0,n)
        return Board(child.get(),True, (col,random.randint(0,n)))

    def evolution(self, population: Board, fitness_fn):
        found = False
        count,limit = 0,100 
        while not found and count < limit:
            new_population = []
            for i in population:
                # iterate through population
                # i is of type board
                self.calc_fitness(population,fitness_fn)
                x = self.random_selection(population,fitness_fn)
                y = self.random_selection(population,fitness_fn)
                # reproduce
                child = self.reproduce(x,y)
                # random probability for mutation
                # print(child)
                if(random.randint(0,100) <= 30):
                    child = self.mutate(child)
                new_population.append(child)
            population = new_population
            # not very elegant
            best_fitness = 0
            for a in population:
                temp_fitness = fitness_fn(a)
                if temp_fitness >= best_fitness:
                    # found with better fitness
                    if temp_fitness == 28:return a
                    best_fitness = temp_fitness
                    best_indiv = a
            count += 1
            print("Genertation: " + str(count) + " | Best: " + str(best_indiv.state) + " | " + str(best_indiv.calculateAllThreats()))
        return best_indiv
                        
                        
                
# b1 = Board("75316401")
# b2 = Board("76543210")
# b3 = Board("15326470")
# pop = [b1,b2,b3]
population_count = 500
pop = []
for p in range(population_count):
    r = ""
    for n in range(8):
        s = random.randint(0,7)
        random.seed(random.randint(0,1000))
        r += str(s)
    pop.append(Board(r))

g = GeneticAlgorithm()
print(g.evolution(pop,Board.calculateAllNonThreats))
# Test mutate
# print(g.mutate(b))

# Test reproduce
# print(g.reproduce(b1,b2))

# Test
# g.calc_fitness(pop,Board.calculateAllNonThreats)
        

