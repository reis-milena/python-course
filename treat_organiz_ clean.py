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
del column
    
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

# deleting rows by row number
covid_sp_test.head()
covid_sp_test2 = covid_sp_test.drop(covid_sp_test.index[[1,3]])
covid_sp_test2.head()

covid_sp_test2 = covid_sp_test2.drop(covid_sp_test2.index[2:4])
covid_sp_test2.head()

#notice the difference: when you chose row by row, you have to write two [[]],
#when you chose a sequence/interval you use onlye one[]

#reset index
covid_sp_test2 = covid_sp_test2.reset_index(drop=True)#drop to delete previous index
covid_sp_test2.head()

del covid_sp_test2

#data frame with municipio not identified
ignored = covid_sp_test.loc[covid_sp_test.municipio == "Ignorado"]
ignored

ignored.shape
#checking the size of the non-indentified data
tuple(i/j for i,j in zip(ignored.shape,covid_sp_test.shape))

del ignored

#deleting non-identified data
covid_sp_test.shape
covid_sp_test = covid_sp_test.loc[covid_sp_test.municipio != "Ignorado"]
covid_sp_test.shape

guarulhos = covid_sp_test.loc[covid_sp_test.municipio == "Guarulhos"]
guarulhos

guarulhos.drop(columns = ["map_leg_s","municipio"],inplace = True)

#changing specific value on dataframe
guarulhos['semana_epidem'] = guarulhos['semana_epidem'].replace({9: "nove",
                                                                 10: "dez"})
guarulhos
guarulhos.semana_epidem = guarulhos.semana_epidem.replace({38: "trinta e oito"})
guarulhos

guarulhos['semana_epidem'] = guarulhos['semana_epidem'].replace([11,12,13],
                                                                ["onze","doze","treze"])
guarulhos.head(30)

#change , to . in string
guarulhos.casos_pc
guarulhos.casos_pc = guarulhos.casos_pc.apply(lambda x: x.replace(',','.'))
guarulhos.casos_pc

#create columns with data
import datetime

date = np.array('2020-02-25',dtype = np.datetime64())
date

date = date + np.arange(579)
date

date = pd.DataFrame(date) #making it as dataframe
date

date.columns = ["date"]
date.head()

guarulhos2 = pd.concat([date,guarulhos],axis = 1)
guarulhos2.head()

"""Out[52]: 
        date  index  mes  casos  ...  area map_leg semana_epidem  density
0 2020-02-25    NaN  NaN    NaN  ...   NaN     NaN           NaN      NaN
1 2020-02-26    NaN  NaN    NaN  ...   NaN     NaN           NaN      NaN
2 2020-02-27    NaN  NaN    NaN  ...   NaN     NaN           NaN      NaN
3 2020-02-28    NaN  NaN    NaN  ...   NaN     NaN           NaN      NaN
4 2020-02-29    NaN  NaN    NaN  ...   NaN     NaN           NaN      NaN
"""
# notice that there is a problem and that is due to the index (date index is different
# from gurarulhos index)

#so first reset index of guarulhos
guarulhos = guarulhos.reset_index(drop=True)#drop to delete previous index
guarulhos.head()

#and then concat
guarulhos2 = pd.concat([date,guarulhos],axis = 1)
guarulhos2.head()

del guarulhos, guarulhos2, date