import pandas as pd
#데이터 로드
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/waters/x_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/waters/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/waters/x_test.csv")


# 데이터 확인 
# print(x_train.head()) # ID 삭제 
# print(y_train.head()) # ID 삭제 
# print(x_test.head()) # ID 삭제 


# # 데이터 정보 
# print(x_train.isnull().sum()) # 결측치 ph Sulfate Trihalomethanes
# print(y_train.isnull().sum())
# print(x_test.isnull().sum()) # 결측치 ph Sulfate Trihalomethanes

# 데이터 타입 확인 > 모두 숫자형 데이터 (정수형)
# print(x_train.info()) 
# print(y_train.info())
# print(x_test.info())

# print(x_train.describe())

# 데이터 전처리 
# 삭제 
x_train = x_train.drop(columns=['ID'])
y_train = y_train.drop(columns=['ID'])
x_test_index = x_test.pop('ID')

# 결측치처리 
# 결측치 ph Sulfate Trihalomethanes
x_train['ph'] = x_train['ph'].fillna(x_train['ph'].mean())
x_train['Sulfate'] = x_train['Sulfate'].fillna(x_train['Sulfate'].mean())
x_train['Trihalomethanes'] = x_train['Trihalomethanes'].fillna(x_train['Trihalomethanes'].mean())

x_test['ph'] = x_test['ph'].fillna(x_train['ph'].mean())
x_test['Sulfate'] = x_test['Sulfate'].fillna(x_train['Sulfate'].mean())
x_test['Trihalomethanes'] = x_test['Trihalomethanes'].fillna(x_train['Trihalomethanes'].mean())

# 결측치 한번더 확인 > 모두 채워짐 
# print(x_train.isnull().sum()) # 결측치 ph Sulfate Trihalomethanes
# print(y_train.isnull().sum())
# print(x_test.isnull().sum()) # 결측치 ph Sulfate Trihalomethanes


## 인코딩 필요없음 

# 모델생성 및 평가 train val
# from sklearn.model_selection import train_test_split
# X_train, X_val, Y_train, Y_val = train_test_split(x_train, y_train,test_size=0.2)

# from sklearn.ensemble import RandomForestClassifier
# model = RandomForestClassifier()
# model.fit(X_train, Y_train)
# predict_val_label = model.predict(X_val)



# from sklearn.metrics import accuracy_score
# print(accuracy_score(Y_val,predict_val_label))

# 모델적합 train test
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(x_train, y_train)
predict_label = model.predict(x_test)

print(pd.DataFrame({"ID": x_test_index, "Potability": predict_label}))
