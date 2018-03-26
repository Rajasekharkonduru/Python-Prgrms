class Parent:
    def print1(self):
        print("this is parent class 'print1' method")


class Child(Parent):
    def print1(self):
        print("this is child class 'print' method") 
        super().print1()
c=Child()
c.print1()   

