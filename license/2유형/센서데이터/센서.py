import pandas as pd
#데이터 로드
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/muscle/x_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/muscle/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/muscle/x_test.csv")


# print(x_train.head())
# print(y_train.head())
# print(x_test.head())

x_train = x_train.drop(columns=['ID'])
y_train = y_train.drop(columns=['ID'])
x_test_index = x_test.pop('ID')


print(x_train.isull().sum())
print(y_train.isull().sum())
print(x_test.isull().sum())


print(x_train.issull().sum())
print(y_train.issull().sum())
print(x_test.issull().sum())