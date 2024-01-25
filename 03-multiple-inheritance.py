class Person:
    def __init__(self, name):           # 생성자 함수
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'


class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'

# 엄마, 아빠 라는 두 개의 클래스
# 다중 상속
# 하위(부모1, 부모2)

class FirstChild(Mom, Dad):
    def swim(self):
        return '첫째가 수영'
    
    def cry(self):
        return '첫째 응애'
    
baby1 = FirstChild('김애기')

# 본인꺼
print(baby1.cry())  # 첫째 응애
print(baby1.swim()) # 첫째가 수영

# dad의 메서드
print(baby1.walk()) # 아빠가 걷기

# Mom의 메서드(겹침) > 내꺼
print(baby1.swim()) # 아빠가 걷기

print(baby1.gene) # XY 
'''
"중복된 속성 gene/메서드가 있을 때" 
"본인" 없으면
"상속 순서 FirstCHhild(Dad, Mom)"> 순서대로
'''    


