import pandas as pd
#데이터 로드
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/hyundai/x_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/hyundai/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/hyundai/x_test.csv")


# 데이터확인 > ID제거
# print(x_train.head()) 
# print(y_train.head())
# print(x_test.head())

x_train = x_train.drop(columns=['ID'])
x_test_index = x_test.pop('ID')
y_train = y_train.drop(columns=['ID'])


# 결측치없음 
# print(x_train.isnull().sum())
# print(y_train.isnull().sum())
# print(x_test.isnull().sum())


# print(x_train.info())
# print(y_train.info())
# print(x_test.info())

# 인코딩 
x_train = pd.get_dummies(x_train)
x_test = pd.get_dummies(x_test)


# 스케일링
num = ['mileage', 'tax(£)', 'mpg','engineSize']

from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
x_train[num] = scaler.fit_transform(x_train[num])
x_test[num] = scaler.fit_transform(x_test[num])

x_train['fuelType_Other'] = False
x_test['model_ Veloster'] = False


# print(x_train.shape, x_test.shape)
# print(x_train.info())
# print(x_test.info())

x_test = x_test[x_train.columns]


# # 모델링 
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor()
model.fit(x_train, y_train)
predict = model.predict(x_test)

print(pd.DataFrame({"ID": x_test_index, "price": predict}))
pd.DataFrame({"ID": x_test_index, "price": predict}).to_csv('./result.csv',index=False)