# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xsk9PcyN0ip58Y0wZXOoG-cFXeWcqauH
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
from sklearn import linear_model


df=pd.DataFrame({"name":["shoyab","harish","faizan","nivas","reddy","anil","ganesh","kishore","vamsi"],
                 "1st-sem":[7.5,3.2,6.2,8.5,7.4,7.5,4.2,9.2,8.5],
                 "2nd-sem":[7.6,3.1,5.9,8.3,7.4,8.5,4.5,9.5,8.2],
                 "3rd-sem":[8.2,2.9,5.6,8.8,8.4,7.9,3.8,9.0,8.6],
                 "4th-sem":[7.9,3.4,6.4,8.2,7.4,8.5,4.8,9.1,8.1]})


train=df.head(9)   
#im taking test data and trained data same

regr = linear_model.LinearRegression()
x = np.array(train[["1st-sem","2nd-sem","3rd-sem"]])
y = np.array(train[['2nd-sem']])
regr.fit (x, y)


y_hat=regr.predict(train[["1st-sem","2nd-sem","3rd-sem"]])




l=y_hat.tolist()
pre=[]
for i in l:
  pre.append(i[0])
j=0

accuracy=[]
for i in df["4th-sem"]:
  accuracy.append(round(((i-pre[j])/i)*100 , 5))
  j+=1



pdf=pd.DataFrame({"name":["shoyab","harish","faizan","nivas","reddy","anil","ganesh","kishore","vamsi"],
                 "1st-sem":[7.5,3.2,6.2,8.5,7.4,7.5,4.2,9.2,8.5],
                 "2nd-sem":[7.6,3.1,5.9,8.3,7.4,8.5,4.5,9.5,8.2],
                 "3rd-sem":[8.2,2.9,5.6,8.8,8.4,7.9,3.8,9.0,8.6],
                 "4th-sem":[7.9,3.4,6.4,8.2,7.4,8.5,4.8,9.1,8.1], "predicted 4th-sem":pre, "error(%)": accuracy
                  })



print(pdf)
print()

x = np.asanyarray(train[["1st-sem","2nd-sem","3rd-sem"]])
y = np.asanyarray(train[["4th-sem"]])
print("Residual sum of squares: %.2f"
#       % np.mean((y_hat - y) ** 2))


print('Variance: %.2f' % regr.score(x, y))