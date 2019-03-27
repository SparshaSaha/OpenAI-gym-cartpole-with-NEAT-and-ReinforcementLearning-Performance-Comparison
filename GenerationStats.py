class GenerationStats(object):

    def __init__(self, noOfAgents, generationNumber):
        self.generationAverage = 0
        self.noOfAgents = noOfAgents
        self.totalScore = 0
        self.average = 0
        self.highestScore = 0
        self.generationNumber = generationNumber

    def setTotalScore(self, totalScore):
        self.totalScore = totalScore
        self.calculateAverage()

    def calculateAverage(self):
        self.average = (self.totalScore * 1.00) / (self.noOfAgents * 1.00)

    def calculateHighestScore(self, agents):
        for _, agent in agents:
            if self.highestScore < agent.fitness:
                self.highestScore = agent.fitness
    
            
            
        
