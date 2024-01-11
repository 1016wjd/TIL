import pandas as pd 

x_train = pd.read_csv('./data/train.csv')
x_test = pd.read_csv('./data/test.csv')

# 데이터 확인 ID 제거 
# print(x_train.head())
# print(x_test.head())

x_train = x_train.drop(columns=['ID'])
y_train = x_train.pop('Segmentation')
x_test_index = x_test.pop('ID')

# 결측치 없음 
# print(x_train.isnull().sum())
# print(y_train.isnull().sum())
# print(x_test.isnull().sum())

# 변수유형 확인 
# print(x_train.info())
# print(y_train.info())
# print(x_test.info())

# 인코딩 

x_train = pd.get_dummies(x_train)
x_test = pd.get_dummies(x_test)

# print(x_train.shape, x_test.shape)

# 모델링 
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(x_train, y_train)
predict = model.predict(x_test)

# print(predict)

# print(pd.DataFrame({"ID" : x_test_index , "Segmentation": predict}))

pd.DataFrame({"ID" : x_test_index , "Segmentation": predict}).to_csv('submission.csv',index=False)