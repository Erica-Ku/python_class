import pandas as pd
df = pd.read_csv('일별평균대기오염도_2022.csv', encoding="cp949")

print(df.info())
print(df.columns)

name_age_col = df.iloc[:, [0, 1]]
print(name_age_col)

sub_df = df.loc[df['미세먼지농도(㎍/㎥)'] >= 30]
print(sub_df)

sub_df = df.loc[(df['미세먼지농도(㎍/㎥)'] >= 30) & (df['초미세먼지농도(㎍/㎥)'] > 15)]
print(sub_df)

sub_df = df.loc[(df['미세먼지농도(㎍/㎥)'] >= 30)].loc[:,['측정일시', '측정소명', '미세먼지농도(㎍/㎥)']]
print(sub_df)