from collections import OrderedDict
import time
class StoreTickData(object):

    scripName=None
    priceToAlphabetsDict={}
    timeFrameToAlphabetList={}
    startTime=None
    endTime=None
    profileAlphabetsArray=None
    timeFrame=None
    doStoreOnlyInHeap=None

    def __init__(self,scripName,marketStartTime,marketEndTime,profileAlphabetsArray,timeFrame,doStoreOnlyInHeap):

        self.scripName=scripName
        self.startTime=marketStartTime
        self.endTime=marketEndTime
        self.profileAlphabetsArray=profileAlphabetsArray
        self.timeFrame=timeFrame
        self.doStoreOnlyInHeap=doStoreOnlyInHeap
        self._mapTimePeriodsToAlphabets(self.timeFrame,self.profileAlphabetsArray,self.startTime,self.endTime)


    def _isAlphabetAlreadyIncludedInTheTick(self,price,timeframeAlphabet):


        if price not in self.priceToAlphabetsDict:
            self.priceToAlphabetsDict[price]=[timeframeAlphabet]
            print self.priceToAlphabetsDict
            return False
        else:
            timeframeAlphabetsList=self.priceToAlphabetsDict[price]

            if timeframeAlphabet in timeframeAlphabetsList:
                return True
            else:
                timeframeAlphabetsList.append(timeframeAlphabet)
                self.priceToAlphabetsDict[price] = timeframeAlphabetsList
                print self.priceToAlphabetsDict
                return False


    def _get_sec(self,s):
        l = s.split(':')
        return int(l[0]) * 3600 + int(l[1]) * 60 + int(l[2])

    def _findCorrespondingAlphabetForGivenTime(self,timeInSeconds,timeFrameToAlphabetList):
        timeFrameToAlphabetList=OrderedDict(sorted(timeFrameToAlphabetList.items(), key=lambda t: t[1]))
        previousKey=None
        for key in timeFrameToAlphabetList:
            intKey=int(key)
            intTimeInSeconds=int(timeInSeconds)
            if intKey > intTimeInSeconds:
                return timeFrameToAlphabetList[previousKey]
            previousKey=intKey



    def _mapTimePeriodsToAlphabets(self,timeFrameInMin,profileAlphabetArray,startTime,EndTime):

        startTimeInSeconds=self._get_sec(startTime)
        endTimeInSeconds=self._get_sec(EndTime)
        num=startTimeInSeconds
        timeFrameInSeconds=timeFrameInMin*60;
        counter=0;

        while num < endTimeInSeconds:
            self.timeFrameToAlphabetList[num]=profileAlphabetArray[counter]
            counter=counter+1
            num=num+timeFrameInSeconds

    def execute(self,price,timeInSeconds):
        correcpondingAlphabet=self._findCorrespondingAlphabetForGivenTime(timeInSeconds,self.timeFrameToAlphabetList)
        if self.doStoreOnlyInHeap==True:
            self._isAlphabetAlreadyIncludedInTheTick(price,correcpondingAlphabet)

    def executeWithPriceOnly(self, price):
        currenTime=time.strftime("%H:%M:%S")
        timeInSeconds=self._get_sec(currenTime)
        correcpondingAlphabet = self._findCorrespondingAlphabetForGivenTime(timeInSeconds, self.timeFrameToAlphabetList)
        if self.doStoreOnlyInHeap == True:
            self._isAlphabetAlreadyIncludedInTheTick(price, correcpondingAlphabet)



if __name__ == '__main__':
    obj=StoreTickData("nifty","9:15:00","15:30:00",["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"],30,True)
    obj.execute(121,33300)
    obj.executeWithPriceOnly(121)
    obj.executeWithPriceOnly(122)
    obj.executeWithPriceOnly(121)
    obj.executeWithPriceOnly(124)
    print obj.priceToAlphabetsDict











