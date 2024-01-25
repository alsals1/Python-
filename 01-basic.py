class Person:                       # 클래스 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')


class Professor(Person):                    # 하위클래스(부모 클래스)
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
        
    def talk(self):
        print(f'반갑습니다~교수입니다~')            # 하위 클래스가 부모 클래스 대신 쓰임


class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa


p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

# 부모 클래스 Person 클래스의 talk 메서드를 활용
p1.talk()           # 반갑습니다. 박교수입니다.  >>>  반갑습니다~교수입니다~
s1.talk()           # 반갑습니다. 김학생입니다.

#... 상속



