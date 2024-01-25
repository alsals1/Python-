class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email


class Student(Person):              # Person 부모클래스를 상속받은 Student
    def __init__(self, name, age, number, email, student_id):       # 다 받고 마지막에 student_id 추가
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        self.student_id = student_id
        

# 다른 버전으로 Student 만들기 

class Student(Person):
    def __init__(self, name, age, number, email, student_id): # (위치인자 그대로 다 작성)
        super().__init__(name, age, number, email)  # super 가 부모 클래스를 소환
        # 같은 말 Person.__init__(name, ae, number, email)
        # Student는 여러 부모 클래스를 가질 수 있으므로, 직접 부모 클래스 이름 쓰지 않고 super
        
        self.student_id = student_id 