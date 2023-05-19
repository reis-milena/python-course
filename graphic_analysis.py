# -*- coding: utf-8 -*-
"""
Created on Fri May 19 17:27:56 2023

@author: ville
"""

### Graphic Analysis

import numpy as np
import pandas as pd

# reading data

# Data of severe acute respiratory syndrome (sars)
sars = pd.read_csv(
    "C:/Users/ville/Documents/Repositories/python-course/SRAG_2020.csv",
     sep = ";",
     encoding = "utf-8")

sars.head()

sars.shape

# treating data

#deleting columns that won't be used in this study
list_del_column = list(range(50,133))

sars_edited = sars.drop(sars.columns[list_del_column], axis = 1)

sars_edited.shape
sars_edited.head()

del list_del_column

#deleting columns by name
sars_edited.drop(columns = ["COD_IDADE","ID_PAIS","CO_PAIS","SG_UF","ID_RG_RESI","CO_RG_RESI","CO_MUN_RES"],
                 inplace = True)

sars_edited.shape
sars_edited.head()

#renaming columns
sars_edited = sars_edited.rename(columns = {"DT_NOTIFIC": "date",
                                            "CS_SEXO"   : "sex",
                                            "NU_IDADE_N": "age",
                                            "CS_RACA"   : "race"})
sars_edited.head()

sars_edited.dtypes

sars_edited.date = sars_edited.date.astype("datetime64[D]")
sars_edited.dtypes

# checking for missing

sars_edited.isnull().sum()

#counting values of race variable

sars_edited.race.value_counts().sort_index()

#changing missing in race for 9
sars_edited.race.fillna(9, inplace = True)

sars_edited.race.value_counts().sort_index()

#counting values of cs_zona variable

sars_edited.CS_ZONA.value_counts().sort_index()

#changing missing in CS_ZONA for 9
sars_edited.CS_ZONA.fillna(9, inplace = True)

sars_edited.CS_ZONA.value_counts().sort_index()

# changing numeric values for names in race (categorical variable)
sars_edited.race.value_counts().sort_index()
sars_edited.race = sars_edited.race.replace({1: "white",
                                             2: "black",
                                             3: "yellow",
                                             4: "brown", #pardo in portuguese
                                             5: "indigenous",
                                             9: "NAN"})
sars_edited.race.value_counts().sort_index()

# changing numeric values for names in CS_ZONA (categorical variable)
sars_edited.CS_ZONA.value_counts().sort_index()
sars_edited.CS_ZONA = sars_edited.CS_ZONA.replace({1: "urban",
                                             2: "rural",
                                             3: "periurban",
                                             9: "NAN"})
sars_edited.CS_ZONA.value_counts().sort_index()

