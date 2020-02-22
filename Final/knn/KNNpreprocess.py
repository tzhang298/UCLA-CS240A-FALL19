import urllib.request as urllib
import numpy as np
import csv

size_limit = 2

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/hill-valley/Hill_Valley_without_noise_Testing.data"
raw_data = urllib.urlopen(url)
with open('testdata/woTesting.csv', 'wb') as file:
    file.write(raw_data.read())

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/hill-valley/Hill_Valley_without_noise_Training.data"
raw_data = urllib.urlopen(url)
with open('testdata/woTraining.csv', 'wb') as file:
    file.write(raw_data.read())


'''with open('testdata/woTesting.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    with open('testdata/test.csv', "w") as file:
        writer = csv.writer(file)
        row_number = 1
        for row in readCSV:
            col_number = 1
            for i in row[:-1]:
                    writer.writerow([row_number,col_number,i])
                    col_number=col_number+1
            row_number=row_number+1
            if row_number >size_limit:
                break

with open('testdata/woTraining.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    with open('testdata/train.csv', "w") as file:
        writer = csv.writer(file)
        row_number = 1
        for row in readCSV:
            col_number = 1
            for i in row[:-1]:
                    writer.writerow([row_number,col_number,i])
                    col_number=col_number+1
            row_number=row_number+1
            if row_number >size_limit:
                break

with open('testdata/woTraining.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    with open('testdata/labels.csv', "w") as file:
        writer = csv.writer(file)
        row_number = 1
        for row in readCSV:
            writer.writerow([row_number,row[-1]])
            row_number=row_number+1 '''

with open('testdata/woTraining.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    with open('testdata/labels.csv', "w") as file:
        writer = csv.writer(file)
        row_number = 1
        for row in readCSV:
            writer.writerow([row_number,row[-1]])
            row_number=row_number+1

with open('testdata/woTesting.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    with open('testdata/TESTDATA.csv', "w") as file:
        writer = csv.writer(file)
        row_number = 1
        for row in readCSV:
            col_number = 1
            for i in row[:-1]:
                    writer.writerow([row_number,col_number,i,row[-1]])
                    col_number=col_number+1
            row_number=row_number+1
            if row_number >size_limit:
                break

with open('testdata/woTraining.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    with open('testdata/TRAINDATA.csv', "w") as file:
        writer = csv.writer(file)
        row_number = 1
        for row in readCSV:
            col_number = 1
            for i in row[:-1]:
                    writer.writerow([row_number,col_number,i,row[-1]])
                    col_number=col_number+1
            row_number=row_number+1
            if row_number >size_limit:
                break


with open('testdata/woTraining.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    with open('testdata/train.txt', "w") as file:
        row_number = 1
        for row in readCSV:
            col_number = 1
            for i in row[:-1]:
                    line = "train("+str(row_number)+","+str(col_number)+","+str(i)+").\n"
                    file.writelines(line)
                    col_number=col_number+1
            row_number=row_number+1
            if row_number >size_limit:
                break

with open('testdata/woTesting.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    with open('testdata/test.txt', "w") as file:
        row_number = 1
        for row in readCSV:
            col_number = 1
            for i in row[:-1]:
                    line = "test("+str(row_number)+","+str(col_number)+","+str(i)+").\n"
                    file.writelines(line)
                    col_number=col_number+1
            row_number=row_number+1
            if row_number >size_limit:
                break

with open('testdata/woTraining.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    with open('testdata/labels.txt', "w") as file:
        writer = csv.writer(file)
        row_number = 1
        for row in readCSV:
            line = "labels("+str(row_number)+","+str(row[-1])+").\n"
            file.writelines(line)
            row_number=row_number+1
            if row_number >size_limit:
                break
