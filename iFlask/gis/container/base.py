# coding: utf-8

import os
import pickle
from sklearn import linear_model
import logging

logger = logging.getLogger(__name__)

class Base(object):
    __abstract__ = True

    def __init__(self):
        self.df = None
        self.dataPath = ''
        self.trainedModel = ''
        # the model must be a object and it contain a named predict method
        self.model = None
        self.picker = None


    def load(self, path):
        return pickle.load(open(path, 'rb'))

    def loadDvalidFromDict(self, data):
        """exactly, need a method convet data to df object"""
        # return feature
        pass

    def loadDvalidFromFile(self, file, skiprows = 1):
        """load feature data from file"""
        # return dvalid
        pass

    def run(self, data):
        # load model from persistence file
        # if not self.df:
        #     self.df = self.load(self.dataPath)
        df = self.df

        lat_list = []
        lng_list = []

        # prepare feature data
        if isinstance(data, dict):
            feature, dataLst = self.loadDvalidFromDict(data)

            # The lat list and lng list should be from js

            trainX = df.fillna(0)[self.picker].loc[df['DataId'].isin(dataLst)]
            trainY = df.fillna(0)[u'SalePrice'].loc[df['DataId'].isin(dataLst) ]

            self.model = linear_model.LinearRegression()

            self.model.fit(trainX, trainY)

            result = self.predict(feature)

            return result
        else:
            logger.error('Data must be a dict type')
            return None

    def predict(self, feature):
        """
        Predict data
        Args:
            param: dvalid, data form
        """
        res = self.model.predict(feature)

        return res
