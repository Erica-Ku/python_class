# 연습문제
# enumerate() 내장 함수를 이용하여 사용자가 입력한 문자열에서 'a' 문자의 위치를 모두 찾아
# 출력하는 프로그램을 작성하라. 'a'가 없으면 "a가 없습니다'라는 메시지를 출력하라.
msg = input("message: ")
flag = 0
for i, ch in enumerate(msg):
    if ch=='a':
        print(i)
        flag=1
if flag==0:
    print("a가 없습니다.")

# 두 수의 합(sum), 차(sub), 곱(mul), 나누기(div)를 수행하는 함수를 각각 정의하라.
# 딕셔너리를 이용하여 사용자가 '1'을 입력하면 sum()을 호출하고, '2'를 입력하면
# sub(), '3'을 입력하면 mul(), '4'를 입력하면 div() 함수를 호출하여 두 수의 연산을 수행하는 프로그램을 작성하라.
def sum(n, m):
    return n+m
def sub(n, m):
    return n-m
def mul(n, m):
    return n*m
def div(n, m):
    return n/m
table = {'1':sum, '2':sub, '3':mul, '4':div}
a = input("1,2,3,4 중 입력: ")
func = table[a]
print(func(2, 3))

# 다음과 같이 구성되는 문자열을 구분 문자(&, =)로 분리하여 딕셔너리로 반환하는 함수 작성
query = 'led=on&motor=off&switch=off'
a = query.split('&')
# a = [a[0].split('='), a[1].split('='), a[2].split('=')]
temp = []
for item in a:
    temp.append(item.split('='))
print(dict(temp))

def query_parse(query):
    a = query.split('&')
    temp = []
    for item in a:
        temp.append(item.split('='))
    return dict(temp)
print(query_parse(query))

# 클래스
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# 인스턴스 생성
rectangle1 = Rectangle(3, 4)
rectangle2 = Rectangle(5, 6)

# 인스턴스 변수에 접근하여 값 출력
print(rectangle1.width) # 출력 결과: 3
print(rectangle1.height) # 출력 결과: 4
print(rectangle2.width) # 출력 결과: 5
print(rectangle2.height) # 출력 결과: 6

# 인스턴스 메서드 호출
print(rectangle1.area()) # 출력 결과: 12
print(rectangle2.area()) # 출력 결과: 30

# 클래스 변수
class Rectangle:
    count = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    def area(self):
        return self.width * self.height

# 클래스 변수 값을 출력
print(Rectangle.count) # 출력 결과: 0

# 인스턴스 생성 시 클래스 변수 값 증가
rectangle1 = Rectangle(3, 4)
print(Rectangle.count) # 출력 결과: 1

rectangle2 = Rectangle(5, 6)
print(Rectangle.count) # 출력 결과: 2

# 클래서 메서드
class Rectangle:
    count = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    @classmethod
    def print_count(cls):
        print(cls.count)

# 클래스 메서드 호출
Rectangle.print_count() # 출력 결과: 0

# 인스턴스 생성 시 클래스 변수 값 증가
rectangle1 = Rectangle(3, 4)
Rectangle.print_count() # 출력 결과: 1

rectangle2 = Rectangle(5, 6)
Rectangle.print_count() # 출력 결과: 2

# Deposit 클래스를 생성하라. 이 클래스는 세 개의 인스턴스 변수 initial과 interest, n을 갖는다.
# initial은 원금을 의미하고 interest는 년 이자율을 나타낸다. 초기화 함수에서 세 개의 인스턴스 변수를
# 전달 받은 값으로 설정해야 한다. 클래스 메소드 profit()은 n년 후 원리금을 반환한다.
# n년 후 원리금은 initial * (1 + interest)**n이다.
# Deposit 클래스를 이용하여 100만원을 이율 3.5%로 7년간 저축했을 때 원리금을 구하는 프로그램을 작성하라.
# 단 원리금은 정수로 표시되어야 한다.
class Deposit:
    def __init__(self, initial, interest, n):
        self.initial = initial
        self.interest = interest
        self.n = n
    
    def profit(self):
        return int(self.initial * (1 + self.interest)**self.n)

x = Deposit(1000000, 0.035, 7)
print(x.profit())

# 캡슐화 - 게터/세터 사용
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # age 인스턴스 변수를 비공개로 설정

p = Person("Alice", 25)
print(p.name)   # Alice
print(p.__age)  # 비공개 인스턴스 변수에 접근 시 에러 발생

