import pandas as pd
#데이터 로드
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/drug/x_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/drug/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/drug/x_test.csv")

#  데이터확인 > ID 삭제 
# print(x_train.head())
# print(y_train.head())
# print(x_test.head())

# 결측치확인 > 없음 
# print(x_train.isnull().sum())
# print(y_train.isnull().sum())
# print(x_test.isnull().sum())

x_train = x_train.drop(columns=['ID'])
y_train = y_train.drop(columns=['ID'])
x_test_index = x_test.pop('ID')

# 변수유형확인 
# print(x_train.info())
# print(y_train.info())
# print(x_test.info())

# print(x_train.describe()) 
num = ['Age', 'Na_to_K']

# 스케일링 
from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
x_train[num] = scaler.fit_transform(x_train[num])
x_test[num] = scaler.fit_transform(x_test[num])


# 인코딩 

x_train = pd.get_dummies(x_train)
x_test = pd.get_dummies(x_test)
x_test = x_test[x_train.columns]
# print(x_train.shape, x_test.shape)

# 모델적합 

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(x_train, y_train)
predict = model.predict(x_test)

print(pd.DataFrame({"ID": x_test_index, "Drug": predict}))
pd.DataFrame({"ID": x_test_index, "Drug": predict}).to_csv('./result.csv', index=False)