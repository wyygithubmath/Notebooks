#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ---------------------
# file name : python_knn_read
# author : wyy
# data : 2017-01-11
# function : kNN
# ---------------------


__author__ = 'wyy'

import numpy as np
import operator
import kNN
import kNNBook

filePath = '../Data/datingTestSet2.txt'

normDataSet, dataLabel = kNN.readData(filePath)
kNN.classFun(normDataSet[2,:], normDataSet, dataLabel, k=5)
kNNBook.classify0(normDataSet[2,:], normDataSet, dataLabel, k=5)
