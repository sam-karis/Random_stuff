# Find the minimal value of f(x)=3x^4-8x^3+6x^2-12 on [-3,3] 
print('\x48\x49!')
def get_minimal_value(x):
    res = 3*x^4-8*x^3+6*x^2-12
    return res

for i in range(-3, 4):
    print(f'The value for {i} is: ', get_minimal_value(i))


class B():
    def __init__(self, s):
        self.s = s
        s ="test"

x = B('122')
print(x.s)

x = []
y = x
y.append(10)
z = 5
w = z
z = z - 1
print(y, x, z, w)

def f(x=[]):
    x.append(1)
    print(x)
f()
f()
f()

class A():
    def __init__(self, s):
        self.s = s
class B(A):
    def __init__(self, s):
        self.x = s

x= B(5)
print(x.s)

x = 10
def f():
    print(x)
    x =x -1
f()
print(x)