class StoreTickData(object):

    scripName=None
    priceToAlphabetDict={}

    def __init__(self,scripName):
        self.scripName=scripName

    def isAlphabetAlreadyIncludedInTheTick(self,price,timeframeAlphabet):
        if price not in self.priceToAlphabetDict:
            self.priceToAlphabetDict[price]=[timeframeAlphabet]
        else:
            timeframeAlphabetList=self.priceToAlphabetDict[price]
            if timeframeAlphabetList.count>0:
                timeframeAlphabetList.append(timeframeAlphabet)
            else:
                timeframeAlphabetList=[timeframeAlphabet]
            self.priceToAlphabetDict[price]=timeframeAlphabetList