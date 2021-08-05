import pandas as pd 
import numpy as np
import os
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


#import and make data clean :D
missing_value=['N/A',np.nan,'na']
df=pd.read_csv('/content/game.csv',na_values=missing_value)
#detecting NULL value
# df.isnull().sum()
df.isna().sum()
df=df.dropna() #drop the missing value or NA Value 
df.info()
df = df.drop(columns=['Name','Rank','Platform','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Publisher'])


X= df.drop(columns='Genre')
y= df['Genre']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)
model = DecisionTreeClassifier()
model.fit(X_train,y_train)
predictions = model.predict([ [2010,4.42] ])
print(predictions)
