import pandas as pd
#데이터 로드
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/studentscore/X_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/studentscore/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/studentscore/X_test.csv")

# print(x_train.head()) # StudentID 삭제 
# print(y_train.head()) # StudentID 삭제 
# print(x_test.head()) # StudentID 삭제 

# 결측치 없음 
# print(x_train.isnull().sum()) 
# print(y_train.isnull().sum()) 
# print(x_test.isnull().sum()) 


# print(x_train.info()) 
# print(y_train.info()) 
# print(x_test.info()) 


x_train_drop = x_train.drop(columns=['StudentID'])
y_train_drop = y_train.drop(columns=['StudentID'])
x_test_index = x_test.pop('StudentID')

# 인코딩 
x_train_dum = pd.get_dummies(x_train_drop)
x_test_dum = pd.get_dummies(x_test)
x_test_dum = x_test_dum[x_train_dum.columns]
# print(x_train_dum.info())



# 스케일링 
from sklearn.preprocessing import MinMaxScaler

# 데이터 나누기 
from sklearn.model_selection import train_test_split
X_train, X_val, Y_train, Y_val = train_test_split(x_train_dum, y_train_drop)


# 모델적합 
# from sklearn.ensemble import RandomForestRegressor 
# model = RandomForestRegressor()
# model.fit(X_train, Y_train)
# predict_val = model.predict(X_val)

# from sklearn.metrics import mean_squared_error
# print(mean_squared_error(Y_val, predict_val))




# 모델적합 
from sklearn.ensemble import RandomForestRegressor 
model = RandomForestRegressor()
model.fit(x_train_dum, y_train_drop)
predict = model.predict(x_test_dum)


pd.DataFrame({"StudentID": x_test_index, "G3": predict}).to_csv('./result.csv',index=False)
 