class A():
    def methoda(self):
        print("iam from class A")
    
class B(A):
    def methodb(self):
        print("iam from class B")

    
class C(B):
    def methodc(self):
        print("iam from class c")

obj1 = C()
obj1.methoda()
obj1.methodb()
obj1.methodc()

#inheritance happens in chain in multilevel
#if you see i am just calling C, but it is inheriting all mehtods
