## Python Day 2

### Regressions as the most popular machine learning model for continuous data predictions

- Error algorithm is RMSE
- correlation and dependence
- used widely for supervised learning for trend prediction, pattern recognition.
- simplest and oversimplified but not the best due to assumptions that have been made
- error testing using Q-Q way and heteroscedasticity
- simple model not subject to overfitting
- linear regression, polynomial, exponential, logarithm regression, Ridge (good for multivariable), Lasso (good for multivariable), quantile, MARS (Adaptive) regressions ...
- ANOVA table (R-test, F-test, T-test)
- uses R-studio (R-studio cloud) or Python for data-science and machine learning

**Python Code (CSV)**
```
upload the csv file

import pandas as pd

df = pd.read_csv("filepath.csv")

print(df)

x = df.loc[:, ["SGD"]]

print(x)

y = df.loc[:, ["DBS"]]

print(y)

# use linear model
from sklearn import linear_model

model = linear_model.LinearRegression()

# train the model, not split train test
model.fit(X, Y)

pred = model.predict(X)

print(pred)

# to know the error by matrix
from sklearn.metrics import mean_square_error

rmse = mean_square_error(Y, pred) ** 0.5

print(rmse)

model.coef_

model.intercept_

```

**R-code (CSV)**
```
a = 1
print(a) # highlight and control enter to run in R-studio, not shift enter

a = "hello"
print(a)

name = readline(prompt="What is your name: ")
print(name)

# if-else
d = 1
if (d == 0) # bracket is mandatory
{print("d is one")} else if (d==2)
{print("d is two")} else
{print("d is not one or two")}

# for loops
e = 1
while (e<5) {
  print(e)
  e = e + 1
}

# import the file into R-studio
library(data.table)
dt = fread("filenam.csv")

model = lm(dt$DBS ~ dt$SDG)
# navigate to the model by clicking the workspace object to get insightful information from them

pred = predict(model, newdata = dt)
print(pred)

error = dt$DBS - pred
print(error)

rmse = mean(error^2)^0.5
print(rmse)
```

**Excel**
Data->Data-Analysis->Regressions->Insert X-range, Y-range(with label and confidence level)->New workbook there will be coefficient generated
Make a new row for prediction and error, square error separately, calculate sum of error square (so that positive and negative do not erase each others), Mean square error sum/count, RMSE = MSE-square-root

**Email**
```
ang.jinfeng@tssglobalsingapore.com
tssacademysg.com
teohteiktoe@gmail.com
ang.jinfeng@tssglobalsingapore.com
```
