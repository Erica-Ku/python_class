'''# 문자열에서 홀수 번째 문자 추출하기
string = "abcdefghij"
result = ""
for i in range(len(string)):
    if i % 2 == 0:
        result += string[i]
print(result)  # 출력값: "acegi"

# 문자열 슬라이싱 - 문자열을 뒤집는 예제
s = "Hello, world!"
reversed_s = s[::-1]
print(reversed_s)  # "!dlrow ,olleH"

# 문자열 구성 파악 메소드 예시
print("hello123".isalnum())  # True
print("123".isalpha())  # False
print("123".isdecimal())  # True
print("123".isdigit())  # True
print("hello".isidentifier())  # True
print("hello".islower())  # True
print("123".isnumeric())  # True
print("Hello, World!".isprintable())  # True
print("   ".isspace())  # True
print("\t".isspace())  # True
print("Hello, World!".istitle())  # True
print("HELLO".isupper())  # True

# 문자열 대소문자 변환 함수 예시
print("hello, world!".upper())  # "HELLO, WORLD!"
print("HeLLo, wOrLd!".lower())  # "hello, world!"
print("hello, world!".capitalize())  # "Hello, world!"
print("hello, world!".title())  # "Hello, World!"
print("Hello, World!".swapcase())  # "hELLO, wORLD!"

# 문자열 찾기 함수 예시
s = "hello, world!"
print(s.find("o"))  # 4
print(s.rfind("o"))  # 8
print(s.index("o"))  # 4
print(s.rindex("o"))  # 8
print(s.count("o"))  # 2

# 문자열 공백 삭제 및 변경 함수 예시
s = "  hello,   world!  "
print(s.strip())  # "hello,   world!"
print(s.lstrip())  # "hello,   world!  "
print(s.rstrip())  # "  hello,   world!"
print(s.replace("o", "0"))  # "  hell0,   w0rld!  "
print(s.replace("o", "0", 1))  # "  hell0,   world!  "

# 문자열 분리, 결합 함수
string = "apple,banana,grape"
string_list = string.split(",")  # 쉼표를 구분자로 사용
print(string_list)  # ['apple', 'banana', 'grape']

print("apple\nbanana\rgrape".splitlines())  # ["apple", "banana", "grape"]
print(",".join(["apple", "banana", "grape"]))  # "apple,banana,grape"

# 문자열 정렬, 채우기 함수 예시
s = "hello"
print(s.center(10))  # "  hello   "
print(s.center(10, "-"))  # "--hello---"
print(s.ljust(10))  # "hello     "
print(s.ljust(10, "*"))  # "hello*****"
print(s.rjust(10))  # "     hello"
print(s.rjust(10, "+"))  # "+++++hello"
print("123".zfill(5))  # "00123"

# 연습문제
s = input("문자열을 입력하세요: ")
print(len(s))
print(s*10)
print(s[0])
print(s[:3])
print(s[-3:])
print(s[::-1])
if len(s) >= 7:
    print(s[6])
else:
    print("문자가 없습니다.")
print(s[1:-1])
print(s.upper())
print(s.lower())
print(s.replace("a","e"))

# a 문자열 프로그램
word = input("단어를 입력하세요: ")
a = word.find('a')
if a!=-1:
    print(word[:a+1])
    print(word[a+1:])
else:
    print(word)

print(word.replace('a','a\n')) # a가 여러 개인 경우

# 1~1000까지 숫자의 각 자리수의 합 구하기
total_sum = 0
for num in range(1, 1001):
    sum = 0
    for s in str(num):
        sum += int(s)
    total_sum += sum
print(total_sum)

# 리스트 컴프리헨션
even_numbers = [num for num in range(1, 11) if num % 2 == 0]
print(even_numbers)  # 출력: [2, 4, 6, 8, 10]

words = ["apple", "banana", "orange", "grape", "watermelon"]
result = [word.upper() for word in words if len(word) > 5]
print(result)  # ['BANANA', 'ORANGE', 'WATERMELON']

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [num for row in matrix for num in row if num % 2 == 0]
print(result)  # [2, 4, 6, 8]

# 리스트 인덱싱
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])  # [1, 2, 3] 출력
print(matrix[1])  # [4, 5, 6] 출력
print(matrix[2])  # [7, 8, 9] 출력
print(matrix[0][1])  # 2 출력
print(matrix[1][2])  # 6 출력

# 리스트 합치기
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
list3 = list1
print(list3) # 출력 결과: [1, 2, 3, 4, 5, 6]

# 리스트 요소, 수정, 추가, 제거하기
my_list = [1, 2, 3, 4]
my_list[2] = 5
print(my_list) # 출력 결과: [1, 2, 5, 4]

my_list = [1, 2, 3, 4]
my_list[1:3] = [5, 6]
print(my_list) # 출력 결과: [1, 5, 6, 4]

my_list = [1, 2, 3, 4]
my_list.append(5)
print(my_list) # 출력 결과: [1, 2, 3, 4, 5]

my_list = [1, 2, 3, 4]
my_list.insert(2, 5)
print(my_list) # 출력 결과: [1, 2, 5, 3, 4]

my_list = [1, 2, 3, 4, 5]
my_list[1:4] = []
print(my_list) # 출력 결과: [1, 5]

my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list) # 출력 결과: [1, 2, 4]

my_list = [1, 2, 3, 4]
my_list.remove(3)
print(my_list) # 출력 결과: [1, 2, 4]

my_list = [1, 2, 3, 4, 5]
removed_item = my_list.pop(2)
print(my_list) # 출력 결과: [1, 2, 4, 5]
print(removed_item) # 출력 결과: 3

my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list) # 출력 결과: []

# 내장 함수를 이용해서 리스트 다루기
nums = [1, 2, 3, 4, 5]
total = sum(nums)
print(total)  # 15

nums = [1, 2, 3, 4, 5]
max_num = max(nums)
min_num = min(nums)
print(max_num)  # 5
print(min_num)  # 1

nums = [3, 5, 1, 4, 2]
sorted_nums = sorted(nums)  # 정렬된 새로운 리스트 반환
print(sorted_nums)  # [1, 2, 3, 4, 5]

nums = [1, 2, 3, 4, 5]
reversed_nums = list(reversed(nums))  # 뒤집힌 새로운 리스트 반환
print(reversed_nums)  # [5, 4, 3, 2, 1]

a = [3, 2, 1]
a.sort()  # 원본 리스트 변경
print(a)  # 출력: [1, 2, 3]

a = [1, 2, 3]
a.reverse()  # 원본 리스트 변경
print(a)  # 출력: [3, 2, 1]

# 연습문제
friends = ["민지", "가혜", "수현", "나연"]
friends.insert(0, "준영")
print(friends)
friends.insert(2, "수지")
print(friends)
friends.append("아람")
print(friends)

mylist = [1,2,3]
mylist[1] = 17
print(mylist)
mylist1 = [4,5,6]
mylist.extend(mylist1)
print(mylist)
del mylist[0]
print(mylist)
mylist.sort()
print(mylist)
mylist.insert(3, 25)
print(mylist)

# for 루프를 이용하여 다음과 같은 리스트를 만들어라
## 0~49까지의 수로 구성되는 리스트
mylist = [num for num in range(0, 50)]
print(mylist)

mylist = []
for i in range(0,50):
    mylist.append(i)
print(mylist)

## 1~50까지 수의 제곱으로 구성되는 리스트
mylist = [num**2 for num in range(1, 51)]
print(mylist)

mylist = []
for i in range(1,51):
    mylist.append(i**2)
print(mylist)

# 두 리스트의 각 요소 합으로 구성되는 새로운 리스트를 생성하기
L = [1,2,3]
M = [4,5,6]
N = [a + b for a, b in zip(L, M)]
print(N)

L = [1,2,3]
M = [4,5,6]
N = []
for i in range(0, len(L)):
    N.append(L[i]+M[i])
print(N)

# 사용자로부터 5개의 숫자를 문자열로 입력 받아 각 숫자를 +로 연결한 문자열 생성
nums = []
for i in range(5):
    num = input("숫자를 입력하세요: ")
    nums.append(num)
result = "+".join(nums)
print(result)

nums = input("숫자를 입력하세요(구분자: 띄어쓰기): ").split()
result = "+".join(nums)
print(result)'''

# 튜플 언패킹
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # 1
print(b)  # 2
print(c)  # 3

x = 1
y = 2
x, y = y, x
print(x)  # 2
print(y)  # 1

# 튜플을 이용한 함수에서의 활용 예시
def calculate(x, y):
    add = x + y
    subtract = x - y
    multiply = x * y
    divide = x / y
    return add, subtract, multiply, divide
result = calculate(10, 2)
print(result)  # 결과: (12, 8, 20, 5.0)