import pandas as pd 

#데이터 로드
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/audit/x_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/audit/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/audit/x_test.csv")


# ID 제거 
# print(x_train.head())
# print(y_train.head())
# print(x_test.head())

x_train = x_train.drop(columns=['ID'])
y_train = y_train.drop(columns=['ID'])
x_test_index = x_test.pop('ID')

# 결측값 Money_Valued에 있음  float64
# print(x_train.isnull().sum())
# print(y_train.isnull().sum())
# print(x_test.isnull().sum())

# print(x_train.info())
# print(y_train.info())
# print(x_test.info())


# 결측값 대체하기 
# print(x_train['Money_Value'] )
x_train['Money_Value'] = x_train['Money_Value'].fillna(x_train['Money_Value'].mean())
x_test['Money_Value'] = x_test['Money_Value'].fillna(x_test['Money_Value'].mean())

# print(x_train.isnull().sum())
# print(x_test.isnull().sum())

# 인코딩 
x_train = pd.get_dummies(x_train)
x_test= pd.get_dummies(x_test)

# print(set(x_train.columns) - set(x_test.columns))
set_list1 = list(set(x_train.columns) - set(x_test.columns))
set_list2 = list(set(x_test.columns) - set(x_train.columns))
# print(set_list1)

for i in set_list1:
    x_test[i] = False
    
for i in set_list2:
    x_train[i] = False
    
x_test = x_test[x_train.columns]
# print(x_train.shape, x_test.shape)

# 모델적합 > 분류모델 

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(x_train, y_train)
predict = model.predict(x_test)

print(pd.DataFrame({"ID" : x_test_index , "Risk": predict }))
pd.DataFrame({"ID" : x_test_index , "Risk": predict }).to_csv('./result.csv', index=False)