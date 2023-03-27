import numpy as np

# 1차원 배열 생성
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)  # [1 2 3 4 5]

# 2차원 배열 생성
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2)

# 배열 데이터 타입 지정
arr3 = np.array([1, 2, 3], dtype=float)
print(arr3)  # [1. 2. 3.]

# 다차원 배열의 인덱싱
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0, 0])  # 1
print(arr2d[1, 1])  # 5

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6, 7])

# 브로드캐스팅을 통해 크기가 다른 배열 간 연산이 가능
print(arr1 + arr2)  # [ 5  7  9  10]

# 정규 분포
arr1 = np.random.normal(0, 1, size=10)
print(arr1)

# 균등 분포
arr2 = np.random.uniform(0, 1, size=10)
print(arr2)

# 이항 분포
arr3 = np.random.binomial(10, 0.5, size=10)
print(arr3)

# 포아송 분포
arr4 = np.random.poisson(3, size=10)
print(arr4)


import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 데이터프레임 정보 출력
print(df.head())            # 상위 5개 데이터 출력
print(df.tail())            # 하위 5개 데이터 출력
print(df.info())            # 데이터프레임 정보 출력
print(df.describe())        # 수치형 열의 기술 통계 정보 출력
print(df.columns)           # 열 이름 출력
print(df.index)             # 행 인덱스 출력
print(df.dtypes)            # 열의 데이터 타입 출력
print(df.shape)             # 데이터프레임의 크기 출력
print(df.isnull().sum())    # 결측치 개수 출력

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 열 선택 방법 1: 대괄호([])를 이용한 단일 열 선택
name_col = df['name']
print(name_col)

# 열 선택 방법 2: 점(.)을 이용한 단일 열 선택
age_col = df.age
print(age_col)

# 열 선택 방법 3: 대괄호([])를 이용한 복수 열 선택
name_age_col = df[['name', 'age']]
print(name_age_col)

# 열 선택 방법 4: loc[]를 이용한 열 선택
name_col = df.loc[:, 'name']
print(name_col)

# 열 선택 방법 5: iloc[]를 이용한 열 선택
name_age_col = df.iloc[:, [0, 1]]
print(name_age_col)

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 행 선택 방법 1: 대괄호([])를 이용한 단일 행 선택
row_0 = df.iloc[0]
print(row_0)

# 행 선택 방법 2: loc[]를 이용한 단일 행 선택
row_1 = df.loc[1]
print(row_1)

# 행 선택 방법 3: iloc[]를 이용한 복수 행 선택
rows_1_3 = df.iloc[[1, 3]]
print(rows_1_3)

# 행 선택 방법 4: loc[]를 이용한 복수 행 선택
rows_2_4 = df.loc[[2, 4]]
print(rows_2_4)

sub_df = df.loc[df['age'] >= 30]
print(sub_df)

# 행 선택 방법 5: 슬라이싱을 이용한 범위 지정
rows_1_3 = df[1:4]
print(rows_1_3)

# 행 선택 방법 6: query()를 이용한 조건에 따른 행 선택
rows_age_over_30 = df.query('age > 30')
print(rows_age_over_30)

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 부분 데이터 선택 방법 1: loc[]를 이용한 조건에 따른 선택
sub_df_1 = df.loc[df['age'] > 30, ['name', 'city']]
print(sub_df_1)

# 부분 데이터 선택 방법 2: query()를 이용한 조건에 따른 선택
sub_df_2 = df.query('age > 30')[['name', 'city']]
print(sub_df_2)

# 부분 데이터 선택 방법 3: 슬라이싱을 이용한 범위 지정
sub_df_3 = df.iloc[1:3, 1:3]
print(sub_df_3)

# 부분 데이터 선택 방법 4: iloc[]를 이용한 인덱스 지정
sub_df_4 = df.iloc[[1, 3], [0, 2]]
print(sub_df_4)

# 부분 데이터 선택 방법 5: 조건에 따른 선택 후 열 지정
sub_df_5 = df[df['age'] > 30][['name', 'city']]
print(sub_df_5)

# 부분 데이터 선택 방법 6: at[]을 이용한 특정 위치 선택
val = df.at[1, 'age']
print(val)

