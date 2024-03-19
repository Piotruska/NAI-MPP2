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
    if line[-1] not in answerList:   #adding unique values to list
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
weightVector = [random.random() for i in range(vectorLength)]

# set all base values
bias = random.random()
LearningRate = float(input("Learning rate (alpha): "))
if LearningRate == "": TestFile = 0.01
errorMax = float(input("Error Threshold: "))
if errorMax == "": TestFile = 0.1

def Train():
    global weightVector, bias
    runFlag = True
    while runFlag:
        for x in TraningData:
            y = 0
            d = 0
            net = 0.0
            for i in range(vectorLength):
                net += float(x[i]) * (weightVector[i])
            if net >= 0: y = 1
            if net < 0: y = 0
            if x[vectorLength+1] == answerList[0]: d = 0
            if x[vectorLength+1] == answerList[1]: d = 1

            if y != d:
                for i in range(vectorLength):
                    weightVector[i] = weightVector[i] + (LearningRate * (d-y) * float(x[i]))
                bias = bias - (LearningRate * (d-y))
        runFlag = ErrorCheck()
