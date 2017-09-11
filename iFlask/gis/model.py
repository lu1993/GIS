# coding: utf-8
from __future__ import division
import os
import numpy as np
from pandas import Series

from .container.base import Base

# set a global variable for keep the big data
df = None

class GIS(Base):
    def __init__(self):
        global df

        super(GIS, self).__init__()
        self.picker = np.array([u'ListPrice',
                                u'DOM',
                                u'CDOM',
                                u'Bedrooms',
                                u'YearBuilt',
                                u'LotSqFt',
                                u'StructureSqFt',
                                u'BathsFull',
                                u'BathsHalf',
                                u'GarageSpaces',
                                u'ParkingSpaces',
                                u'NumberUnits',
                                u'StoriesTotal',
                                u'HOAFee']
                               )
        appPath = os.path.join(os.getcwd(), 'iFlask/gis/data')

        self.dataPath = os.path.join(appPath, 'data.pkl')
        if df is None:
            df = self.load(self.dataPath)
        self.df = df

    def loadDvalidFromDict(self, data):
        """exactly, need a method convet data to df object"""
        # it will raise ValueError: If using all scalar values, you must must pass an index
        # reference: http://stackoverflow.com/questions/18837262/convert-python-dict-into-a-dataframe
        points = data.pop('POINTS')

        index = ['ListPrice', 'DOM', 'CDOM', 'Bedrooms', 'YearBuilt', 'LotSqFt', 'StructureSqFt', 'BathsFull',
                 'BathsHalf', 'GarageSpaces', 'ParkingSpaces', 'NumberUnits', 'StoriesTotal', 'HOAFee']

        feature = Series([data[key] for key in index], index=index)

        return feature, points

