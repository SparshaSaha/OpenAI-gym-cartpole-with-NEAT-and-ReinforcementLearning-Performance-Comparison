import gym
from Agent import Agent
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
            print(self.agent.fitness)
            
loadAgent = None
with open('bestAgent.pickle', 'rb') as handle:
    loadAgent = pickle.load(handle)

local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, 'config')
config = neat.Config(Agent, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
environment = gym.make('CartPole-v0')
g = Game(loadAgent, config, environment)
print(loadAgent.fitness)
g.sim()
