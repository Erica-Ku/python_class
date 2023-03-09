# 연습문제
days = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}
month = input("월을 입력하세요: ")
print(days[month.title()])
days_key = list(days.keys())
print(sorted(days_key))
for x in days:
    if (days[x]==31):
        print(x)
days_item = days.items()
days_item = [(day, month) for (month, day) in days_item]
days_item.sort()
days_item = [(month, day) for (day, month) in days_item]
print(days_item)
mon = input("월을 입력하세요: ")
for x in days:
    if x[0:3]==mon.title():
        print(days[x])

d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'}, {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},{'name':'Princess', 'phone':'555-3141', 'email':''},{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]
for x in d:
    if x['phone'][7]=='8':
        print(x['name'])
for x in d:
    if x['email']=='':
        print(x['name'])
name = input("이름을 입력하세요: ")
flag = 1
for x in d:
    if x['name']==name.title():
        print(x['phone'], x['email'])
        flag = 0
if flag==1:
    print("이름이 없습니다.")

# set 예제
## 1부터 45까지의 수 중에서 6개를 선택하여 로또 번호를 만드는 프로그램
import random
s = set()
while len(s)<6:
    s.add(random.randint(1,45))
print(sorted(s))

# 학생들의 성적을 딕셔너리로 저장하고, 성적 평균을 계산하는 프로그램을 작성해보세요.
grades = {"Alice": [85, 90, 95], "Bob": [75, 80, 85], "Charlie": [95, 95, 95]}
print("Average grades:")
for name, grade_list in grades.items():
    avg = (sum(grade_list)/len(grade_list))
    print(name+":", avg)
    
# 숫자들이 들어있는 리스트에서 중복된 숫자를 제거하고, 남은 숫자들의 합을 계산하는 프로그램을 작성해보세요.
s = set([1, 2, 2, 3, 3, 3, 4, 4, 5])
print(sum(s))

# 주어진 문자열에서 각 알파벳의 빈도수를 구하는 프로그램을 작성하시오.
text = "Hello, world!"
d = {}
for x in text:
    d.setdefault(x, text.count(x))
print(d)

for x in text:
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1
print(d)

# 두 개의 리스트가 주어졌을 때, 두 리스트에 공통으로 포함된 요소를 모두 담은 리스트를 반환하는 프로그램을 작성하시오.
def find_common_elements(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2 and element not in common_elements:
            common_elements.append(element)
    return common_elements
list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8, 10]
common_elements = find_common_elements(list1, list2)
print(common_elements)

# 1~n까지의 합을 계산하는 함수
def sum_n(a, b):
    sum = 0
    for x in range(a, b+1):
        sum += x
    return sum
s = sum_n(1, 10)
print(s)

# 반지름을 전달하면 원의 면적을 반환하는 cir_area(r) 함수와 원의 둘레를 반환하는 cir_cirm(r) 함수를 작성하라.
# 이들 함수를 이용하여 반지름이 3.5cm인 원의 면적과 둘레를 소수점 아래 첫 자리까지 구하라.
def cir_area(r):
    return 3.14*r**2
def cir_cirm(r):
    return 2*3.14*r
print(round(cir_area(3.5),1))
print(round(cir_cirm(3.5),1))

# den(n) 함수를 이용하여 약수를 구하여 반환하는 프로그램을 작성
def den(n):
    cd = []
    for i in range(1, n+1):
        if n%i==0:
            cd.append(i)
    return cd
print(den(32))

# 두 개의 매개변수 n, m을 전달받아 m x n개의 * 상자를 출력하는 프로그램을 함수로 작성
def n_m(n, m):
    for x in range(n):
        for y in range(m):
            p = print("*",end='')
        p = print()
    return p
n_m(2,4)

# 하나의 숫자를 전달받아 숫자의 자리 합을 구하는 함수를 작성
def sum_n(n):
    sum = 0
    for x in str(n):
        sum += int(x)
    return print(sum)
sum_n(123)

# 두 개의 문자열이 서로 다른 처음 위치를 반환하는 함수를 작성. 두 개의 문자열이 같으면 -1을 반환
import math
def str_comp(str1, str2):
    flag = 0
    lengh = min(len(str1), len(str2))
    for i in range(lengh):
        if str1[i]!=str2[i]:
            if i!=0:
                return i
            else:
                return 0
    return -1
str1 = input("1번째 문자열: ")
str2 = input("2번째 문자열: ")
print(str_comp(str1, str2))

# 문자열과 하나의 문자를 전달받아 문자열에서 문자의 위치를 모두 찾아 리스트로 반환하는 함수를 작성
def find_char(s, c):
    indices = []
    for i in range(len(s)):
        if s[i]==c:
            indices.append(i)
    return indices
s = input("문자열: ")
c = input("문자: ")
print(find_char(s,c))

# 재귀 함수를 이용하여 1부터 100까지의 합을 계산하는 프로그램
def sum_n(n):
    if n==1:
        return 1
    else:
        return n + sum_n(n-1)
print(sum_n(100))