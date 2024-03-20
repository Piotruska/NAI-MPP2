import fileinput
import random
import matplotlib.pyplot as plt

# Insert TrainingFile
TrainingFile = str(input("Training File: "))
if TrainingFile == "": TrainingFile = "perceptron.data"
f1 = open(TrainingFile, "r")
TraningData = []
answerList = []  # [value for 0, value for 1]
for x in f1.readlines():
    line = (x.strip("\n")).split(',')
    if line[-1] not in answerList:  # adding unique values to list
        answerList.append(line[-1])
    TraningData.append(line)

# Insert Testfile
TestFile = str(input("Test File: "))
if TestFile == "": TestFile = "perceptron.test.data"
f2 = open(TestFile, "r")
TestData = []
for x in f2.readlines():
    TestData.append((x.strip("\n")).split(','))

# Calculate vector length
vectorLength = len(TraningData[0]) - 1

# randomise weight vector from [0,1]
weightVector = [random.random() for i in range(vectorLength)]

# set all base values
bias = random.random()
LearningRate = float(input("Learning rate (alpha) eg, 0.01: "))
errorMax = float(input("Error Threshold eg. 0.1: "))


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
            net = net - bias
            if net >= 0: y = 1
            if net < 0: y = 0
            if x[vectorLength] == answerList[0]: d = 0
            if x[vectorLength] == answerList[1]: d = 1

            if y != d:
                for i in range(vectorLength):
                    weightVector[i] = weightVector[i] + (LearningRate * (d - y) * float(x[i]))
                bias = (bias - (LearningRate * (d - y)))
        runFlag = ErrorCheck()


def ErrorCheck():
    error = 0.0
    for vector in TestData:
        if answerList[classyfy(vector)] != vector[-1]:
            error += 1
    error = error / len(TestData)
    print(f"E: {error} W: {weightVector}  B: {bias}")
    if error <= errorMax:
        return False
    else:
        return True


def classyfy(vector):
    net = 0
    for i in range(vectorLength):
        net = net + (float(vector[i]) * weightVector[i])
    net = net - bias
    if net >= 0: return 1
    if net < 0: return 0

def TestCorrectness():
    counttotal = 0
    countcorrect = 0
    for vector in TestData:
        counttotal += 1
        if answerList[classyfy(vector)] == vector[-1]:
            countcorrect += 1
    print(f"c: {countcorrect} , t: {counttotal}")
    print(countcorrect/counttotal)

def menu():
    print("--------------")
    print("    Menu")
    print("--------------")
    print("1. Test accuracy of Perceptron")
    print("2. Clasyfy personal vector")
    print("3. Draw Error/Epoch")
    corect = False
    while not corect:
        userInput = int(input("Enter choise: "))
        if userInput == 1




menu()

Train()
TestCorrectness()
