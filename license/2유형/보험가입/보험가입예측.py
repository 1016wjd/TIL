import pandas as pd 

#데이터 로드
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/insurance/x_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/insurance/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/insurance/x_test.csv")



# 데이터 확인 > 분류모형  
# print(x_train.head()) # ID 삭제 
# print(y_train.head()) # ID 삭제
# print(x_test.head()) # ID 팝 

# 결측치 없음 
# print(x_train.isnull().sum()) 
# print(y_train.isnull().sum()) 
# print(x_test.isnull().sum()) 


# print(x_train.info()) # ID 삭제
# print(y_train.info()) # ID 삭제
# print(x_test.info()) # ID 팝 / id 삭제



# 데이터 전처리 
x_train = x_train.drop(columns=['ID','id'])
y_train = y_train.drop(columns=['ID'])
x_test_index = x_test.pop('ID')
x_test = x_test.drop(columns=['id'])




# 인코딩 
# 문자형변수 정리 Gender, Vehicle_Age, Vehicle_Damage 
# print(x_train.Vehicle_Damage.value_counts()) # 모두 3개 이하 > 원핫인코딩 
col = ['Gender', 'Vehicle_Age', 'Vehicle_Damage' ]

x_train_dummies = pd.get_dummies(data=x_train, columns=col)
x_test_dummies = pd.get_dummies(data=x_test, columns=col)




# 모델 학습 

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(x_train_dummies,y_train)
predict = model.predict(x_test_dummies)




print(pd.DataFrame({"ID" : x_test_index,  "Response": predict})).to_csv('./result.csv', index=False)

