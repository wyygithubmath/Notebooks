#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ---------------------
# file name : python_knn_read
# author : wyy
# data : 2017-01-10
# function : kNN
# ---------------------


__author__ = 'wyy'

import numpy as np
import operator

# import data
def readData(filePath):
    with open(filePath) as dataFile:
        dataTXT = dataFile.readlines()
    numLin = len(dataTXT)
    numCol = len(dataTXT[0].strip().split('\t'))
    dataMat = np.zeros((numLin, (numCol-1)))
    dataLabel = []
    index = 0
    for line in dataTXT:
        line = line.strip()
        listFromLime = line.split('\t')
        dataMat[index, :] = listFromLime[0:(numCol-1)]
        dataLabel.append(int(listFromLime[-1]))
        index += 1

    # normalize data
    # colum min
    minVals = dataMat.min(0)
    maxVals = dataMat.max(0)
    rag = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataMat))
    m = dataMat.shape[0]
    normDataSet = dataMat - np.tile(minVals, (m,1))
    normDataSet = normDataSet / np.tile(rag, (m,1))
    return normDataSet, dataLabel


# classify
def classFun(inX, normDataSet, dataLabel, k):
    dataSize = normDataSet.shape[0]
    diffMat = np.tile(normDataSet[0,:], (dataSize, 1)) - normDataSet
    sqDiffMat = diffMat ** 2
    sqDistance = sqDiffMat.sum(axis=1)
    distance = sqDistance ** 0.5
    # pick k point
    sortedDistanceIndex = distance.argsort()
    classCount = {}
    for i in range(5):
        voteLabel = dataLabel[sortedDistanceIndex[i]]
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
    # order
    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

# test
def dataClassTest(normDataSet, dataLabel, k):
    errorCount = 0.0
    for i in range(1000):
        classifierResult = classFun(normMat[i,:],normMat, dataLabel, k)
        print((classifierResult, dataLabel[i]))
        if (classifierResult != dataLabel[i]):
            errorCount += 1.0
    print((errorCount/float(numTestVecs)))




if __name__ == '__main__':
    print("This is a kNN.")
