class A():
    def add(self, a, b):
        return a + b


class B(A):
    def sub(self, a, b):
        return a - b



print( B().add(4, 6))

try:
    print(B().sub(10,5))
except Exception as  e:
    print(e)
finally:
    print("小于0")