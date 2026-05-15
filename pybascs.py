set1 ={1,2,3,5,67,67}

for i in set1:
    print(i)

set1.add(10)

# print(set1)

set2={1,4,7,6}
print(set2)

print(set1.union(set2))
#set does not allwo duplicates,ordered
#tupleis a hetergenous data struture
#tuple follows zero indexing
#immutable
#
tuples= (10,20,30,40,"index")
print("tuple",tuples[1])

#key value pairts
#

mydict={"name":"Karthi","age":25}

#add new element
mydict["Sal"]=5000
print(mydict)

print(mydict["name"])

#loop
for a,b in mydict.items():
    print(a,b)


class A:
    def __init__(self):
        self.x = None
        self.y = None
        self.c = None

    def sum(self, x, y):
        self.x = x
        self.y = y
        return self.x + self.y

    def mult(self, c):
        self.c = c
        y = self.x * c
        return y


b = A()
b.sum(10,20)
print("b", b.mult(5))

# when you used self.x and self.y its going global
# and can be called with in class anywhere
#but first sum func should be called to get values of x and y and then only its passed to mult
