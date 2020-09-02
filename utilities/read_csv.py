import csv

def getCSVData(fileName):
    # Empty list to store rows
    rows = []
    rowsNum = 0
    # Open csv
    csvDataFile = open(fileName, "r")
    # Create csv reader
    csvReader = csv.reader(csvDataFile)
    # Header skip
    next(csvReader)

    for row in csvReader:
        rows.append(row)
        rowsNum += 1

    return rows


