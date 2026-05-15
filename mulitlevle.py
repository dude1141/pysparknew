class A:
    def sum(self,a,b):
        return a+b

class B():
    def display(self):
        print("am from B class")

class C(A,B):
    print("am from class C")

obj = C()
print(obj.sum(10,20))
print(obj())