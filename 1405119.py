import numpy as np

featureVectorTrain = np.zeros((500, 5))
labelTrain = []

featureVectorTest = np.zeros((500, 5))
labelTest = []

weight = np.zeros(5 + 1)
temp = np.zeros(5 + 1)
storedWeight = np.zeros(5 + 1)


def readTrain():
    file = open("Train.txt", "r")
    for i in range(0, 500):
        data = file.readline()
        datanow = data.split()
        featureVectorTrain[i][0] = float(datanow[0])
        featureVectorTrain[i][1] = float(datanow[1])
        featureVectorTrain[i][2] = float(datanow[2])
        featureVectorTrain[i][3] = float(datanow[3])
        featureVectorTrain[i][4] = float(datanow[4])
        labelTrain.append(int(datanow[5]))


def readTest():
    file = open("Test.txt", "r")
    for i in range(0, 500):
        data = file.readline()
        datanow = data.split()
        featureVectorTest[i][0] = float(datanow[0])
        featureVectorTest[i][1] = float(datanow[1])
        featureVectorTest[i][2] = float(datanow[2])
        featureVectorTest[i][3] = float(datanow[3])
        featureVectorTest[i][4] = float(datanow[4])
        labelTest.append(int(datanow[5]))


def predict(inputs):
    res = np.dot(inputs, weight[1:]) + weight[0]
    if res > 0:
        return 2
    else:
        return 1


def predict2(inputs):
    res = np.dot(inputs, storedWeight[1:]) + storedWeight[0]
    if res > 0:
        return 2
    else:
        return 1


def train1(inputs, labels):
    for i in range(0, 500):
        temp = np.zeros(6)
        for j in range(0, 500):
            prediction = predict(inputs[j])
            temp[1:] += (labels[j]-prediction)*inputs[j]
            temp[0] += (labels[j]-prediction)
        weight[1:] += temp[1:]
        weight[0] += temp[0]


def train2(inputs, labels):
    for i in range(0, 10):
        for j in range(0, 500):
            prediction = predict(inputs[j])
            weight[1:] += (labels[j]-prediction)*inputs[j]
            weight[0] += (labels[j]-prediction)


def train3(inputs, labels):
    maxm = 0
    for i in range(0, 100):
        corrCount = 0
        for j in range(0, 500):
            prediction = predict(inputs[j])
            if prediction == labels[j]:
                corrCount += 1
            weight[1:] += (labels[j]-prediction)*inputs[j]
            weight[0] += (labels[j]-prediction)
        if corrCount > maxm:
            storedWeight[1:] = weight[1:]
            storedWeight[0] = weight[0]
            maxm = corrCount


def basicPerceptron():
    readTrain()
    train1(featureVectorTrain, labelTrain)
    readTest()
    missclassify = 0
    for i in range(0, 500):
        if labelTest[i] != predict(featureVectorTest[i]):
            missclassify += 1
    print('basic perceptron: ', missclassify)
    return


def rewardPunishment():
    readTrain()
    train2(featureVectorTrain, labelTrain)
    readTest()
    missclassify = 0
    for i in range(0, 500):
        if labelTest[i] != predict(featureVectorTest[i]):
            missclassify += 1
    print('reward punishment: ', missclassify)
    return


def pocket():
    readTrain()
    train3(featureVectorTrain, labelTrain)
    readTest()
    missclassify = 0
    for i in range(0, 500):
        if labelTest[i] != predict2(featureVectorTest[i]):
            missclassify += 1
    print('pocket: ', missclassify)
    return


def multiClass():
    readTrain()
    train3(featureVectorTrain, labelTrain)
    readTest()
    missclassify = 0
    for i in range(0, 500):
        if labelTest[i] != predict2(featureVectorTest[i]):
            missclassify += 1
    print('multiclass: ', missclassify)
    return


def main():
    basicPerceptron()
    #rewardPunishment()
    #pocket()
    #multiClass()


main()