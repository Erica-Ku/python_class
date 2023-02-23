# 문자열 포매팅 - f-string
name = "Tom"
age = 20
print(f"My name is {name} and I am {age:d} years old.")

num1 = 3
num2 = 2
num3 = 1
print(f"I have {num1:d} apples, {num2:d} oranges, and {num3:d} banana.")

f1 = 1.23
print(f"The result is {f1:.2f}.")

per = 90
print(f"Your score is {per:d}%.")

num4 = 10
num5 = 20
num6 = 30
print(f"{num4:d} + {num5:d} = {num6:d}")

# 사과 쇼핑몰 프로그램
n1 = int(input("사과의 개수: "))
price = int(input("가격: "))
per1 = float(input("부가세율: "))
result = f'''
사과의 개수: {n1}
가격: {price}
부가세율: {per1}
결과: {(n1*price)+(n1*price*per1):.0f}'''
print(result)

# 초를 입력하면 분과 초로 표시하는 프로그램
sec = int(input("초를 입력하시오: "))
minute1 = int(sec//60)
minute2 = sec%60
result = f'''
초: {sec}
결과: {minute1}분 {minute2}초'''
print(result)

# 분을 입력하면 일, 시간, 분으로 출력하는 프로그램
min1 = int(input("분을 입력하시오: "))
h1 = int(min1//60)
h2 = (h1%24)
d1 = int(h1//24)
min2 = min1%60
result = f'''
분: {min1}
결과: {d1}일 {h2}시간 {min2}분'''
print(result)

# 원리금 합계 출력 프로그램
w=5000000
y=5
Sum = int(w*(1+0.05)**y)
print(f"원리금: {Sum}")

# 1~100 합계 출력 프로그램
n=100
sum1 = int(n*(n+1)//2)
print(f"합계: {sum1}")

# 포도, 딸기 총 무게 계산 프로그램
grape = int(input("포도의 개수: "))
stro = int(input("딸기의 개수: "))
gw = grape * 75
sw = stro * 113.5
result = f'''
포도의 개수: {grape}
딸기의 개수: {stro}
총 무게: {gw+sw}'''
print(result)