"""
This module asks the user to input the path to where the data is located and load it in the right format
"""

class classLoadData:

    @staticmethod
    def loadData():
        # Asks the user to input the path to the data
        inputPath = input("Enter the path where data is located e.g. '/Users/evelyn/Downloads/inputExample.txt' -> ")
        # Loads the data in the right format (as a list of lists)
        with open(inputPath) as f:
            data = [i.strip().split(',') for i in f]

        return data