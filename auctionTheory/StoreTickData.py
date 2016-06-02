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
            return False
        else:
            timeframeAlphabetsList=self.priceToAlphabetsDict[price]

            if timeframeAlphabet in timeframeAlphabetsList:
                return True
            else:
                timeframeAlphabetsList.append(timeframeAlphabet)
                self.priceToAlphabetsDict[price] = timeframeAlphabetsList
                return False

    def _get_sec(self,s):
        l = s.split(':')
        return int(l[0]) * 3600 + int(l[1]) * 60 + int(l[2])

    def _findCorrespondingAlphabetForGivenTime(self,timeInSeconds,timeFrameToAlphabetList):
        for key in timeFrameToAlphabetList:
            intKey=int(key)
            val=timeFrameToAlphabetList[key]
            intTimeInSeconds=int(timeInSeconds)
            if intKey > intTimeInSeconds:
                return val



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


if __name__ == '__main__':
    obj=StoreTickData("nifty","9:15:00","15:30:00",["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"],30,True)
    obj.execute(121,3000)











