# -*- coding: utf-8 -*-
"""
Created on Tue May 16 17:57:46 2023

@author: ville
"""

# Statistical Analysis

import numpy as np
import pandas as pd

# reading data saved from last part of the course
covid = pd.read_csv(
    "C:/Users/ville/Documents/Repositories/python-course/covid_sp_20230515.csv",
     sep = ";",
     encoding = "utf-8")

covid.head()

covid.dtypes

# filtering data by city name (municipio)

campinas = covid.loc[covid.municipio == "Campinas"]
campinas.head()

guarulhos = covid.loc[covid.municipio == "Guarulhos"]
guarulhos.head()

# % of eldery people at campinas

campinas['percentual_idosos'] = 100*(campinas.pop_60/campinas['pop'])

campinas.head()

guarulhos['percentual_idosos'] = 100*(guarulhos.pop_60/guarulhos['pop'])
guarulhos.head()

# mean

round(campinas.obitos_novos.mean(),3)
round(campinas.casos_novos.mean(),3)

round(guarulhos.obitos_novos.mean(),3)
round(guarulhos.casos_novos.mean(),3)

#which one is bigger?

round(campinas.obitos_novos.mean(),3) > round(guarulhos.obitos_novos.mean(),3)
#guarulhos have more no of (new) deaths due covid

round(campinas.casos_novos.mean(),3) > round(guarulhos.casos_novos.mean(),3)
#campinas have a greater number of new cases of covid

# median

campinas.obitos_novos.median()
campinas.casos_novos.median()

guarulhos.obitos_novos.median()
guarulhos.casos_novos.median()

# mode

campinas.obitos_novos.mode()
campinas.casos_novos.mode()

guarulhos.obitos_novos.mode()
guarulhos.casos_novos.mode()

campinas.mes.mode()
guarulhos.mes.mode()

# general information

round(campinas.describe(),1)
round(guarulhos.describe(),1)

round(campinas.casos_novos.describe(),1)
round(campinas.casos_pc.describe(),1)

round(guarulhos.casos_novos.describe(),1)
round(guarulhos.casos_pc.describe(),1)

# histogram

#onlye data from 2021
campinas.data.head()
campinas_2021 = campinas.loc[campinas.data > "2020-12-31"]

campinas.obitos_novos.mean()
campinas.obitos_novos.median()
campinas.obitos_novos.max()
campinas.obitos_novos.min()

import plotly.express as  px

#this import is because hist_graph.show() wasn't working
import plotly.io as pio
pio.renderers.default='browser'


hist_graph = px.histogram(campinas_2021, x = "obitos_novos", nbins = 30)
hist_graph.update_layout(width = 400, height = 400,
                         title_text = "New Deaths at Campinas in 2021")
hist_graph.show()


cases_hist = px.histogram(campinas_2021, x = "casos_novos", nbins = 40)
cases_hist.update_layout(width = 400, height = 400,
                         title_text = "New Cases at Campinas in 2021")
cases_hist.show()


