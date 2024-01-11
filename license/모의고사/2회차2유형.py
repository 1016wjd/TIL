import pandas as  pd 

train= pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/stroke_/train.csv')
test= pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/stroke_/test.csv')

# 불필요한 컬럼 제거 id/ stroke 컬럼은 y
# print(train.head())
# print(test.head())

y_train = train.pop('stroke')
x_train = train.drop(columns=['id'])
x_test_index = test.pop('id')
x_test = test

# 컬럼/ 타입 확인 
# print(x_train.info())
# print(y_train.info())
# print(x_test.info())

# print(y_train.head())

# 결측치확인 
# print(x_train.isnull().sum()) # bmi
# print(y_train.isnull().sum())
# print(x_test.isnull().sum()) # bmi


# 결측치처리 
x_train['bmi'] = x_train['bmi'].fillna(x_train['bmi'].mean())
x_test['bmi'] = x_test['bmi'].fillna(x_test['bmi'].mean())

# print(x_train.isnull().sum()) # bmi
# print(y_train.isnull().sum())
# print(x_test.isnull().sum()) # bmi


# 정규화 
num = x_train.select_dtypes(exclude=object).columns

from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
x_train[num] = scaler.fit_transform(x_train[num])
x_test[num] = scaler.fit_transform(x_test[num])
x_train['age'] = x_train['age'].map(lambda x: x.replace("*",""))
x_train['age'] = x_train['age'].astype('int')

# 인코딩 
x_train = pd.get_dummies(x_train)
x_test = pd.get_dummies(x_test)

x_test['gender_Other'] = False

# print(x_train.info())
# print(x_test.info())

x_test = x_test[x_train.columns]

# # 모델링 과정
# from sklearn.model_selection import train_test_split
# X_train, X_val, Y_train, Y_val = train_test_split(x_train, y_train)

# from sklearn.ensemble import RandomForestClassifier
# model1 = RandomForestClassifier()
# model1.fit(X_train,Y_train)
# pred_val = model1.predict(X_val)


# from sklearn.metrics import accuracy_score
# print(accuracy_score(Y_val, pred_val))

# ## 최종모델링
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(x_train,y_train)
pred = model.predict(x_test)
result = pd.DataFrame({"id" : x_test_index, "stroke": pred})
# print(result['stroke'].value_counts())
result.to_csv('result2.csv',index=False)

# print(y_train.value_counts())