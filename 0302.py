# 사용자로부터 숫자를 입력받아, 홀수인지 짝수인지 판별하기
num = int(input("숫자를 입력하세요: "))
if num % 2 == 0:
    print(f"{num}은(는) 짝수입니다.")
else:
    print(f"{num}은(는) 홀수입니다.")

# if-else if
num = int(input("숫자를 입력하세요: "))
if num > 0:
    print("양수입니다")
elif num < 0:
    print("음수입니다")
else:
    print("0입니다")

# 사용자로부터 성적을 입력받아, 학점 부여하기
score = int(input("성적을 입력하세요: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"당신의 학점은 {grade}입니다.")

# 한 문장의 if-else
num = 10
result = "10보다 큽니다" if num > 10 else "10보다 작거나 같습니다"
print(result)

score = int(input("성적을 입력하세요: "))
grade = "A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else ("D" if score >= 60 else "F")))
print(grade)

string = input("문자열을 입력하세요: ")
length = len(string) if string else 0
print("문자열의 길이는", length, "입니다.")

import math
num = float(input("양수를 입력하세요: "))
result = math.sqrt(num) if num > 0 else "잘못된 입력입니다."
print("결과: ", result)

# 성적 계산기 작성
kscore = float(input("국어 성적을 입력하세요: "))
escore = float(input("영어 성적을 입력하세요: "))
mscore = float(input("수학 성적을 입력하세요: "))
print(f"각 과목의 평균 점수: {kscore:.2f}점, {escore:.2f}점, {mscore:.2f}점")
avg = ((kscore*0.4)+(escore*0.4)+(mscore*0.2))
print(f"총 평균 점수: {avg:.2f}")
if avg>=90:
    result="A"
elif avg>=80:
    result="B"
elif avg>=70:
    result="C"
elif avg>=60:
    result="D"
else:
    result="F"
print(f"학점: {result}")

# if 문제
num = float(input("길이를 입력하세요: "))
if num<0:
    print("잘못 입력하였습니다.")
else:
    print(num*2.54)

num = int(input("학점을 입력하세요: "))
if num<40:
    print("1학년입니다.")
elif 40<=num<80:
    print("2학년입니다.")
elif 80<=num:
    print("졸업반입니다.")
else:
    print("")

num = int(input("현재 시간: "))
num1 = int(input("am (1) or pm (2): "))
num2 = int(input("How many hours ahead? "))
if num1==1:
    if num+num2<12:
        print(f"New hour: {num+num2}am")
    elif num+num2==12:
        print(f"New hour: {num+num2}pm")
    else:
        print(f"New hour: {(num+num2)-12}pm")
if num1==2:
    if num+num2<12:
        print(f"New hour: {num+num2}pm")
    else:
        print(f"New hour: {(num+num2)-12}am")

# while
num = int(input("10진수를 입력하세요: "))
binary = ""
while num > 0:
    remainder = num % 2
    binary = str(remainder) + binary
    num = num // 2
print("입력한 수의 2진수 표현: ", binary)

# for
for i in range(10, 0, -1): # 10~1까지 거꾸로 출력
    print(i)
for i in range(2, 10): # 구구단 출력
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")
for i in range(4, 0, -1):
    for j in range(1, i+1):
        print("*", end="") # print는 기본적으로 출력 후 줄바꿈
    print()

# 3의 배수와 5의 배수의 합 구하기
n = int(input("양의 정수 n을 입력하세요: "))
sum = 0
for i in range(1, n+1):
    if i%3==0 or i%5==0:
        sum += i
print(f"1부터 {n}까지의 자연수 중에서 3의 배수와 5의 배수의 합: {sum}")

# 최댓값과 최솟값 찾기
n1 = int(input("1번째 숫자를 입력하세요: "))
n2 = int(input("2번째 숫자를 입력하세요: "))
n3 = int(input("3번째 숫자를 입력하세요: "))
n4 = int(input("4번째 숫자를 입력하세요: "))
n5 = int(input("5번째 숫자를 입력하세요: "))
nums = [n1, n2, n3, n4, n5]
a = max(nums)
b = min(nums)
print(f"최댓값: {a}")
print(f"최솟값: {b}")

# 숫자의 합이 100보다 작을 때까지 입력받기
sum = 0
while sum < 100:
    num = int(input("숫자를 입력하세요: "))
    sum += num
print(f"입력받은 숫자들의 합: {sum}")

# 피보나치 수열의 n번째 항을 출력하는 프로그램
num = int(input("몇 번째 항을 출력할까요? : "))
if num==1 or num==2:
    result = 1
else:
    a, b = 1, 1
    i = 3
    while i <= num:
        result = a+b
        a = b
        b = result
        i += 1
print(f"피보나치 수열의 {num}번째 항은 {result}입니다.")

def fibonacci(n): #재귀함수 사용 버젼
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
n = int(input("몇 번째 항을 출력할까요? "))
print("피보나치 수열의", n, "번째 항은", fibonacci(n), "입니다.")

# 주사위 게임
import random
while True:
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    sum = num1+num2
    print(f"주사위1: {num1}, 주사위2: {num2}, 합: {sum}")
    if sum==7:
        print("이겼습니다.")
        break
    else:
        print("다시 던집니다.")

# 계산기 프로그램
while True:
    num1 = input("첫 번째 숫자를 입력하세요: ")
    if num1 == "exit":
        break
    num2 = input("두 번째 숫자를 입력하세요: ")
    if num2 == "exit":
        break
    operator = input("연산자를 입력하세요 (+, -, *, /): ")
    if operator == "exit":
        break
    num1 = float(num1)
    num2 = float(num2)
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("0으로 나눌 수 없습니다.")
            continue
        else:
            result = num1 / num2
    else:
        print("잘못된 연산자입니다.")
        continue
    print(f"{num1} {operator} {num2} = {result}")
    
# 게임 프로그램 작성
import random

money = 50
while money > 0 and money < 100:
    print("현재 잔액: ", money)
    guess = random.randint(1, 2)
    # guess = int(input("동전 던지기! 앞면(1) 또는 뒷면(2)을 맞춰보세요: "))
    result = random.randint(1, 2)
    if guess == result:
        print("맞췄습니다!")
        money += 9
    else:
        print("틀렸습니다.")
        money -= 10
if money <= 0:
    print("돈을 모두 잃으셨습니다. 게임 오버!")
else:
    print("축하합니다! $100을 모으셨습니다. 게임 클리어!")
    
# 두 수의 최대 공약수
n1 = int(input("첫번째 수를 입력하세요: "))
n2 = int(input("두번째 수를 입력하세요: "))
if n1>n2:
    maxn = n1
    minn = n2
else:
    maxn = n2
    minn = n1
rem = 1
while rem!=0:
    rem = maxn % minn
    maxn = minn
    minn = rem
print("최대공약수는", maxn, "입니다.")