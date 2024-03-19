import fileinput
import random
import matplotlib.pyplot as plt

# Insert TrainingFile
TrainingFile = str(input("Training File: "))
if TrainingFile == "": TrainingFile = "perceptron.data"

# Insert Testfile
TestFile = str(input("Test File: "))
if TestFile == "": TestFile = "perceptron.test.data"