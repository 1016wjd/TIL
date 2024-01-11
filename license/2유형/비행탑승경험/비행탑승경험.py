import pandas as pd
#데이터 로드
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/airline/x_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/airline/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/airline/x_test.csv")


# 데이터 확인 
# print(x_train.head()) # ID 제거 
# print(y_train.head()) # ID 제거 
# print(x_test.head()) # ID 제거 

# 결측치확인 
# print(x_train.isnull().sum()) # ID ,id제거 /결측치 Arrival Delay in Minutes 
# print(y_train.isnull().sum()) # ID 제거 
# print(x_test.isnull().sum()) # ID, id제거 /결측치 Arrival Delay in Minutes

# 데이터 타입 확인 
# print(x_train.info()) # ID ,id제거 /결측치 Arrival Delay in Minutes 
# print(y_train.info()) # ID 제거 
# print(x_test.info()) # ID, id제거 /결측치 Arrival Delay in Minutes

# 불필요한 컬럼 삭제 
x_train = x_train.drop(columns=['ID','id'])
y_train = y_train.drop(columns=['ID'])
x_test_index = x_test.pop('ID')
x_test = x_test.drop(columns=['id'])


# 결측치 처리 

# print(x_train['Arrival Delay in Minutes'])
# print(round(x_train['Arrival Delay in Minutes'].mean(),0))
x_train['Arrival Delay in Minutes'] = x_train['Arrival Delay in Minutes'].fillna(round(x_train['Arrival Delay in Minutes'].mean(),0))
x_test['Arrival Delay in Minutes'] = x_test['Arrival Delay in Minutes'].fillna(round(x_train['Arrival Delay in Minutes'].mean(),0))

# print(x_train.isnull().sum())
# print(x_test.isnull().sum())

## 인코딩 
# 문자형  Gender/ Customer Type/ Type of Travel / Class

# >> 2~3개로 많지 않음! >> 원핫인코딩 
# print(len(x_train['Gender'].value_counts()))
# print(len(x_train['Customer Type'].value_counts()))
# print(len(x_train['Type of Travel'].value_counts()))
# print(len(x_train['Class'].value_counts()))
col = ['Gender', 'Customer Type', 'Type of Travel', 'Class']
x_train_dummies = pd.get_dummies(data=x_train, columns=col)
x_test_dummies = pd.get_dummies(data=x_test, columns=col)


# ## 데이터 스플릿 
# from sklearn.model_selection import train_test_split
# X_train, X_val, Y_train, Y_val = train_test_split(x_train_dummies, y_train, test_size=0.2)

# ## 모델학습 

# from sklearn.ensemble import RandomForestClassifier  
# model = RandomForestClassifier()
# model.fit(X_train, Y_train)
# predict_val_label = model.predict(X_val)
# predict_val_prob = model.predict_proba(X_val)[:,1]

# 모델 정확도 확인 
# from sklearn.metrics import accuracy_score
# print(accuracy_score(Y_val, predict_val_label))

# 모델선택 
from sklearn.ensemble import RandomForestClassifier  
model = RandomForestClassifier()
model.fit(x_train_dummies, y_train)
predict_label = model.predict(x_test_dummies)
predict_prob  = model.predict_proba(x_test_dummies)[:,0] # 확인하고 넣기

# print(predict_label,predict_prob )
# print(pd.DataFrame({"ID": x_test_index, "satisfaction": predict_label}))

# pd.DataFrame({"ID": x_test_index, "satisfaction": predict_label}).to_csv("./result.csv", index=False)



# print(pd.DataFrame({"ID": x_test_index, "satisfaction": predict_label}))
print(pd.DataFrame({"ID": x_test_index, "satisfaction_prob": predict_prob}))


