import matplotlib.pyplot as plt
class PlotMP(object):
    scripName="Default Scrip"
    maxX=0
    minX=0
    maxY=0
    minY=0
    currentDay=0
    ax=None
    allTextObj=[]
    dataForPlot={}

    def __init__(self,scripName,currentDay,maxX,minX,maxY,minY):
        self.maxX=maxX
        self.minX=minX
        self.maxY=maxY
        self.minY=minY
        self.scripName=scripName
        self.currentDay=currentDay
        self.plotInit(scripName,minX, maxX, minY, maxY)

    def flushAllTextObjects(self):
        for each in self.allTextObj:
            each.remove()
        self.allTextObj=[]

    def udpateDataForPlot(self,data):
        self.dataForPlot=data
        self.plot(data)

    def plot(self,timeFrameToAlphabetListSorted):
        for price in timeFrameToAlphabetListSorted:
            alphabetList=timeFrameToAlphabetListSorted[price]
            alphabet = r' '.join(alphabetList)
            plt.yticks(range(self.minY, self.maxY))
            plt.xticks(range(self.minX, self.maxX))
            txt = self.ax.text(self.currentDay, price, alphabet, fontsize=10)
            mng = plt.get_current_fig_manager()
            mng.resize(*mng.window.maxsize())
            totalSizeOfDictionary=len(timeFrameToAlphabetListSorted)
            if totalSizeOfDictionary >1:
                minVal=timeFrameToAlphabetListSorted.keys()[0]
                maxVal=timeFrameToAlphabetListSorted.keys()[totalSizeOfDictionary-1]
                plt.axhspan(ymin=minVal-1,ymax=maxVal,xmin=0, xmax=1,facecolor='0.5', alpha=0.5)
            plt.draw()
            plt.pause(0.001)


    def plotInit(self, scripName, minX, maxX, minY, maxY):
        plt.ion()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_autoscale_on(True)  # enable autoscale
        ax.autoscale_view(True, True, True)
        ax.set_title(scripName)
        ax.set_xlabel('Days')
        ax.set_ylabel('Price')
        ax.axis([minX, maxX, minY, maxY])
        self.ax = ax