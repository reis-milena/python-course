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

del scatter
#linear correlation

cor = covid_brazil.corr(method = "spearman")#spearman cause it hasn't a normal distrib.
cor

plt.figure()
sns.heatmap(cor, annot = True)

del cor

# Machine Learning
covid_brazil.shape

# Linear regression
scatter = px.scatter(covid_brazil, x = "new_cases", y = "new_deaths")
scatter.update_layout(width = 800, height = 500, title_text = "Deaths VS Cases")
scatter.update_xaxes(title = "New cases")
scatter.update_yaxes(title = "New Deaths")
scatter.show()

del scatter

x = covid_brazil.iloc[:,4].values #4 is new cases
y = covid_brazil.iloc[:,6].values #6 is new deaths

x
y

#setting X into column-matrix
x = x.reshape(-1,1)
x

#separate data into test-data and training-data
from sklearn.model_selection import train_test_split
x_training , x_test, y_training, y_test = train_test_split(x ,y,
                                                           test_size = 0.25,
                                                           random_state = 2) #seed
x_training
x_test

x_training.size
x_test.size
y_training.size
y_test.size

# Creating model
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(x_training,y_training)
score = reg.score(x_training,y_training)
score #R-squared

#Chart with training data
plt.scatter(x_training,y_training)
plt.plot(x_training,reg.predict(x_training),
         color = "darkred")

predict = reg.predict(x_test)

#Chart with test data
plt.scatter(x_test,y_test)
plt.plot(x_test,reg.predict(x_test),
         color = "pink");

predict2 = reg.predict(np.array(80000).reshape(1, -1))
predict2
# Out[31]: array([1951.4593068]) for 80000 cases 1951 deaths will fit
#simulation of 80000 new cases will result in 1951 new deaths

reg.intercept_
reg.coef_

# Performance metrics 
reg.score(x_test,y_test) #R-squared

from sklearn.metrics import mean_absolute_error, mean_squared_error

print("Mean absolute error (mae): ", mean_absolute_error(y_test, predict))
print("Mean squared error (mse): ", mean_squared_error(y_test, predict))
print("Root mean squared error (rmse): ", np.sqrt( mean_squared_error(y_test, predict)))
#smaller values are better

del reg, predict, predict2, x, y, x_test, x_training, y_test, y_training, score

# Polynomial regression

x = covid_brazil.iloc[:,0].values #0 is date
y = covid_brazil.iloc[:,5].values #6 is cumulative cases

x
#setting dates to numeric sequence (1,2,3...) and as column-matrix
x = np.arange(1,len(x)+1).reshape(-1,1)
x

#separate data into test-data and training-data
x_training , x_test, y_training, y_test = train_test_split(x ,y,
                                                           test_size = 0.25,
                                                           shuffle = True,
                                                           random_state = 2) #seed
x_training.size
x_test.size

# Creating model
from sklearn.preprocessing import PolynomialFeatures
# from sklearn.linear_model import LinearRegression

poly = PolynomialFeatures(degree = 2)
x_training_poly = poly.fit_transform(x_training)
x_test_poly     = poly.fit_transform(x_test)

reg = LinearRegression()
reg.fit(x_training_poly,y_training)
score = reg.score(x_training_poly,y_training)
score

predict = reg.predict(x_test_poly)
predict.size

#sequence for forecasting
forecast = np.arange(len(x)+20 ).reshape(-1, 1) # 20 days of forecasting
forecast.shape

x_training_total = poly.transform(forecast)
x_training_total.shape
x_training_total 

total_predict = reg.predict(x_training_total)
len(total_predict)
total_predict

plt.subplots(figsize = (10,5))
plt.plot(forecast[:-20], y, color = "red")
plt.plot(forecast, total_predict, linestyle = "dashed")
plt.title("Covid-19 cases in Brazil")
plt.ylabel("No. of cases")
plt.legend(["Cumulative cases","Forecast"]);


# Performance metrics 
score #R-squared

poly_test_pred = reg.predict(x_test_poly)

print("Mean absolute error (mae): ", mean_absolute_error(poly_test_pred,y_test)) #order doesn't matter
print("Mean squared error (mse): ", mean_squared_error(poly_test_pred,y_test))
print("Root mean squared error (rmse): ", np.sqrt( mean_squared_error(poly_test_pred,y_test)))
#smaller values are better

del reg, predict, x, y, x_test, x_training, y_test, y_training, score
del x_training_poly, x_test_poly, x_training_total, poly, poly_test_pred, total_predict
