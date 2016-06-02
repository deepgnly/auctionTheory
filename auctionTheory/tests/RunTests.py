import unittest

import os
from auctionTheory.src import StoreTickData
from auctionTheory.tests import HTMLTestRunner

class RunTests(object):

    def executeTests(self):
        # get the directory path to output report file
        static_folder_root=os.path.dirname(os.path.dirname(__file__))

        # get all tests from SearchProductTest and HomePageTest class
        search_tests = unittest.TestLoader().loadTestsFromModule(StoreTickData,)

        # create a test suite combining search_test and home_page_test
        smoke_tests = unittest.TestSuite([search_tests])



        # open the report file
        outfile = open("Test.html", "w")

        # configure HTMLTestRunner options
        runner = HTMLTestRunner.HTMLTestRunner(
                         stream=outfile,
                         title='Test Report',
                         description='Smoke Tests'
                         )

        # run the suite using HTMLTestRunner
        runner.run(smoke_tests)

if __name__ == "__main__":
    obj=RunTests()
    obj.executeTests()
