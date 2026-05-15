class A:
    def sum(self,a,b):
        return a+b

class B(A):
    def display():
        print("am from B class")

obj= B()
print(obj.sum(10,30))
