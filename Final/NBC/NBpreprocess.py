import numpy as np
import csv
import urllib.request as urllib
import random

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"
raw_data = urllib.urlopen(url)
with open('testdata/agaricus-lepiota.csv', 'wb') as file:
    file.write(raw_data.read())

size_limit = 3
# this function is used to verticalize the data and handle numeric
with open('testdata/bank-additional.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    names = readCSV
    next(readCSV)
    with open('testdata/loaddata.csv', "w") as file:
        writer = csv.writer(file)
        row_number = 1
        for row in readCSV:
            col_number = 1
            for i in row[:-1]:
                #handle numeric
                    if col_number = 21:
                        if names[col_number] >= 15 and names[col_number] < 15:
                            updated_att =  '15-25'
                        else if names[col_number] >= 25 and names[col_number] < 35:
                            updated_att =  '25-35'
                        else if names[col_number] >= 35 and names[col_number] < 45:
                            updated_att =  '35-45'
                        else if names[col_number] >= 45 and names[col_number] < 55:
                            updated_att =  '45-55'
                        else :
                            updated_att =  '>55'
                    if col_number = 12:
                        if names[col_number] == 1 :
                            updated_att =  '1'
                        else if names[col_number] == 2 :
                            updated_att =  '1'
                        else if names[col_number] == 3:
                            updated_att =  '3'
                        else :
                            updated_att =  '>=4'
                    if col_number = 16:
                        if names[col_number] < -2  :
                            updated_att =  '1'
                        else if names[col_number] >=  -2 and names[col_number] <  -1  :
                            updated_att =  '2'
                        else if names[col_number] >=  -1 and names[col_number] <  1  :
                            updated_att =  '3'
                        else if names[col_number] >=  1 :
                            updated_att =  '4'
                    if col_number = 20:
                        if names[col_number]  <= 5000  :
                            updated_att =  '1'
                        else if names[col_number] >  5000 and names[col_number] <= 5100 :
                            updated_att =  '2'
                        else if names[col_number] > 5100 and names[col_number] <=  5200  :
                            updated_att =  '3'
                        else if names[col_number] >=  5200 :
                            updated_att =  '4'
                    writer.writerow([row_number,col_number,updated_att,names[col_number],0,1])
                    col_number=col_number+1
            row_number=row_number+1
            if row_number >size_limit:
                break


#partition
with open('testdata/loaddata.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if random.random() > 0.8:
            with open('testdata/TEST_DATASET.csv', "w") as file:
                writer = csv.writer(file)
                writer.writerow(row)
        else:
            with open('testdata/TRAIN_DATASET.csv', "w") as file:
                writer = csv.writer(file)
                writer.writerow(row)
