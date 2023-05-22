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

## Bar Chart

# Matplotlib library
import matplotlib.pyplot as plt

bar_graph = sars_edited.sex.value_counts()
bar_graph

# vertical bar plot
plt.bar(bar_graph.index, bar_graph, color = "darkred")
plt.title("Sex distribution")
plt.ylabel("Quantity")
plt.xlabel("Sex")
plt.show()

#horizontal bar plot

plt.barh(bar_graph.index, bar_graph, color = "darkred")
plt.title("Sex distribution")
plt.xlabel("Quantity")
plt.ylabel("Sex")
plt.show()

# Seaborn library

import seaborn as sns
# vertical
sns.countplot(x = "sex", data = sars_edited); #';" to not show message in Out

#horizontal
sns.countplot(y = "sex", data = sars_edited); #';" to not show message in Out

fig, ax = plt.subplots(figsize = (8,6))
sns.countplot(x = "race", data = sars_edited)
ax.set_title("Race Distribution", fontdict = {"fontsize": 20})
ax.set_xlabel("Race", fontdict = {"fontsize": 15})
ax.set_ylabel("Quantity", fontdict = {"fontsize": 15});

# Plotly library

import plotly.express as px
#this import is because .show() wasn't working
import plotly.io as pio
pio.renderers.default='browser'

#in plotly it need to be in dataframe type
bar_graph2 = bar_graph.rename_axis('sex').reset_index(name='counts')
bar_graph2

bar_plotly = px.bar(bar_graph2, x = "sex", y = "counts" ,
                    title = "Sex distribution" )
bar_plotly.show()

del bar_graph, bar_graph2, bar_plotly, fig, ax

## Box Plot

# first creating age variable by years old
sars_edited.TP_IDADE.value_counts().sort_index()
sars_edited.age.value_counts().sort_index()

sars_edited.age.describe()

sars_edited.age.mode()

sars_edited.loc[sars_edited["TP_IDADE"] == 1, "age"] = 0
sars_edited.loc[sars_edited["TP_IDADE"] == 2, "age"] = 0

sars_edited.describe()

# Plotly library

import plotly.express as px
#this import is because .show() wasn't working
import plotly.io as pio
pio.renderers.default='browser'


box_plotly = px.box(sars_edited, y  ="age")
box_plotly.show()

sars_edited_no_outliers = sars_edited.loc[sars_edited.age < 118]

box_plotly = px.box(sars_edited_no_outliers, y  ="age")
box_plotly.show()

box_plotly = px.box(sars_edited_no_outliers, y  ="age", x = "sex")
box_plotly.show()

box_plotly = px.box(sars_edited_no_outliers, y  ="age", x = "race")
box_plotly.show()

del box_plotly

# Seaborn library

import seaborn as sns

sns.boxplot(y = "age", data = sars_edited_no_outliers, color = "darkred")

sns.boxplot(y = "age", x = "sex", data = sars_edited_no_outliers)

sns.boxplot(y = "age", x = "CS_ZONA", data = sars_edited_no_outliers)

sns.boxplot(y = "age", x = "CS_ZONA", hue = "sex", data = sars_edited_no_outliers)

# Matplotlib library
import matplotlib.pyplot as plt

plt.boxplot(sars_edited_no_outliers.age)
plt.title("Age Box Plot")
plt.xlabel("Age")
plt.show()

# Histogram
# Plotly library
import plotly.express as px
#this import is because .show() wasn't working
import plotly.io as pio
pio.renderers.default='browser'

hist = px.histogram(sars_edited, x = "age", nbins = 60)
hist.update_layout(width = 800, height = 500, title_text = "Age distribution")
hist.show()

# Normality analysis - QQ Plot

sars_edited.age.describe()
sars_edited.age.mode()

import scipy.stats as stats
import matplotlib.pyplot as plt

stats.probplot(sars_edited.age, dist = "norm", plot = plt)
plt.title("Normality Analysis")
plt.show()

# Normality analysis - Kolmogorov-Smirmov Test

# when p>0.05 it has a normal dist.

#THIS PART IT ISN'T RUNNING
#"""
import statsmodels
from statsmodels import lilliefors

