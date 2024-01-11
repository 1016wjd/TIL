import pandas as pd 

## 1단계 데이터 로드  > 분류모형 
x_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/HRdata/X_train.csv")
y_train = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/HRdata/y_train.csv")
x_test= pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/HRdata/X_test.csv")


## 2단게 데이터 전처리 > 불필요한 컬럼 / 결측치

# 불필요한 컬럼 
# print(x_train.head()) # 불필요한 컬럼 : enrollee_id   
# print(y_train.head()) # 불필요한 컬럼 : enrollee_id (pop)
# print(x_test.head()) # 불필요한 컬럼 : enrollee_id

x_train = x_train.drop(columns=['enrollee_id'])
y_train = y_train.drop(columns=['enrollee_id'])
x_test_index = x_test.pop('enrollee_id')


# 결측치 확인 
# print(x_train.isnull().sum()) 
# 결측치가 있는 컬럼 : /enrolled_university / education_level/ major_discipline/major_discipline/experience //last_new_job
# 삭제 해야할 컬럼 : gender, company_size, company_type
# print(y_train.isnull().sum()) # 결측치 없음 
# print(x_test.isnull().sum()) # train과 마찬가지 


# 결측치 너무 많은 컬럼 제거 
x_train = x_train.drop(columns=['gender', 'company_size', 'company_type'])
x_test = x_test.drop(columns=['gender', 'company_size', 'company_type'])


# 결측치 채우기 
x_train['enrolled_university'] = x_train['enrolled_university'].fillna(x_train['enrolled_university'].mode().values[0])
x_train['education_level'] = x_train['education_level'].fillna(x_train['education_level'].mode().values[0])
x_train['major_discipline'] = x_train['major_discipline'].fillna(x_train['major_discipline'].mode().values[0])
x_train['experience'] = x_train['experience'].fillna(x_train['experience'].mode().values[0])
x_train['last_new_job'] = x_train['last_new_job'].fillna(x_train['last_new_job'].mode().values[0])


x_test['enrolled_university'] = x_test['enrolled_university'].fillna(x_test['enrolled_university'].mode().values[0])
x_test['education_level'] = x_test['education_level'].fillna(x_test['education_level'].mode().values[0])
x_test['major_discipline'] = x_test['major_discipline'].fillna(x_test['major_discipline'].mode().values[0])
x_test['experience'] = x_test['experience'].fillna(x_test['experience'].mode().values[0])
x_test['last_new_job'] = x_test['last_new_job'].fillna(x_test['last_new_job'].mode().values[0])

# print(x_train.isnull().sum())
# print(x_test.isnull().sum())

## 3단계 인코딩 / 스케일링 
# 인코딩
# 1. 라벨인코딩 city/experience/
# 2. 원핫인코딩 relevent_experience /education_level/enrolled_university/major_discipline/last_new_job


# print(x_train['last_new_job'].value_counts()) # 일일히 확인하기 


# 1. 라벨인코딩 
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

x_train['city'] = encoder.fit_transform(x_train['city'])
x_test['city'] = encoder.fit_transform(x_test['city'])

x_train['experience'] = encoder.fit_transform(x_train['experience'])
x_test['experience'] = encoder.fit_transform(x_test['experience'])

# 2. 원핫인코딩

col = ['relevent_experience','enrolled_university', 'education_level',
       'major_discipline','last_new_job']

x_train = pd.get_dummies(data=x_train, columns=col)
x_test = pd.get_dummies(data=x_test, columns=col)
x_test = x_test[x_train.columns]



# 스케일링 
# 수치형데이터 스케일링 'city_development_index'
# print(x_train.describe()) # training_hours 만 필요해보임 

from sklearn.preprocessing import RobustScaler

# scale = RobustScaler()
# x_train['training_hours'] = scale.fit_transform(x_train['training_hours'])
# x_test['training_hours'] = scale.fit_transform(x_test['training_hours'])


# ## 5단계 train val 

# from sklearn.model_selection import train_test_split
# X_train, X_val, Y_train, Y_val = train_test_split(x_train, y_train, test_size=0.2)

# # print(X_train.shape)
# # print(Y_train.shape)

# ## 5단계 모델 학습하기 

# from sklearn.ensemble import RandomForestClassifier
# model = RandomForestClassifier()

# model.fit(X_train, Y_train)

# model_pred = model.predict(X_val)



# ## 모델평가 

# from sklearn.metrics import accuracy_score
# print(accuracy_score(Y_val , model_pred))


# >> 나누고 학습하는건 파라미터 조정을 위함일 뿐이다! > 모두 주석처리해주고 답을위한 학습만 진행해야함 


from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()

model.fit(x_train, y_train)

model_pred = model.predict(x_test)

pd.DataFrame({"enrollee_id": x_test_index, "target": model_pred}).to_csv('./result_02.csv',index=False)
