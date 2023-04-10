from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 웹 크롤링
## 웹 파싱 - 데이터 수집
response = urlopen("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blNH&qvt=0&query=%ED%95%9C%EA"
                   "%B5%AD%20%EC%8B%A4%EC%97%85%EB%A5%A0")
soup = BeautifulSoup(response, "html.parser")
value = soup.find_all("span", {"class": "text"})

## 날짜 추출 - 데이터 전처리
result1 = []
for i in value:
    if value.index(i) % 3 == 0:
        result1.append(i)
result2 = []
for j in result1:
    st1 = j.text.strip()
    st2 = st1[0:7]
    result2.append(st2)
result2.remove("2023.04")

## 실업률 추출 - 데이터 전처리
result3 = []
for i in value:
    if value.index(i) % 3 == 1:
        result3.append(i)
result4 = []
for j in result3:
    st3 = j.text.strip()
    st4 = st3[0:4]
    result4.append(st4)
result4.remove("-")

# pandas 사용
data = {"Date": result2, "Unemployment_rate": result4}
df1 = pd.DataFrame(data)
df1.to_csv("한국 실업률.csv", index=False)
df2 = pd.read_csv("한국 실업률.csv")
print(df2.head(5))

# matplotlib 사용 - 데이터 시각화
plt.plot(df2["Date"], df2["Unemployment_rate"])
plt.xlabel("Date")
plt.ylabel("Unemployment_rate")
plt.title("Unemployment Rate in Korea")
plt.show()