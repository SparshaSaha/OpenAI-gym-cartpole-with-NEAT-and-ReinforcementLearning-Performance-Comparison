import neat

class Agent(neat.DefaultGenome):

    def __init__(self, key):
        super().__init__(key)

        # Define score
        self.fitness = 0

    def configure_new(self, config):
        super().configure_new(config)
    

    def configure_crossover(self, genome1, genome2, config):
        super().configure_crossover(genome1, genome2, config)
    

    def mutate(self, config):
        super().mutate(config)
    

    def distance(self, other, config):
        return super().distance(other, config)
