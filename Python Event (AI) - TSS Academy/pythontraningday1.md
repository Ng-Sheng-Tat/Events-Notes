## Day 1

- used webbased or jupyter notebook
**Commands in python**
1. ``print``
2. ``if-else``
3. ``for-loops``
4. ``while-loops``

**CEPP Python certification pathway**

**Python Applications**
1. Basics Python
2. Data Structure
3. Object Oriented Programming Language
4. SQL CRUD operations
5. Network Socket, REST API, json & json-server, XML, request, configuration file
6. Others like decorator, generator, lambda, exception, pip, pyc, pypi, namespace, virtuals environment, multiple variable, configuration, multi-threading, pipe, file, magic, tktinker, pickle & shelve
7. AI like regressions and decision tree
8. Excel Using Python
---
**Excel Function**
```
=countif(range, "No") -> return no accumulation
=countif(range, "Yes")
--> Imbalance data
use SMOTE data to balance either over_sampling or under_samplig
```
---
Import the balanced data into the google workspace for AI application)
```
# import the data into the system
import pandas as pd # naming convention

# read the csv file
df = pd.read_csv("filename.csv or pathname")

dir(pd) # to display all the function for pandas

dir(df) # to display all the function for data frame

# to view the data frame
print(df)

# select column
df = df.loc[:, ["column1", "column2"]]
print(df)

# remove na
df = df.dropna()
print(df)

# replace with numbers
df["default"] = df["default"].replace("Yes", :No)

# remove the outliers
import numpy as np
from scipy import stats

z = stats.zscore(df.astype(np.float))

z = np.abs(z)

f = (z < 3).all(axis=1)

df = df[f]

df.describe()

df.corr() # -> correlation, data description
# the higher the correlation, the more relationship between variables
# negative means inversely proportional meaning

import seaborn as sns

sns.heatmap(df.corr()) # plot a matrix

dir(sns)
```
