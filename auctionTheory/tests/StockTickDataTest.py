import unittest
from auctionTheory.src import StoreTickData

stockTickDataObj= StoreTickData()

class StockTickDataTest(unittest.TestCase):

    def test_executeTickData(self):
        obj = stockTickDataObj("nifty", "9:15:00", "15:30:00",
                            ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                             "S", "T"], 30, True)
        obj.execute(121, 34300)
        obj.execute(122, 34600)
        obj.execute(121, 35300)
        obj.execute(124, 50000)


def main():

    unittest.main()

if __name__ == '__main__':
    main()