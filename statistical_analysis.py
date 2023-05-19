# -*- coding: utf-8 -*-
"""
Created on Tue May 16 17:57:46 2023

@author: ville
"""

### Statistical Analysis

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

## general information

round(campinas.describe(),1)
round(guarulhos.describe(),1)

round(campinas.casos_novos.describe(),1)
round(campinas.casos_pc.describe(),1)

round(guarulhos.casos_novos.describe(),1)
round(guarulhos.casos_pc.describe(),1)

## histogram

#onlye data from 2021
campinas.data.head()
campinas_2021 = campinas.loc[campinas.data > "2020-12-31"]

campinas.obitos_novos.mean()
campinas.obitos_novos.median()
campinas.obitos_novos.max()
campinas.obitos_novos.min()

import plotly.express as px

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

del campinas_2021

# min, max, quartile (or n quantile)

campinas.casos_novos.min()
campinas.casos_novos.max()

guarulhos.casos_novos.min()
guarulhos.casos_novos.max()

campinas.casos_novos.quantile(q = 0.25) #1st quartile
campinas.casos_novos.quantile(q = 0.5) #2nd quartile
campinas.casos_novos.median() # 2nd quartile  =  median
campinas.casos_novos.quantile(q = 0.75) #3rd quartile
campinas.casos_novos.quantile(q = 1) #4th quartile (= max)

campinas.casos_novos.describe()

## boxplot and outlier

import plotly.express as px

#this import is because hist_graph.show() wasn't working
import plotly.io as pio
pio.renderers.default='browser'

boxplot = px.box(campinas, y = "casos_novos")
boxplot.show()

#calculus of boxplot

outlier_sup = campinas.casos_novos.quantile(q = 0.75) + \
    1.5*(campinas.casos_novos.quantile(q = 0.75) - campinas.casos_novos.quantile(q = 0.25))
# \ breaks line

outlier_inf = campinas.casos_novos.quantile(q = 0.25) - \
    1.5*(campinas.casos_novos.quantile(q = 0.75) - campinas.casos_novos.quantile(q = 0.25))
    
outlier_sup
outlier_inf

no_outlier = campinas.loc[campinas.casos_novos <= outlier_sup]

noout_boxplot = px.box(no_outlier, y = "casos_novos")
noout_boxplot.show()

del no_outlier, noout_boxplot

boxplot = px.box(guarulhos, y = "casos_novos")
boxplot.show()

del boxplot, outlier_inf, outlier_sup

# dispersion measures

#variance
guarulhos.obitos_novos.var()
campinas.obitos_novos.var()

#standard deviation
guarulhos.obitos_novos.std()
campinas.obitos_novos.std()

guarulhos.obitos_novos.describe()
campinas.obitos_novos.describe()

## normal distribution - normality test

import seaborn as sns

sns.histplot(campinas, x = "casos_novos", bins = 30,
             color = "darkblue",
             kde = True, #kde is a tendency line
             stat = "count")

# qqplot
import scipy.stats as stats
import matplotlib.pyplot as plt

stats.probplot(campinas.casos_novos, dist = "norm", plot = plt)
plt.title("Normality Study")
plt.show()

# shapiro-wilk test
# p>0.05 for normality

stats.shapiro(campinas.casos_novos)
statistic_shapiro, p_shapiro = stats.shapiro(campinas.casos_novos)
print("Test (w) statistic =",round(statistic_shapiro,2))
print("P value =", p_shapiro)
print("P value =", round(p_shapiro,4))

del statistic_shapiro, p_shapiro

# Kolmogorov-Smirnov Test

#THIS PART IT ISN'T RUNNING
"""
import statsmodels
from statsmodels import lilliefors

statistic_ks, p_ks = statsmodels.stats.diagnostic.lilliefors(campinas.casos_novos,
                                                             dist = "norm")
print("Test (ks) statistic =",round(statistic_ks,2))
print("P value =", p_ks)
"""

## linear correlation
import scipy.stats as stats
import matplotlib.pyplot as plt

plt.scatter(campinas.casos, campinas.obitos)
plt.title("Covid SP Correlation")
plt.xlabel("Cases")
plt.ylabel("Deaths")
plt.grid(False)
plt.show()


df = campinas[["casos","casos_novos","obitos","obitos_novos"]]

# include correlation

# shapiro-wilk test
# p>0.05 for normality

statistic_shapiro, p_shapiro = stats.shapiro(campinas.casos)
print("Test (w) statistic =",round(statistic_shapiro,2))
print("P value =", p_shapiro)

statistic_shapiro, p_shapiro = stats.shapiro(campinas.obitos)
print("Test (w) statistic =",round(statistic_shapiro,2))
print("P value =", p_shapiro)

statistic_shapiro, p_shapiro = stats.shapiro(campinas.casos_novos)
print("Test (w) statistic =",round(statistic_shapiro,2))
print("P value =", p_shapiro)

statistic_shapiro, p_shapiro = stats.shapiro(campinas.obitos_novos)
print("Test (w) statistic =",round(statistic_shapiro,2))
print("P value =", p_shapiro)

del statistic_shapiro, p_shapiro

#Pearson  - parametric data (normality and Homoscedasticity)
#Spearman - non parametric data, big sample (>=30)
#Kendall  - non parametric data, small sample (<30)
correlacoes = df.corr(method = "spearman") #obs: as seen before, this data doesn't have a normal distribution
correlacoes

import seaborn as sns
plt.figure()
sns.heatmap(correlacoes, annot = True)

sns.pairplot(df) # histogram and scatter plots

## Linear Regression with Statsmodels

import statsmodels.formula.api as smf
import statsmodels.stats.api   as sms

regression = smf.ols("obitos ~ casos", data = campinas).fit()
print(regression.summary())

coefs = pd.DataFrame(regression.params)
coefs.columns = ["Coefficients"]
print(coefs)

plt.scatter(y = campinas.obitos, x = campinas.casos, color = "lightblue",
            s = 15, alpha = 0.5)
x_plot = np.linspace(min(campinas.casos), max(campinas.casos),len(campinas.obitos))
plt.plot(x_plot, x_plot*regression.params[1]+regression.params[0],
         color = "darkred")
plt.title("Linear Regression")
plt.xlabel("Cases")
plt.ylabel("Deaths")
plt.grid(False)
plt.show()


