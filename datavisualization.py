# -*- coding: utf-8 -*-
"""DataVisualization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SpykKZEiN1I6Ri-HqdFHaU9Glv0Fc6G4
"""

#using the seaborn library
#importing the libraries
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""Note: seaborn has some built-in dataset"""

#total bill vs tip dataset
tips = sns.load_dataset('tips')
tips.head()

#visualize the tips dataset
sns.relplot(data=tips,x='total_bill',y='tip',col='time',hue='smoker',style='smoker',size='size')
plt.show()

#visualize the tips dataset
#setting a theme for the plots
sns.set_theme(style='darkgrid')
sns.relplot(data=tips,x='total_bill',y='tip',col='time',hue='smoker',style='smoker',size='size')
plt.show()

#load the iris dataset
iris=sns.load_dataset('iris')
iris.head()

sns.scatterplot(data=iris,x='sepal_length',y='sepal_width',hue='species')
plt.show()

#loading the titanic dataset
titanic=sns.load_dataset('titanic')
titanic.head()

titanic.shape

"""Count plot"""

sns.countplot(data=titanic,x='sex')
plt.show()

sns.countplot(x='survived',data=titanic,hue='alive')
plt.show()

"""Bar chart"""

sns.barplot(data=titanic,x='sex',y='age',hue='alive')
plt.show()

#house price dataset
from sklearn.datasets import fetch_california_housing
import pandas as pd
house_california=fetch_california_housing()
df=pd.DataFrame(house_california.data,columns=house_california.feature_names)
df['price']=house_california.target
print(house_california)

df.head()

"""Distribution plot"""

sns.distplot(df['price'])
plt.show()

"""correlation:
1.+ve correlation
2.-ve correlation
"""

correlation=df.corr()
#constructing a heat map
sns.heatmap(correlation,square=True,fmt='.1f',annot=True,annot_kws={'size':8},cmap='Blues')
plt.show()
#dark color says +vely correlated
