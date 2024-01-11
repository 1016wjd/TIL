import pandas as pd 

#데이터 로드 >> 회귀
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/admission/x_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/admission/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/admission/x_test.csv")

# print(x_train.head())
# print(y_train.head())
# print(x_test.head())

# print(x_train.isnull().sum())
# print(y_train.isnull().sum())
# print(x_test.isnull().sum())

# print(x_train.info())
# print(y_train.info())
# print(x_test.info())

x_train = x_train.drop(columns=["ID"])
y_train = y_train.drop(columns=["ID"])
x_test_index = x_test.pop("ID")


num = x_train.select_dtypes(exclude=object).columns
# print(num)

# # 스케일링
from sklearn.preprocessing import RobustScaler
scale = RobustScaler()
x_train[num] = scale.fit_transform(x_train[num])
x_test[num] = scale.fit_transform(x_test[num])
x_test = x_test[x_train.columns]

# import sklearn
# print(sklearn.__all__)

# from sklearn.model_selection import train_test_split
# X_train, X_val, Y_train, Y_val = train_test_split(x_train, y_train, test_size=0.2)


# from sklearn.ensemble import RandomForestRegressor
# model1 = RandomForestRegressor()
# model1.fit(X_train, Y_train)
# predict_val = model1.predict(X_val)


# from sklearn.metrics import mean_squared_error
# print(mean_squared_error(Y_val, predict_val))

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(x_train, y_train)
predict = model.predict(x_test)

print(pd.DataFrame({"ID": x_test_index, "Chance of Admit": predict}))

pd.DataFrame({"ID": x_test_index, "Chance of Admit": predict}).to_csv('./result.csv', index=False)