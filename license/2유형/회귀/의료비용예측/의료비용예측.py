import pandas as pd
#데이터 로드
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/MedicalCost/x_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/MedicalCost/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/MedicalCost/x_test.csv")

# 데이터 확인 
# print(x_train.head()) # 제거 ID
# print(y_train.head()) # 제거 ID
# print(x_test.head()) # 제거 ID

# 결측치확인 없음 
# print(x_train.isnull().sum()) 
# print(y_train.isnull().sum()) 
# print(x_test.isnull().sum()) 

x_train = x_train.drop(columns=['ID'])
y_train = y_train.drop(columns=['ID'])
x_test_index = x_test.pop('ID')


# print(x_train.info()) 
# print(y_train.info()) 
# print(x_test.info())
num = ['age', 'bmi','children']

# 인코딩 
x_train = pd.get_dummies(x_train)
x_test = pd.get_dummies(x_test)

# 스케일링
from sklearn.preprocessing import RobustScaler
scale = RobustScaler()
x_train[num] = scale.fit_transform(x_train[num])
x_test[num] = scale.fit_transform(x_test[num])
x_test[x_train.columns]

# print(x_train.shape, x_test.shape)


# 스플릿 

# from sklearn.model_selection import train_test_split
# X_train, X_val, Y_train, Y_val = train_test_split(x_train, y_train, test_size=0.2)

# from sklearn.ensemble import RandomForestRegressor
# model = RandomForestRegressor()
# model.fit(X_train, Y_train)
# predict_val = model.predict(X_val)

# from sklearn.metrics import mean_squared_error
# import numpy as np
# print(np.sqrt(mean_squared_error(Y_val, predict_val)))



from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(x_train, y_train)
predict = model.predict(x_test)



print(pd.DataFrame({"ID": x_test_index, "charges": predict}))
pd.DataFrame({"ID": x_test_index, "charges": predict}).to_csv('./result.csv', index=False)