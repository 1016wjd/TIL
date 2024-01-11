import pandas as pd

## 1단계 데이터 로드
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/shipping/X_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/shipping/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/shipping/X_test.csv")


## 2단계 데이터 확인 
# ID 제거
# print(x_train.head()) 
# print(y_train.head())
# print(x_test.head())

# 결측치 없음 
# print(x_train.info())
# print(y_train.info())
# print(x_test.info())

x_train = x_train.drop(columns=['ID'])
x_test_index = x_test.pop('ID')
y_train = y_train.drop(columns=['ID'])



## 3단계 Warehouse_block
# print(x_train['Warehouse_block'].value_counts())
# print(x_train['Mode_of_Shipment'].value_counts())
# print(x_train['Customer_care_calls'].value_counts())
# print(x_train['Product_importance'].value_counts())
# print(x_train['Gender'].value_counts())

# 원핫인코딩 
col = ['Warehouse_block','Mode_of_Shipment','Customer_care_calls','Product_importance','Gender']
x_train= pd.get_dummies(data= x_train, columns=col)
x_test = pd.get_dummies(data= x_test, columns=col)
# print(x_train)



## 4단계 - 데이터 나누기 
from sklearn.model_selection import train_test_split
# print(help(train_test_split))
X_train, X_val, Y_train, Y_val = train_test_split(x_train, y_train, test_size=0.2)


## 5단계 
from sklearn.ensemble import RandomForestClassifier

# n_estimators = 10~300
# max_depth = 5~30

# model1 = RandomForestClassifier(n_estimators=10, max_depth=20)
# model1.fit(X_train, Y_train)
# predict_val1 = model1.predict(X_val)


# model2 = RandomForestClassifier(n_estimators=50, max_depth=5)
# model2.fit(X_train, Y_train)
# predict_val2 = model2.predict(X_val)

# model3 = RandomForestClassifier(n_estimators=50, max_depth=10)
# model3.fit(X_train, Y_train)
# predict_val3 = model3.predict(X_val)

# model4 = RandomForestClassifier(n_estimators=60, max_depth=10)
# model4.fit(X_train, Y_train)
# predict_val4 = model4.predict(X_val)

# model5 = RandomForestClassifier(n_estimators=70, max_depth=10)
# model5.fit(X_train, Y_train)
# predict_val5 = model5.predict(X_val)



# from sklearn.metrics import accuracy_score
# print(accuracy_score(Y_val, predict_val1))
# print(accuracy_score(Y_val, predict_val2))
# print(accuracy_score(Y_val, predict_val3))
# print(accuracy_score(Y_val, predict_val4))
# print(accuracy_score(Y_val, predict_val5))


model = RandomForestClassifier(n_estimators=70, max_depth=10)
model.fit(x_train, y_train)
predict = model.predict(x_test)

## test 예측 

pd.DataFrame({'ID': x_test_index, 'Reached.on.Time_Y.N': predict}).to_csv('./result_02.csv', index=False)