#if one or more functions are not defined in a class
#  it is called abstract cvlass

# class AB:
#     def sum(self):
#         pass   #undefining a function
#     def div(self):
#         pass
# obj = AB()
# print(obj.sum())


#defintion is same but we are acheving this by implementhod implementaiton
# in a different class


from abc import ABC, abstractmethod

class Greet():
    @abstractmethod
    def say_hello(self):
        pass

class English(Greet):
    def say_hello(self):
        return "Hello"
    
obj1 = English()
print(obj1.say_hello())
    