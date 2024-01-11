import pandas as pd
## 데이터 로드
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/smoke/x_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/smoke/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/smoke/x_test.csv")

## 데이터 확인 > 분류
# print(x_train.head()) # ID 제거 
# print(y_train.head())
# print(x_test.head())
x_train = x_train.drop(columns=['ID','구강검진수검여부'])
y_train = y_train.drop(columns=['ID'])
x_test_index = x_test.pop('ID')
x_test = x_test.drop(columns=['구강검진수검여부'])

# print(x_train['구강검진수검여부'].value_counts())
# 한개의 값만 가지므로 제거 

## 결측치확인 
# print(x_train.info()) # 결측치가 있는 변수 : 없음 /범주형 : 성별코드, 구강검진수검여부, 치석
# print(y_train.info())
# print(x_test.info())
# print(x_train.isnull().sum())

## 인코딩 
col = ['성별코드', '치석']
x_train = pd.get_dummies(data=x_train, columns=col)
x_test = pd.get_dummies(data=x_test, columns=col)

## 데이터 분할 

from sklearn.model_selection import train_test_split
X_train, X_val, Y_train, Y_val = train_test_split(x_train,  y_train, test_size=0.2)

## 모델 생성 

from sklearn.ensemble import RandomForestClassifier

# model = RandomForestClassifier()
# model.fit(X_train, Y_train)
# predict_val = model.predict(X_val)



# from sklearn.metrics import accuracy_score
# print(accuracy_score(Y_val, predict_val))
#############################################################
model = RandomForestClassifier()
model.fit(x_train, y_train)
predict = model.predict(x_test)

print(pd.DataFrame({"ID": x_test_index, "흡연여부": predict}))
pd.DataFrame({"ID": x_test_index, "흡연여부": predict}).to_csv('./result.csv', index=False)