import gym
from Agent import Agent
from GenerationStats import GenerationStats
import os
import neat
import pickle

class Game(object):
    
    def __init__(self, agent, config, environment):
        self.environment = environment
        self.environment.reset()
        self.maxScore = 1000
        self.agent = agent
        self.agent.fitness = 0
        self.agent.net = neat.nn.FeedForwardNetwork.create(self.agent, config)

    def sim(self):
        observation = (0.0, 0.0, 0.0, 0.0)
        self.environment.reset()
        while True:
            inputForNet = (observation[0], observation[1], observation[2], observation[3])
            outputFromNet = self.agent.net.activate(inputForNet)
            action = 0
            if outputFromNet[1] > outputFromNet[0]:
                action = 1
                
            observation, reward, done, info = self.environment.step(action) # take a random action
            self.agent.fitness += reward            
            
            self.environment.render()

            if done or self.agent.fitness > self.maxScore:
                break


class Simulate:

    def __init__(self):
        self.generationNumber = 0
        self.generationStats = []

    def main(self):
        local_dir = os.path.dirname(__file__)
        config_path = os.path.join(local_dir, 'config')
        config = neat.Config(Agent, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

        pop = neat.Population(config)
        stats = neat.StatisticsReporter()
        pop.add_reporter(stats)

        winner = pop.run(self.eval_genomes, 50)
        print("Writing generation Stats and best player metadata to file")
        with open('generationStatistics.pickle', 'wb') as handle:
            pickle.dump(self.generationStats, handle, protocol=pickle.HIGHEST_PROTOCOL)
        with open('bestAgent.pickle', 'wb') as handle:
            pickle.dump(winner, handle, protocol=pickle.HIGHEST_PROTOCOL)

    

    def eval_genomes(self, genomes, config):
        
        self.generationNumber += 1
        currentGeneration = GenerationStats(len(genomes), self.generationNumber)
        environment = gym.make('CartPole-v0')
        totalScore = 0
        for _, agent in genomes:
            g = Game(agent, config, environment)
            g.sim()
            totalScore += agent.fitness
            
        print("Generation: " + str(self.generationNumber) + " simluation over")
        currentGeneration.setTotalScore(totalScore)
        currentGeneration.calculateHighestScore(genomes)
        self.generationStats.append(currentGeneration)
        

s = Simulate()
s.main()
    
