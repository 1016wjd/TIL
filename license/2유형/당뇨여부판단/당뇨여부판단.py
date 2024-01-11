import pandas as pd 

# 데이터로드
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/diabetes/x_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/diabetes/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/diabetes/x_test.csv")

# 불필요한 컬럼 제거 : ID >> 분류모델
# print(x_train.head())
# print(y_train.head())
# print(x_test.head())

# 결측치확인 > 결측치 없음 
# print(x_train.isnull().sum())
# print(y_train.isnull().sum())
# print(x_test.isnull().sum())

# 범주형변수 없음 
# print(x_train.info())
# print(y_train.info())
# print(x_test.info())

x_train = x_train.drop(columns=['ID'])
y_train = y_train.drop(columns=['ID'])
x_test_index = x_test.pop('ID')
print(x_train.info())
print(y_train.info())
print(x_test.info())

# 모델적합 
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(x_train,y_train)
predict = model.predict(x_test)

print(pd.DataFrame({"ID": x_test_index, "Outcome":predict}))
pd.DataFrame({"ID": x_test_index, "Outcome":predict}).to_csv('./result.csv',index=False)