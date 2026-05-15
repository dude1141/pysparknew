# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

# obj= A(10,20)
# print(obj.a)
# print(obj.b)

#protect variable and functions in class by applying acccess specifiers

class A:
    def __init__(self,balance):
        self._balance=balance
    
    def getbal(self):
        return (self._balance)
    
    def setbal(self,balance):
        self._balance= balance
        
    
obj= A(2000)
print(obj.setbal(4000))
print(obj.getbal())
