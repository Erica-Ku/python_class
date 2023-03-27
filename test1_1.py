import pandas as pd

# 데이터 파일 경로
data_path = '일별평균대기오염도_2022.csv'

# CSV 파일 읽기
df = pd.read_csv(data_path, encoding="cp949")

# 필요한 필드 추출
df = df[['측정일시', '측정소명', '미세먼지농도(㎍/㎥)', '초미세먼지농도(㎍/㎥)']]

# 결측치 처리
df = df.dropna()

# 측정일시 컬럼의 데이터 타입을 datetime으로 변경
df['측정일시'] = pd.to_datetime(df['측정일시'], format='%Y%m%d')

print(df.head(20))

import matplotlib.pyplot as plt

# 연도별 미세먼지와 초미세먼지 농도 평균 계산
df_monthly = df.resample('M', on='측정일시').mean(numeric_only=True)

# 그래프 그리기
plt.plot(df_monthly.index.month, df_monthly['미세먼지농도(㎍/㎥)'], label='PM10')
plt.plot(df_monthly.index.month, df_monthly['초미세먼지농도(㎍/㎥)'], label='PM2.5')
plt.legend()
plt.xlabel('Month')
plt.ylabel('Concentration')
plt.title('2022 Air Pollution Trend')
plt.show()

# 일별 합계 계산
df_daily = df.resample('D', on='측정일시').sum(numeric_only=True)

# 일평균 대기오염도 계산
df_daily['미세먼지농도(㎍/㎥)'] /= 24
df_daily['초미세먼지농도(㎍/㎥)'] /= 24

# 그래프 그리기
plt.plot(df_daily.index, df_daily['미세먼지농도(㎍/㎥)'], label='PM10')
plt.plot(df_daily.index, df_daily['초미세먼지농도(㎍/㎥)'], label='PM2.5')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Concentration')
plt.title('2022 Air Pollution Trend')
plt.show()

# 지역별 미세먼지와 초미세먼지 농도 평균 계산
df_area = df.groupby('측정소명').mean(numeric_only=True).head(10)

# 그래프 그리기
plt.bar(df_area.index, df_area['미세먼지농도(㎍/㎥)'], label='PM10')
plt.bar(df_area.index, df_area['초미세먼지농도(㎍/㎥)'], label='PM2.5')
plt.legend()
plt.xlabel('Area')
plt.ylabel('Concentration')
plt.title('Air Pollution by Area')
plt.show()

# 그래프 그리기
plt.boxplot([df['미세먼지농도(㎍/㎥)'], df['초미세먼지농도(㎍/㎥)']])
plt.xticks([1,2],['PM10', 'PM2.5'])
plt.ylabel('Concentration')
plt.title('Air Pollution Boxplot')
plt.show()

# 이상치를 모아서 result.csv 파일로 저장
q1 = df['미세먼지농도(㎍/㎥)'].quantile(0.25)
q3 = df['미세먼지농도(㎍/㎥)'].quantile(0.75)
iqr = q3 - q1
outlier_df = df[(df['미세먼지농도(㎍/㎥)'] < q1 - 1.5 * iqr) | (df['미세먼지농도(㎍/㎥)'] > q3 + 1.5 * iqr)]
outlier_df.to_csv('result.csv', index=False, encoding='utf-8-sig')
