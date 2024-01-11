import pandas as pd
train = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/ep6_p2_train.csv')
test = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/ep6_p2_test.csv')

# 모델 >> 분류모델 
# 불필요한 컬럼 ID

x_train = train.drop(columns=["ID"])
y_train = x_train.pop('General_Health')
x_test_index = test.pop('ID')
x_test = test

# 인코딩 필요함 / 정규화 필요함 
# print(x_train.info())
# print(y_train.info())
# print(x_test.info())

# 결측치확인 
# print(x_train.isnull().sum())
# print(y_train.isnull().sum())
# print(x_test.isnull().sum())


# 정규화 
num = x_train.select_dtypes(exclude=object).columns
# print(num)
from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
x_train[num] = scaler.fit_transform(x_train[num])
x_test[num] = scaler.fit_transform(x_test[num])

# 인코딩 
x_train = pd.get_dummies(x_train)
x_test = pd.get_dummies(x_test)

# print(x_train.shape, x_test.shape)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(x_train,y_train)
predict = model.predict(x_test)

print(pd.DataFrame({"ID": x_test_index, "predict" : predict}))