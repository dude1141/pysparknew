class A:
    def sum(self,a,b):
        return a+b

class B:
    def display(self):
        print("I am from B class")

class C(A,B):
    def show(self):
        print("I am from class C")

obj = C()
print(obj.sum(10,20))
print(obj.show())