# 예제의 Teacher 클래스에서 People 클래스의 __init__()를 호출하지 않고
# 부모 클래스의 age, name 인스턴스 변수를 이용할 수 있는가? 이용할 수 없다면 그 이유는?
# 이용할 수 있게 하려면 프로그램을 어떻게 수정해야 하는가?
class People :
    def __init__(self, age=0, name=None):
        self.__age = age
        self.__name = name

    def get_age(self):
        return self.__age
    
    def get_name(self):
        return self.__name
    
    def set_age(self, age):
        self.__age = age
        
    def set_name(self, name):
        self.__name = name
    
    def introMe(self):
        print("Name :", self.__name, "age :", str(self.__age))

class Teacher(People) :
    def __init__(self, age=0, name=None, school=None) :
        super().__init__(age, name)
        self.school = school

    def showSchool(self):
        print("My School is ", self.school)

t = Teacher(35,'Kim','highschool')
t.introMe()
t.set_name('Lee')
t.introMe()
t.showSchool()

# 다음 Person 클래스를 상속 받는 Employee 클래스를 정의하라.
# Employee 클래스에 employeeID 인스턴스 변수를 추가하고 getID() 메소드를 정의하라.
# getID() 메소드는 employeeID를 반환하는 메소드이다. Employee 클래스를 이용하여
# Employee("동양", 65, 2019)로 생성된 객체의 이름, 나이, ID를 출력하라.
class Person:
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    def getName(self): 
        print(self.name) 

    def getAge(self): 
        print(self.age) 

class Employee(Person):
    def __init__(self, name, age, employeeID):
        super().__init__(name, age)
        self.employeeID = employeeID
    
    def getID(self):
        print(self.employeeID)
    
employee = Employee('동양', 65, 2019)
employee.getName()
employee.getAge()
employee.getID()

# 클래스 분리
class Game:
    def __init__(self, player_name, player_hp, player_attack, monster_name, monster_hp, monster_attack):
        self.player_name = player_name
        self.player_hp = player_hp
        self.player_attack = player_attack
        self.monster_name = monster_name
        self.monster_hp = monster_hp
        self.monster_attack = monster_attack

    def fight(self):
        while self.player_hp > 0 and self.monster_hp > 0:
            print(f"{self.player_name}의 체력: {self.player_hp}")
            print(f"{self.monster_name}의 체력: {self.monster_hp}")
            self.monster_hp -= self.player_attack
            print(f"{self.player_name}이 {self.monster_name}을 공격하여 {self.player_attack}의 데미지를 입혔습니다.")
            if self.monster_hp <= 0:
                print(f"{self.monster_name}을 물리쳤습니다.")
                break
            self.player_hp -= self.monster_attack
            print(f"{self.monster_name}이 {self.player_name}을 공격하여 {self.monster_attack}의 데미지를 입혔습니다.")
            if self.player_hp <= 0:
                print(f"{self.player_name}이 죽었습니다.")
                break

class Player:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def attack_monster(self, monster):
        print(f"{self.name}이(가) {monster.name}을(를) 공격했습니다.")
        damage = self.attack
        monster.defend(damage)

    def defend(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name}이(가) 죽었습니다.")
        else:
            print(f"{self.name}의 체력이 {self.hp} 남았습니다.")

class Monster:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def attack_player(self, player):
        print(f"{self.name}이(가) {player.name}을(를) 공격했습니다.")
        damage = self.attack
        player.defend(damage)

    def defend(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name}이(가) 죽었습니다.")
        else:
            print(f"{self.name}의 체력이 {self.hp} 남았습니다.")

class Game:
    def __init__(self):
        self.player = None
        self.monster = None

    def create_player(self, name, hp, attack):
        self.player = Player(name, hp, attack)

    def create_monster(self, name, hp, attack):
        self.monster = Monster(name, hp, attack)

    def fight(self):
        while self.player.hp > 0 and self.monster.hp > 0:
            self.player.attack_monster(self.monster)
            if self.monster.hp <= 0:
                break
            self.monster.attack_player(self.player)
            if self.player.hp <= 0:
                break

game = Game()
game.create_player("Alice", 100, 10)
game.create_monster("Goblin", 50, 5)
game.fight()

