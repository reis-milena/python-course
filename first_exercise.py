# -*- coding: utf-8 -*-
"""
Created on Mon May 15 19:08:23 2023

@author: ville
"""

from sklearn import datasets

iris = datasets.load_iris()
iris

iris.feature_names

iris.target_names

# Exercise: transform IRIS array into dataframe with column of target name

#1 importing library
import numpy as np
import pandas as pd

#2 checking iris format
type(iris)

#3 making it a dataframe

iris.feature_names # names of columns of iris
iris_df = pd.DataFrame(iris.data, columns = ["sepal_length",
                                     "sepal_width",
                                     "petal_length",
                                     "petal_width"]) #making it as dataframe

iris_df

#4 creating array with target/class name

names_target = iris.target

np.unique(names_target, return_counts=True) #checking values of target

names_target = pd.DataFrame(names_target, columns = ["class"])


iris.target_names #names are here

names_target = names_target.replace({0: "setosa",
                                     1: "versicolor",
                                     2: "virginica"})

#5 adding the class column to iris dataframe

iris_df = pd.concat([iris_df,names_target],axis = 1)
iris_df.head()

iris_df.shape
