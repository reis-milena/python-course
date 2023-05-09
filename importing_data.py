# -*- coding: utf-8 -*-
"""
Created on Tue May  9 17:56:30 2023

@author: ville
"""

## Importing the data (.csv)

import pandas as pd

data = pd.read_csv(
    "C:/Users/ville/Documents/Repositories/python-course/dados_covid_sp.csv",
    sep=";",
    encoding="utf-8")

data.head()

data.shape  # rows and columns

del data

## Importing data (.xlsx)

data_xlsx = pd.read_excel(
    "C:/Users/ville/Documents/Repositories/python-course/dados_covid_sp.xlsx")

data_xlsx.head()

data_xlsx.shape  # rows and columns

del data_xlsx

## Importing data from url

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

colnames = ['sepal-length','sepal-width','petal-length','petal-width','Class']

iris_data = pd.read_csv(url,names = colnames)

iris_data.head()

iris_data.shape

type(iris_data)

len(iris_data.Class) #no observations

del url, colnames, iris_data

## Importing datasets

# https://www.statsmodels.org/stable/datasets/index.html

import statsmodels.api as sm

cancer = sm.datasets.cancer.load_pandas().data

cancer.head()

cancer.shape

del cancer

# https://scikit-learn.org/stable/datasets/toy_dataset.html

import sklearn

from sklearn import datasets

iris = datasets.load_iris()

iris

type(iris)

iris.data

iris.target #Class values

iris.target_names #Clas names