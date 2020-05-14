import random
from Board import Board
from collections import Counter

class GeneticAlgorithm:
    def __init__(self):
        pass

    # TODO
    def random_selection(self, population, fitness_fn) -> Board:
        pass
    
    # TODO
    def reproduce(self, x, y) -> Board:
        pass

    #def
    def mutate(self, child) -> Board:
        pass

    def evolution(self, population: Board, fitness_fn):
        found = False
        count,limit = 0,100 
        while not found and count < limit:
            new_population = []
            for i in len(population):
                # iterate through population
                # i is of type board
                x = random_selection(population,fitness_fn)
                y = random_selection(population,fitness_fn)
                # reproduce
                child = reproduce(x,y)
                # random probability for mutation
                if(random.randint(0,100) <= 30):
                    child = mutate(child)
                new_population.append(child)
            population = new_population
            # not very elegant
            best_fitness = 100
            for a in population:
                temp_fitness = fitness_fn(a)
                if temp_fitness <= best_fitness:
                    # found with better fitness
                    if temp_fitness == 0:return a
                    best_fitness = temp_fitness
                    best_indiv = a
        return best_indiv
                        
                        
                


        

