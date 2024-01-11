import pandas as pd 
train= pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/train.csv')
test= pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/test.csv')
# submission= pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/bank/submission.csv')

# 모델 유형 >> 반응여부 >> 분류
# 불필요한 컬럼 제거 ID 
# print(train.head())
# print(test.head())
# print(submission.head())

# 결측치 없음 
# print(train.isnull().sum())
# print(test.isnull().sum())
# print(submission.isnull().sum())

# 모델유형분류  
# print(train.info())
# print(test.info())
# print(submission.info())

train = train.drop(columns=['ID'])
test_index = test.pop('ID')
y = train.pop('y')

## 정규화 
num = train.select_dtypes(exclude=object).columns
# print(num)

from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
train[num] = scaler.fit_transform(train[num])
test[num] = scaler.fit_transform(test[num])

## 인코딩 
train = pd.get_dummies(train)
test = pd.get_dummies(test)


# print(y.value_counts())
# 모델
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()
model.fit(train,y)
predict = model.predict(test)
prob = model.predict_proba(test)[:,1]
# print(prob)
print(pd.DataFrame({"ID": test_index, "predict": prob}))
pd.DataFrame({"ID": test_index, "predict": prob}).to_csv('./result.csv',index=False)