import pandas as pd 
import numpy as np
from sklearn.preprocessing import RobustScaler
from sklearn.ensemble import RandomForestRegressor

#데이터 로드
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/redwine/x_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/redwine/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/redwine/x_test.csv")

# 데이터확인  ## 아이디제거 
# print(x_train.head())  
# print(y_train.head())  
# print(x_test.head()) 

# 결측값 없음 
# print(x_train.isnull().sum())  
# print(y_train.isnull().sum())  
# print(x_test.isnull().sum()) 

# 데이터 유형 확인 >> 인코딩 필요없음 
# print(x_train.info())  
# print(y_train.info())  s
# print(x_test.info()) 

x_train = x_train.drop(columns=["ID"])
y_train = y_train.drop(columns=["ID"])
x_test_index = x_test.pop("ID")

# 수치형 인덱스 
num = x_train.select_dtypes(exclude=object).columns

# 정규화 
scaler = RobustScaler()
x_train = scaler.fit_transform(x_train[num])
x_test = scaler.fit_transform(x_test[num])
# x_test = x_test[x_train.columns]


model = RandomForestRegressor()
model.fit(x_train, y_train)
predict = model.predict(x_test)
# print({"ID": x_test_index, "quality": predict})
# print(pd.DataFrame({"quality": predict}))
pd.DataFrame({"ID": x_test_index, "quality": predict}).to_csv('./result.csv',index=False)
