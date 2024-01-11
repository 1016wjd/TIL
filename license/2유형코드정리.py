import pandas as pd
# 1단계: 데이터 로드 
x_train = pd.read_csv("")
y_train = pd.read_csv("")
x_test = pd.read_csv("")

## 2단계:데이터 확인 
# 모델 > 분류 or 회귀
# 불필요한 컬럼 제거  
print(x_train.head())
print(y_train.head())
print(x_test.head())


# 결측치 확인
print(x_train.isnull().sum())
print(y_train.isnull().sum())
print(x_test.isnull().sum())


# 모델유형분류  
print(x_train.info())
print(y_train.info())
print(x_test.info())


# 3단계: 데이터 전처리 
## 불필요한 컬럼 제거
x_train = x_train.drop(columns=['ID'])
y_train = y_train.rop(columns=['ID'])
x_test_index = x_test.pop('ID')

## 결측치 처리 >> train, test 모두 해주어야함  
### 수치형변수 결측치처리 > 평균값으로 대체 
x_train['a'] = x_train['a'].fillna(round(x_train['a'].mean(),0))
x_test['a'] = x_test['a'].fillna(round(x_train['a'].mean(),0))
### 범주형변수 결측치처리 > 최빈값으로 대체 
x_train['b'] = x_train['b'].fillna(x_train['b'].mode())

## 4단계: 수치형변수 정규화 
# 수치형 변수컬럼 
num = x_train.select_dtypes(exclude=object).columns

from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
x_train[num] = scaler.fit_transform(x_train[num])
x_test[num] = scaler.fit_transform(x_test[num])

# 5단계 : 인코딩
# 라벨인코딩 >> 범주형변수의 범주가 너무 많은 경우 
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
x_train['b'] = encoder.fit_transform(x_train['b'])
x_test['b'] = encoder.fit_transform(x_test['b'])


## 인코딩 
x_train = pd.get_dummies(x_train)
x_test = pd.get_dummies(x_test)

## 컬럼순서 똑같게 하기 
x_test = x_test[x_train.columns]

# 6단계: 분류모델
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()
model.fit(x_train,y_train)
predict = model.predict(x_test)
prob = model.predict_proba(x_test)[:,1]

from sklearn.ensemble import RandomForestRegressor
model=RandomForestRegressor()
model.fit(x_train,y_train)
predict = model.predict(x_test)
prob = model.predict_proba(x_test)[:,1]

# 7단계: 결과제출
# print(prob)
print(pd.DataFrame({"ID": x_test_index, "predict": predict}))
pd.DataFrame({"ID": x_test_index, "predict": predict}).to_csv('./result.csv',index=False)

######################################################################################## 
# 참고 > 모델 스플릿 

from sklearn.model_selection import train_test_split
X_train, X_val, Y_train, Y_val = train_test_split(x_train, y_train, test_size=0.2)

# 여러개의 모델 돌려보기 ㅎㅎ 
# n_estimators = 10~300
# max_depth = 5~30

model1 = RandomForestClassifier(n_estimators=10, max_depth=20)
model1.fit(X_train, Y_train)
predict_val1 = model1.predict(X_val)
predict_val_prob = model1.predict_proba(X_val)

model2 = RandomForestClassifier(n_estimators=50, max_depth=5)
model2.fit(X_train, Y_train)
predict_val2 = model2.predict(X_val)

model3 = RandomForestClassifier(n_estimators=50, max_depth=10)
model3.fit(X_train, Y_train)
predict_val3 = model3.predict(X_val)

model4 = RandomForestClassifier(n_estimators=60, max_depth=10)
model4.fit(X_train, Y_train)
predict_val4 = model4.predict(X_val)

model5 = RandomForestClassifier(n_estimators=70, max_depth=10)
model5.fit(X_train, Y_train)
predict_val5 = model5.predict(X_val)



from sklearn.metrics import accuracy_score
print(accuracy_score(Y_val, predict_val1))
print(accuracy_score(Y_val, predict_val2))
print(accuracy_score(Y_val, predict_val3))
print(accuracy_score(Y_val, predict_val4))
print(accuracy_score(Y_val, predict_val5))

# 모델평가 
## 문제에서 묻는 것에 따라 모델 성능 확인하기

# 분류모델
# 정확도 (accuracy) , f1_score , recall , precision -> model.predict로 결과뽑기
# auc , 확률이라는 표현있으면 model.predict_proba로 결과뽑고 첫번째 행의 값을 가져오기 model.predict_proba()[:,1]
from sklearn.metrics import accuracy_score , f1_score, recall_score, roc_auc_score ,precision_score
print('train accuracy :', accuracy_score(Y_train,predict))
print('val accuracy :', accuracy_score(Y_val,predict_val1))
print('\n')
print('train f1_score :', f1_score(Y_train,predict))
print('val accuracy :', f1_score(Y_val,predict_val1))
print('\n')
print('train recall_score :', recall_score(Y_train,predict))
print('val recall_score :', recall_score(Y_val,predict_val1))
print('\n')
print('train precision_score :', precision_score(Y_train,predict))
print('val precision_score :', precision_score(Y_val,predict_val1))
print('\n')
print('train auc :', roc_auc_score(Y_train, prob))
print('val auc :', roc_auc_score(Y_val, predict_val_prob))

# 회귀모델 
import numpy as np
from sklearn.metrics import mean_squared_error , mean_absolute_error , mean_absolute_percentage_error ,r2_score
#mse 
print('validation mse' ,mean_squared_error(y_train,predict))
#mae 
print('validation mae' ,mean_absolute_error(y_train,predict))
#mape 
print('validation mape' ,mean_absolute_percentage_error(y_train,predict))
#rmse
print('validation rmse' ,np.sqrt(mean_absolute_percentage_error(y_train,predict)))
#r2
print('validation r2 score' ,r2_score(y_train,predict))