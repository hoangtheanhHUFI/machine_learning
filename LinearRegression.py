import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model,datasets

#import CSV using pandas su li csv
data= pd.read_csv('machine_learning/data_hw.csv')
data.info()
data[['Height','Weight']].head(20)
#Dung Data ve len plt
x_bar=data['Height']
y_bar=data['Weight']
plt.plot(y_bar,x_bar,'ro')
plt.title('Biểu đồ cân nặng và chiều cao')
plt.xlabel('Chiều Cao (cm)')
plt.ylabel('Cân Nặng(kg)')
plt.show()
#Bieu do cho thay su tuyen tinh => Chieu cao va can nang ti le thuan => Co the Dung linear regression.
lnrgs=linear_model.LinearRegression()
#Chuyển dữ liệu từ pandas sang numpy
newXbar=np.array(x_bar)
newYbar=np.array(y_bar)
#vẽ line
lnrgs.fit(newYbar.reshape(-1, 1),newXbar) #vì cần dùng mảng 2 chiều nên .reshape()
plt.plot(y_bar,x_bar,'ro')
plt.title('Biểu đồ cân nặng và chiều cao')
plt.xlabel('Chiều Cao (cm)')
plt.ylabel('Cân Nặng(kg)')
plt.plot(newYbar,lnrgs.predict(newYbar.reshape(-1, 1)))
#kiem thu  chieu cao => Can nang 
kiem_thu=(160,165,190)
for chieucao in kiem_thu: 
  print(lnrgs.predict([[chieucao]]))
