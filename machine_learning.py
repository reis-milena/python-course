# -*- coding: utf-8 -*-
"""
Created on Tue May 23 18:30:22 2023

@author: ville
"""

### Machine learning

# library

import numpy as np
import pandas as pd

# reading data

#Data of worldwide covid-19 (data from WHO 2020-09-04)
covid_world = pd.read_csv(
    "C:/Users/ville/Documents/Repositories/python-course/covid19_mundial.csv",
     sep = ",",
     encoding = "utf-8")

covid_world

# analyzing data

total_deaths = covid_world.groupby('country').cumulative_deaths.max()
total_deaths
total_deaths.sort_values(ascending = False).head(15)

total_cases = covid_world.groupby('country').cumulative_cases.max()
total_cases.sort_values(ascending = False).head(15)

covid_brazil = covid_world.loc[covid_world.country == "Brazil"]
covid_brazil

covid_brazil.dtypes #ok
covid_brazil.isnull().sum() #ok
covid_world.isnull().sum() #ok

del total_cases, total_deaths

# negative values

covid_world.loc[covid_world.new_cases < 0, :]
covid_world.loc[covid_world.new_cases < 0, :].count()

covid_world.loc[covid_world.new_deaths < 0, :]
covid_world.loc[covid_world.new_deaths < 0, :].count()

#brazil
covid_brazil.loc[covid_world.new_cases < 0, :]
covid_brazil.loc[covid_world.new_cases < 0, :].count()

covid_brazil.loc[covid_world.new_deaths < 0, :]
covid_brazil.loc[covid_world.new_deaths < 0, :].count()

# statistical analysis

covid_brazil.describe()

# checking for outliers

import plotly.express as px
#this import is because .show() wasn't working
import plotly.io as pio
pio.renderers.default='browser'

px.box(covid_brazil, y = "cumulative_cases")
px.box(covid_brazil, y = "cumulative_deaths")

# normality test

import seaborn as sns

sns.histplot(covid_brazil, x = "cumulative_cases", bins = 20, color = "darkred",
             kde = True, stat = "count");
sns.histplot(covid_brazil, x = "cumulative_deaths", bins = 20, color = "darkred",
             kde = True, stat = "count");

import scipy.stats as stats
import matplotlib.pyplot as plt

stats.probplot(covid_brazil.cumulative_cases, dist = "norm", plot = plt)
plt.title("Normality Analysis - cumulative_cases")
plt.show()
stats.probplot(covid_brazil.cumulative_deaths, dist = "norm", plot = plt)
plt.title("Normality Analysis - cumulative_deaths")
plt.show()

#THIS PART IT ISN'T RUNNING
"""
import statsmodels
from statsmodels import lilliefors

statistic_ks, p_ks = statsmodels.stats.diagnostic.lilliefors(covid_brazil.cumulative_cases,
                                                             dist = "norm")
print("Test statistic =",round(statistic_ks,2))
print("P value =", p_ks)
statistic_ks, p_ks = statsmodels.stats.diagnostic.lilliefors(covid_brazil.cumulative_deaths,
                                                             dist = "norm")
print("Test statistic =",round(statistic_ks,2))
print("P value =", p_ks)
"""

# scatter plot with date

scatter = px.scatter(covid_brazil, x = "date", y = "cumulative_cases")
scatter.update_layout(width = 800, height = 500, title_text = "cumulative cases")
scatter.update_xaxes(title = "Date")
scatter.update_yaxes(title = "cumulative_cases")
scatter.show()

scatter = px.scatter(covid_brazil, x = "date", y = "cumulative_deaths")
scatter.update_layout(width = 800, height = 500, title_text = "cumulative deaths")
scatter.update_xaxes(title = "Date")
scatter.update_yaxes(title = "cumulative_deaths")
scatter.show()

plt.subplots(figsize = (10,5))
plt.stackplot(covid_brazil.date, [covid_brazil.cumulative_cases, covid_brazil.cumulative_deaths],
              labels = ['cumulative_cases','cumulative_deaths'])
plt.legend(loc = "upper left")
plt.title("Cases and Deaths from Covid-19 Evolution in Brazil");

#linear correlation

cor = covid_brazil.corr(method = "spearman")#spearman cause it hasn't a normal distrib.
cor

plt.figure()
sns.heatmap(cor, annot = True)