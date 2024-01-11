import pandas as pd 
x_train = pd.read_csv('./train.csv')
x_test = pd.read_csv('./test.csv')

## 회귀모형 

# 불필요한 컬럼 없음 # price 
# print(x_train.head())
# print(x_test.head())

# 결측치 없음 
# print(x_train.isnull().sum())
# print(x_test.isnull().sum())

y_train = x_train.pop('price')

# print(x_train.info())
# print(x_test.info())

# 인코딩 
x_train = pd.get_dummies(x_train)
x_test = pd.get_dummies(x_test)

# 모델적합 
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(x_train, y_train)
predict = model.predict(x_test)


    
pd.DataFrame({"pred": predict }).to_csv("./result.csv", index=False)