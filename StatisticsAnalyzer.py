import matplotlib.pyplot as plot
import pickle

class StatsAnalyzer(object):

    def __init__(self, pickleFiles):
        self.filenames = pickleFiles

    def plotData(self, dataPts, label):
        xCoords = dataPts[0]
        yCoords = dataPts[1]

        plot.plot(xCoords, yCoords, label = label)

    def handlePlot(self):
        lab = ["Average", "Highest"]
        f=0
        for i in self.filenames:
            loadedData = None
            with open(i, 'rb') as handle:
                loadedData = pickle.load(handle)
            xCoords = []
            yCoords = []

            for j in loadedData:
                yCoords.append(j.average)
                xCoords.append(j.generationNumber)
            self.plotData([xCoords, yCoords], lab[f])
            f += 1

            xCoords1 = []
            yCoords1 = []

            for j in loadedData:
                yCoords1.append(j.highestScore)
                xCoords1.append(j.generationNumber)
            self.plotData([xCoords1, yCoords1], lab[f])
        plot.legend()
        plot.show()

stats = StatsAnalyzer(["generationStatistics.pickle"])
stats.handlePlot()

            
                
