import csv
import pandas
import matplotlib.pyplot as plt
import sys

"""A script that finds '|' characters in a .txt file, indicates their
position, gives a total number of needles, create a scatterplot of those needle
coordinates, and a histogram of those coordinates."""

def find(file_name):
    file = open(file_name, 'r')
    output = open('data.csv', 'w')
    writer = csv.writer(output)
    column = 0
    row = 0
    needle_total = 0
    fields = ['needle','row_location','column_location']
    data = []
    for line in file:
        row += 1
        for char in line:
            column += 1
            if char == '|':
                needle_total += 1
                print("needle at: " +str(row) + "," + str(column))
                data.append([needle_total, row, column])
        column = 0
    writer.writerow(fields)
    writer.writerows(data)
    file.close()
    output.close
    return needle_total

if __name__ == '__main__':
    file_path = sys.argv[1]
    find(file_path)
    dataframe = pandas.read_csv('data.csv')
    plt.scatter(dataframe.row_location, dataframe.column_location)
    plt.xlabel("Row")
    plt.ylabel("Column")
    plt.savefig("needle_location.png")


