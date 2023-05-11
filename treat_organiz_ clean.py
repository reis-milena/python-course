# -*- coding: utf-8 -*-
"""
Created on Thu May 11 17:52:02 2023

@author: ville
"""

# Treating data

## Reading data
#covid data - Sao Paulo/Brazil - feb 2020 - sep 2021

import numpy as np
import pandas as pd

covid_sp = pd.read_csv(
    "C:/Users/ville/Documents/Repositories/python-course/dados_covid_sp.csv",
    sep=";",
    encoding="utf-8")

covid_sp.head()

## Data treatment, organization and cleaning

#rename columns
# iterating the columns
for column in covid_sp.columns:
    print(column)
    
covid_sp = covid_sp.rename(columns = {"nome_munic": "municipio"})

covid_sp.head()

covid_sp.rename(columns = {"datahora": "data"}, inplace = True)

for column in covid_sp.columns:
    print(column)

covid_sp.rename(columns = {"codigo_ibge": "cod_munic",
                           "latitude": "lat",
                           "longitude": "long"},
                inplace = True)

for column in covid_sp.columns:
    print(column)
    
#deleting column by colname

covid_sp.shape

covid_sp_test = covid_sp.drop(columns = ["cod_ra"])

covid_sp_test.shape

covid_sp_test.drop(columns = ["lat","long"], inplace = True)

covid_sp_test.shape

#deleting column by colnumber
covid_sp_test.head()

covid_sp_test = covid_sp_test.drop(covid_sp_test.columns[[1]],
                                   axis = 1) # axis =1 column / =2 row

covid_sp_test.shape
covid_sp_test.head()

covid_sp_test.drop(covid_sp_test.columns[[1,3]],
                                   axis = 1,
                                   inplace = True) 
covid_sp_test.shape
covid_sp_test.head()

#changing values

covid_sp_test.area.head()

covid_sp_test['area'] = covid_sp_test['area']/100
# covid_sp_test['area'] = covid_sp_test.area/100 #same result

covid_sp_test.area.head()

#creating column

covid_sp_test["density"] = covid_sp_test["pop"] / covid_sp_test["area"]
 
covid_sp_test.shape
#Out[65]: (374034, 21)

rownum = list(range(1,374035))

##changing rownum to be a dataframe

df = pd.DataFrame(rownum, columns = ["index"])
df

del rownum

##inserting new column on dataframe

#joining dataframes (cbind in R)
covid_sp_test = pd.concat([covid_sp_test,df],
                          axis = 1) #=1 column / =2 row
covid_sp_test.head()

del df

#changing position of column

covid_sp_test = covid_sp_test.reindex(columns = ["index"] +
                                      list(covid_sp_test.columns[:-1])
                                      )
# -1 is the last column
covid_sp_test.head()


## Counting values

covid_sp_test["semana_epidem"].value_counts()

#ex: on the 35o week there was 9044 covid cases

from collections import Counter
Counter(covid_sp_test.semana_epidem) #same result

#sorting by week
covid_sp_test["semana_epidem"].value_counts().sort_index()

covid_sp_test.query("obitos_novos > 30")["municipio"].value_counts()

#ex: Sao Paulo registered 295 times no of deaths > 50

covid_sp_test.query("obitos_novos > 30 and density > 500.0")["municipio"].value_counts()


#selecting columns by index

x = covid_sp_test.iloc[: , 3:10]
x
type(x)

y = covid_sp_test.iloc[: , 1]
y
type(y) #one column = type series

y = covid_sp_test.iloc[:, 1].values #.values to be an ARRAY
y
type(y) # type  = array

#changing to list
list_y = list(y.flatten())  #list the array
list_y
type(list_y)

#changing to dataframe
df = pd.DataFrame(list_y, columns = ["municipio"])
df

del df,x,y,list_y

