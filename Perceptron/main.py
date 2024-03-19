import fileinput
import random
import matplotlib.pyplot as plt

# Insert TrainingFile
TrainingFile = str(input("Training File: "))
if TrainingFile == "": TrainingFile = "perceptron.data"
f1 = open(TrainingFile, "r")
TraningData = []
answerList = [] #  [value for 0, value for 1]
for x in f1.readlines():
    line = (x.strip("\n")).split(',')
    if line[-1] not in answerList:
        answerList.append(line[-1])
    TraningData.append(line)

# Insert Testfile
TestFile = str(input("Test File: "))
if TestFile == "": TestFile = "perceptron.test.data"
f2 = open(TestFile, "r")
TestData = []
for x in f2.readlines():
    TraningData.append(x.split(','))

# Calculate vector length
vectorLength = len(TraningData[0])-1

#randomise weight vector from [0,1]
weigthVector = [random.random() for i in range(vectorLength)]

