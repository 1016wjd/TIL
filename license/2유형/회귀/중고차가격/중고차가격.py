import pandas as pd
#데이터 로드
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/carsprice/X_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/carsprice/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/carsprice/X_test.csv")

# 데이터 확인 
# print(x_train.head()) # 제거 : carID
# print(y_train.head()) # carID
# print(x_test.head()) # carID


# 결측치없음
# print(x_train.isnull().sum()) 
# print(y_train.isnull().sum()) 
# print(x_test.isnull().sum()) 

# # 데이터 확인 
# print(x_train.info()) 
# print(y_train.info()) 
# print(x_test.info()) 

# 불필요한 열 제거 
x_train = x_train.drop(columns=['carID'])
x_test_index = x_test.pop('carID')
y_train = y_train.drop(columns=['carID'])

# 인코딩
x_train_dum = pd.get_dummies(x_train)
x_test_dum = pd.get_dummies(x_test)
x_test_dum['model_ M6'] = 0
x_test_dum = x_test_dum[x_train_dum.columns]

# (4960, 113) (2672, 112) 한개의 행이 누락된 것 발견  'model_ M6'

# print(x_train_dum.shape, x_test_dum.shape)
# print[x_test_dum[x_train_dum.columns]]

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(x_train_dum,y_train)
predict_test = model.predict(x_test_dum)


# print(pd.DataFrame({"carID" : x_test_index ,"price": predict_test}))
pd.DataFrame({"carID" : x_test_index ,"price": predict_test}).to_csv('./result.csv',index=False)