# 학생 정보를 관리하는 프로그램을 만드세요.
class Student:
    def __init__(self, name, student_id, year, major, avg_score):
        self.name = name
        self.student_id = student_id
        self.year = year
        self.major = major
        self.avg_score = avg_score
        
    def get_info(self):
        return f"이름:{self.name}, 학번:{self.student_id}, 학년:{self.year}, 전공:{self.major}, 평균:{self.avg_score}"
        
class StudentManager:
    def __init__(self):
        self.student_list = []
    
    def add_student(self, student):
        self.student_list.append(student)
        
    def show_all_student(self):
        for student in self.student_list:
            print(student.get_info())
            
    def remove_student(self, student_id):
        for student in self.student_list:
            if student_id==student.student_id:
                self.student_list.remove(student)
                
    def find_student(self, student_id):
        for student in self.student_list:
            if student_id==student.student_id:
                print(student.get_info())
                return
        print("학생이 존재하지 않습니다.")
    
student_manager = StudentManager()

student1 = Student('홍길동','20230001',2,'컴퓨터공학',90.5)
student2 = Student('김철수','20230002',4,'전자공학',82.5)
student3 = Student('이영희','20230003',1,'건축공학',92.5)

student_manager.add_student(student1)
student_manager.add_student(student2)
student_manager.add_student(student3)

student_manager.show_all_student()

student_manager.remove_student('20230001')

student_manager.show_all_student()

student_manager.find_student('20230002')

# 모듈
import random

# random 모듈 내에 포함된 변수, 함수, 클래스 등을 나열합니다.
print(dir(random))

# random 모듈 내에 포함된 choice 함수의 도움말을 출력합니다.
print(help(random.choice))

# 현재의 디렉토리와 시스템 경로 변수 출력하기
import os, sys
print(os.getcwd()) #현재 디렉토리 표시
print(sys.path) #환경변수에 지정된 디렉토리

# os
import os

# 현재 작업 디렉토리 확인
current_dir = os.getcwd()
print("현재 작업 디렉토리:", current_dir)

# 새로운 디렉토리 생성
new_dir = "new_directory"
os.mkdir(new_dir)
print(f"새로운 디렉토리 '{new_dir}'가 생성되었습니다.")

# 생성한 디렉토리 내에 파일 생성
new_file = "new_file.txt"
with open(os.path.join(new_dir, new_file), "w") as f:
    f.write("새로운 파일 내용")
print(f"'{new_file}' 파일이 '{new_dir}' 디렉토리 내에 생성되었습니다.")

# 지정된 디렉토리의 파일 및 디렉토리 목록 확인
list_dir = os.listdir(new_dir)
print(f"'{new_dir}' 디렉토리 내의 파일 및 디렉토리 목록: {list_dir}")

# 파일인지 디렉토리인지 확인
for item in list_dir:
    item_path = os.path.join(new_dir, item)
    if os.path.isfile(item_path):
        print(f"'{item_path}'는 파일입니다.")
    elif os.path.isdir(item_path):
        print(f"'{item_path}'는 디렉토리입니다.")

# 파일 삭제
os.remove(os.path.join(new_dir, new_file))
print(f"'{new_file}' 파일이 삭제되었습니다.")

# 디렉토리 삭제
os.rmdir(new_dir)
print(f"'{new_dir}' 디렉토리가 삭제되었습니다.")

# datetime
import datetime

# 현재 날짜
today = datetime.date.today()

# 100일 후의 날짜
hundred_days_later = today + datetime.timedelta(days=100)

# 1000일 후의 날짜
thousand_days_later = today + datetime.timedelta(days=1000)

# 결과 출력
print("100일 후:", hundred_days_later)
print("1000일 후:", thousand_days_later)

# calender
import calendar

# 2023년 3월의 달력을 출력합니다.
print("2023년 3월의 달력:")
print(calendar.month(2023, 3))

# 2023년 3월 15일의 요일을 확인합니다. (월요일: 0, 화요일: 1, ..., 일요일: 6)
year = 2023
month = 3
day = 15
weekday = calendar.weekday(year, month, day)
print("2023년 3월 15일은 요일 인덱스 {}에 해당하는 요일입니다.".format(weekday))

# 요일 인덱스를 사용하여 요일 이름을 가져옵니다.
weekday_name = calendar.day_name[weekday]
print("2023년 3월 15일은 {}입니다.".format(weekday_name))

# matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.linspace(-np.pi, np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

# 그래프 그리기
plt.plot(x, y_sin, label='sin')
plt.plot(x, y_cos, label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sin and Cos Functions')
plt.legend()
plt.show()