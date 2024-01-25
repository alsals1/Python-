class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')


class ParentB:
    
    value_b = 'b'               # 하위 클래스가 가져감
    
    
    def __init__(self):
        self.value_b = 'ParentB'            # ParentB 클래스가 만드는 것만 가져감.

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')


class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__()          # MRO 순서대로 super 는 ParentA
        self.value_c = 'Child'
        
    def show_value(self):
        print(f'Value from Child: {self.value_c}')


child = Child()
child.show_value()      # 자기자신의 것

print(child.value_a)     # Parent A  >>super 가 가져온 ParentA의 것
print(child.value_c)     # Child


# print(child.value_b)  # 'Child' object has no attribute 'value_b'
