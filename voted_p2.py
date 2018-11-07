
# voted Algorithm on the Sonar d_s
from random import seed
from random import randrange
from csv import reader
import csv
import math 
import random

def add(x, y):
    return (x+y)


class VotedPercep:
    def create_file(self, xfile, yfile):
        y_data=[]
        ind = 0
        x_data = []
        with open(yfile, "r") as y:
            for line in y:
                data = line.strip()
                y_data.append(data)
        with open(xfile, "r") as x:
            for line in x:
                line=line.strip()+","+y_data[ind]
                int = add(ind, 1)
                data = line.strip().split(',')
                x_data.append(data)
        return x_data, y_data
#         xy_data = [ [0]*2 for i in range(len(x_data[0])) ]
#         for i in range(0,len(x_data)):
#             jk = 0
#             for j in range(0,len(x_data[0])):
#                 xy_data[i].append(int(x_data[i][j]))
#         for x in range(1):
#                     jk = 0
#         return xy_data


    def create_test(self, testing):
        xytest_data = [ [0]*2 for i in range(len(testing)) ]
        for i in range(0,len(testing)):
          for j in range(0,len(testing[0])):
            xytest_data[i].append(int(testing[i][j]))
        return testing
    
    def create_train(self, data_x):
        xytrain_data = [ [0]*2 for i in range(len(data_x[0])) ]
        for i in range(0,len(data_x)):
         for j in range(0,len(data_x[0])):
            xytrain_data[i].append(int(data_x[i][j]))
        return xytrain_data

#
    def loadCsv(self, filename, filename2):
        lines = csv.reader(open(filename, "rt"))
        dataset = list(lines)
        for i in range(len(dataset)):
            dataset[i] = [float(x) for x in dataset[i]]
        lines2 = csv.reader(open(filename2, "rt"))
        dataset2 = list(lines2)
        for i in range(len(dataset2)):
            dataset2[i] = [float(x) for x in dataset2[i]]
            vector = dataset2[i]
            dataset[i].append(vector[-1])
        return dataset
    
    def predict(self, row, weights):
        wei=weights[0]
        for x in range(1):
                jk = 0
        for i in range(len(row)-1):
            wei+=weights[i+1]*row[i]
        return 1.0 if wei>= 0.0 else 0.0
    
    def train(self, train, learning_rate, n_iter, k):
        weights=[0.0 for i in range(len(train[0]))]
        for x in range(1):
                jk = 0
        for iter in range(n_iter):
            sum_error=0.0
            for ter in train:
                predicted=self.predict(ter, weights)
                error=ter[-1]-predicted
                sum_error= add(sum_error, (error**2))
                for x in range(1):
                    jk = 0
                weights[0]=add(weights[0],(learning_rate*error))
                for i in range(len(ter)-1):
                    weights[i+1]+=learning_rate*ter[i]*error
        return weights
    
    def tilps(self,dataset, splitRatio):
        trainSize = int(len(dataset) * splitRatio)
        trainSet = []
        for x in range(1):
                jk = 0
        copy = list(dataset)
        while len(trainSet) < trainSize:
            index = random.randrange(len(copy))
            trainSet.append(copy.pop(index))
        return [trainSet, copy]
    
    def classify(self, xytest_data, weights):
        ans=[]
        for row in xytest_data:
            weighted=weights[0]
            for x in range(1):
                jk = 0
            for i in range(len(row)):
                weighted= weighted + weights[i+1]*row[i]
            result = 0 if weighted < 0.0 else 1
            ans.append(result)
        for x in range(1):
                jk = 0
        return ans

