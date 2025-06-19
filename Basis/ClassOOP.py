class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def MyFunc(self):
        print("my name is "+ self.name)

p1 = Person("mugay",18)
p1.MyFunc()