# 데이터 전처리
# 예제 데이터
data = {'A': [1, np.nan, 3], 'B': [4, 5, np.nan], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# 결측치 확인
print(df.isnull())
# 결과:
#        A      B      C
# 0  False  False  False
# 1   True  False  False
# 2  False   True  False

# 결측치 대체
filled_df = df.fillna(0)
print(filled_df)
# 결과:
#      A    B  C
# 0  1.0  4.0  7
# 1  0.0  5.0  8
# 2  3.0  0.0  9

# 결측치 제거
dropped_df = df.dropna()
print(dropped_df)
# 결과:
#      A    B  C
# 0  1.0  4.0  7

# 예제 데이터
data = {'A': [1, 2, 2], 'B': [4, 5, 5], 'C': [7, 8, 8]}
df = pd.DataFrame(data)

# 중복 확인
print(df.duplicated())
# 결과:
# 0    False
# 1    False
# 2     True

# 중복 제거
deduplicated_df = df.drop_duplicates()
print(deduplicated_df)
# 결과:
#    A  B  C
# 0  1  4  7
# 1  2  5  8

# 데이터프레임 생성
data = {'int_col': [1, 2, 3, 4, 5],
        'float_col': [1.1, 2.2, 3.3, 4.4, 5.5],
        'str_col': ['1', '2', '3', '4', '5'],
        'bool_col': [True, False, True, False, True],
        'category_col': ['a', 'b', 'c', 'a', 'b'],
        'date_col': ['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01']}

df = pd.DataFrame(data)

# 열 데이터 형 변환
df['int_col'] = df['int_col'].astype(float)  # 정수형 -> 실수형
df['float_col'] = df['float_col'].astype(int)  # 실수형 -> 정수형
df['str_col'] = df['str_col'].astype(bool)  # 문자열 -> 불리언형
df['bool_col'] = df['bool_col'].astype(str)  # 불리언형 -> 문자열형
df['category_col'] = df['category_col'].astype('category')  # 문자열 -> 범주형
df['date_col'] = pd.to_datetime(df['date_col'])  # 문자열 -> 날짜/시간형

# 데이터프레임 정보 출력
print(df.dtypes)

# 데이터프레임 생성
data = {'gender': ['Male', 'Female', 'Male', 'Male', 'Female'],
        'age': [20, 30, 25, 35, 27],
        'city': ['Seoul', 'Busan', 'Seoul', 'Incheon', 'Seoul']}

df = pd.DataFrame(data)

# gender 열을 category 형으로 변환
df['gender'] = df['gender'].astype('category')

# city 열을 category 형으로 변환
df['city'] = df['city'].astype('category')

# 카테고리별 데이터 개수 확인
print(df['gender'].value_counts())
print(df['city'].value_counts())

# 카테고리별 통계량 확인
print(df.groupby('gender').mean(numeric_only=True))
print(df.groupby('city').mean(numeric_only=True))

# 샘플 데이터 생성
data = {
    'text': ['Hello, World!', 'Pandas is great', 'Python is awesome']
}
df = pd.DataFrame(data)

# 문자열 처리 작업
df['lower'] = df['text'].str.lower()  # 모든 문자를 소문자로 변환
df['words'] = df['text'].str.split()  # 공백을 기준으로 단어 분할
df['no_punctuation'] = df['text'].str.replace('[^\w\s]', '', regex=True)  # 구두점, 기호 제거
df['word_count'] = df['text'].str.split().str.len()  # 단어 개수 계산

print(df.iloc[:, 1:])

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 열 추가 방법 1: 기존 열을 이용하여 새로운 열 추가
df['age2'] = df['age'] + 1

# 열 추가 방법 2: insert() 메소드를 이용하여 특정 위치에 열 추가
df.insert(loc=2, column='gender', value=['F', 'M', 'M', 'M', 'F'])

# 열 추가 방법 3: assign() 메소드를 이용하여 여러 개의 열 한 번에 추가
df = df.assign(age3=[26, 31, 36, 41, 46], height=[160, 170, 180, 175, 165])

# 출력
print(df)

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 행 추가 방법 1: append() 메소드를 이용하여 단일 행 추가
new_row = {'name': 'Frank', 'age': 50, 'city': 'Seoul'}
df = df.append(new_row, ignore_index=True)

# 행 추가 방법 2: append() 메소드를 이용하여 여러 행 추가
new_rows = [{'name': 'George', 'age': 22, 'city': 'Toronto'},
            {'name': 'Helen', 'age': 27, 'city': 'Sydney'}]
df = df.append(new_rows, ignore_index=True)

# 출력
print(df)

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 행 삭제 방법 1: drop() 메소드를 이용하여 단일 행 삭제
df = df.drop(0)

# 행 삭제 방법 2: drop() 메소드를 이용하여 여러 행 삭제
df = df.drop([1, 2])

# 열 삭제 방법 1: drop() 메소드를 이용하여 단일 열 삭제
df = df.drop('age', axis=1)

# 열 삭제 방법 2: drop() 메소드를 이용하여 여러 열 삭제
df = df.drop(['name', 'city'], axis=1)

# 출력
print(df)

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 행 재정렬 방법 1: loc[]을 이용하여 행 순서 변경
df = df.loc[[4, 3, 2, 1, 0]]

# 행 재정렬 방법 2: sort_values() 메소드를 이용하여 열 기준으로 정렬
df = df.sort_values('age', ascending=False)

# 열 재정렬 방법 1: 열 이름 순서 변경
df = df[['city', 'name', 'age']]

# 열 재정렬 방법 2: 열 이름을 알파벳 순서로 정렬
df = df.reindex(sorted(df.columns), axis=1)

# 출력
print(df)

# concat
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']})

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']})

result = pd.concat([df1, df2], axis=0, ignore_index=True)

print(result)

# merge
left = pd.DataFrame({'key': ['K0', 'K1', 'K3'],
                     'A': ['A0', 'A1', 'A3'],
                     'B': ['B0', 'B1', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K2', 'K3'],
                      'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']})

result = pd.merge(left, right, on='key')

print(result)

# 예시 데이터
left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']},
                     index=['K0', 'K1', 'K2', 'K3'])
right = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']},
                      index=['K0', 'K1', 'K2', 'K3'])

# 인덱스를 기준으로 병합
result = left.join(right)

print(result)

# 데이터 그룹화
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank'],
        'gender': ['F', 'M', 'M', 'M', 'F', 'M'],
        'age': [25, 30, 35, 40, 45, 50],
        'score1': [80, 70, 85, 75, 90, 95],
        'score2': [85, 75, 90, 80, 95, 100]}

df = pd.DataFrame(data)

# count
print(df.groupby('gender')[['score1', 'score2']].count())

# size
print(df.groupby('gender')[['score1', 'score2']].size())

# sum
print(df.groupby('gender')[['score1', 'score2']].sum())

# mean
print(df.groupby('gender')[['score1', 'score2']].mean())

# median
print(df.groupby('gender')[['score1', 'score2']].median())

# min
print(df.groupby('gender')[['score1', 'score2']].min())

# max
print(df.groupby('gender')[['score1', 'score2']].max())

# std
print(df.groupby('gender')[['score1', 'score2']].std())

# var
print(df.groupby('gender')[['score1', 'score2']].var())

# sem
print(df.groupby('gender')[['score1', 'score2']].sem())

# describe
print(df.groupby('gender')[['score1', 'score2']].describe())

# 고객 데이터 생성
data = {'Region': ['East', 'East', 'West', 'West', 'North', 'North', 'South', 'South'], 
        'Age': [20, 30, 40, 50, 30, 40, 50, 60],
        'Sales': [100, 150, 200, 250, 300, 350, 400, 450]}
df = pd.DataFrame(data)

# 피벗테이블 생성
result = pd.pivot_table(df, index='Region', columns=pd.cut(df['Age'], [10, 30, 50, 70]), values='Sales', aggfunc='mean')

print(result)

#데이터 전처리
data = {'date': ['2021-08-15', '2021-08-16', '2021-08-17'],
        'value': [100, 200, 150]}
df = pd.DataFrame(data)

df['date'] = pd.to_datetime(df['date'])
print(df)
# Output:
#         date  value
# 0 2021-08-15    100
# 1 2021-08-16    200
# 2 2021-08-17    150

# 날짜 데이터 생성
df = pd.DataFrame({'date': ['2022년 01월 01일', '2022년 01월 02일', '2022년 01월 03일']})

# 날짜 데이터를 datetime 형식으로 변환
df['date'] = pd.to_datetime(df['date'], format='%Y년 %m월 %d일')

# 년, 월, 일 컬럼 추출
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

print(df)

data = {'date': ['2022-01-01', '2022-01-02', '2022-01-01', '2022-01-02', '2022-01-01', '2022-01-02'],
        'location': ['서울', '서울', '부산', '부산', '대구', '대구'],
        'PM10': [50, 40, 45, 55, 60, 65],
        'PM2.5': [25, 20, 22, 28, 30, 35]}
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])

df_monthly = df.groupby('location').resample('D', on='date').mean(numeric_only=True)
print(df_monthly)