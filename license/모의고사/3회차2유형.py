import pandas as pd 

x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/muscle/x_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/muscle/y_train.csv")
test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/muscle/x_test.csv")

# 모델 분류모델 > RandomForestClassifier
# 불필요한 열 제거 ID 
# print(x_train.head())
# print(y_train.head())
# print(test.head())

# 결측치확인 
# print(x_train.isnull().sum())
# print(y_train.isnull().sum())
# print(test.isnull().sum())

## 모두 숫자형변수이므로 인코딩 필요없음 
# print(x_train.info())
# print(y_train.info())
# print(test.info())

x_train = x_train.drop(columns=["ID"])
y_train = y_train.drop(columns=["ID"])
test_index = test.pop('ID')

## 정규화 

from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
x_train = scaler.fit_transform(x_train)
test = scaler.fit_transform(test)

## 모델적합 
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(x_train,y_train)
predict = model.predict(test)


result = pd.DataFrame({"ID": test_index, "pose": predict})
# print(result)
result.to_csv('./result3.csv', index=False)