statistic_ks, p_ks = statsmodels.stats.diagnostic.lilliefors(sars_edited.age,
                                                             dist = "norm")
print("Test statistic =",round(statistic_ks,2))
print("P value =", p_ks)
#"""

# Histogram
# Seaborn library

import seaborn as sns
fig, ax = plt.subplots(figsize = (8,6))
sns.histplot(sars_edited, x = "age", bins = 20, color = "darkred",
             kde = True, stat = "count");
ax.set_title("Age distribution")

del fig, ax
# Matplotlib library
import matplotlib.pyplot as plt

plt.hist(sars_edited.age, color = "darkred", density=False, bins = 20)
plt.title("Age distribution")
plt.xlabel("Age")
plt.show()

# Scatter Plot

#selecting one city from data
sars_edited.ID_MN_RESI.head()

sars_catanduva = sars_edited.loc[sars_edited.ID_MN_RESI == "CATANDUVA"]
sars_catanduva

# Matplotlib library
import matplotlib.pyplot as plt
plt.scatter(sars_catanduva.date, sars_catanduva.age)
plt.title("Linear Correlation")
plt.xlabel("Date")
plt.ylabel("Age")
plt.show()

# Seaborn library
import seaborn as sns
fig, ax = plt.subplots(figsize = (8,6))
sns.scatterplot(sars_catanduva, y = "age", x = "date", color = "darkred");
ax.set_title("Linear Correlation")
ax.set_xlabel("Dates")
ax.set_ylabel("Age")

# Plotly library
import plotly.express as px
#this import is because .show() wasn't working
import plotly.io as pio
pio.renderers.default='browser'

scatter = px.scatter(sars_catanduva, x = "date", y = "age", color = "sex")
scatter.update_layout(width = 800, height = 500, title_text = "Linear Correlation")
scatter.update_xaxes(title = "Date")
scatter.update_yaxes(title = "Age")
scatter.show()

del sars_catanduva, scatter
# Pie chart
# Plotly library
sars_edited.sex.value_counts()

piechart = px.pie(sars_edited, "sex")
piechart.show()
piechart = px.pie(sars_edited, "race")
piechart.show()

# Matplotlib library
counts_race = sars_edited.race.value_counts()

plt.figure(figsize = (8,8))
plt.pie(counts_race, labels = counts_race.index, autopct = "% .2f %%") # % with 2 decimals
plt.title("Pie Chart")
plt.show()

del piechart, counts_race
# Scatter plot with bubbles

#selecting one city from data

sars_tupa = sars_edited.loc[sars_edited.ID_MN_RESI == "TUPA"]
sars_tupa
# Plotly library
bubbles = px.scatter(sars_tupa, x = "date", y = "CS_ZONA", color = "sex", size = "age")
bubbles.show()
bubbles = px.scatter(sars_tupa, x = "date", y = "race", color = "sex", size = "age")
bubbles.show()

# Seaborn library
fig, ax = plt.subplots(figsize = (8,6))
sns.scatterplot(sars_tupa, y = "race", x = "date", color = "darkred", size = "age");
ax.set_title("Bubble Chart")
ax.set_xlabel("Dates")
ax.set_ylabel("Age")

del fig, ax, sars_tupa, bubbles
# Line Chart
## in sars data there isn't a variable that suits for this type of chart, so it'll be created one

# Matplotlib library
plt.subplots(figsize = (8,6))
y = [4,9,6,4,0,3,5.1,6,8.4,12.3]
x = range(len(y))
plt.plot(x,y, color = "darkred", marker = "o")
plt.title("Line Chart")
plt.show()

# Plotly library

type(y)
type(x)
x = list(x)
type(x)
print(x)

df = pd.DataFrame(x, columns = ["x"])
df = pd.concat([df,pd.DataFrame(y, columns = ["y"])], axis = 1)
df

line_chart = px.line(df, "x", "y")
line_chart.show()

# Seaborn library
fig, ax = plt.subplots(figsize = (8,6))
sns.lineplot(x = x, y = y)
ax.set_title("Line Chart")
ax.set_xlabel("X")
ax.set_ylabel("Y");