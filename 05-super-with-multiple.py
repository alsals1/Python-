class A:
    def __init__(self):
        print('A Constructor')


class B(A):
    def __init__(self):
        super().__init__()
        print('B Constructor')


class C(A):
    def __init__(self):
        super().__init__()
        print('C Constructor')


class D(B, C):
    def __init__(self):
        super().__init__()
        print('D Constructor')


obj = D()

# super 순서 찾기 
print(D.mro()) # D B C A
# 역순으로 출력


# mro() 메서드