import fileinput
import random
import matplotlib.pyplot as plt

# Insert TrainingFile
TrainingFile = str(input("Training File: "))
if TrainingFile == "": TrainingFile = "perceptron.data"
f1 = open(TrainingFile, "r")
TraningData = []
for x in f1.readlines():
    TraningData.append(x.split(','))



# Insert Testfile
TestFile = str(input("Test File: "))
if TestFile == "": TestFile = "perceptron.test.data"
f2 = open(TestFile, "r")
TestData = []
for x in f2.readlines():
    TraningData.append(x.split(','))

# Calculate vector length
vectorLength = len(TraningData[0])-1
