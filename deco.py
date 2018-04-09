def attach_data(func):
       func.data = 3
       return func
 
@attach_data
def add (x, y):
       return x + y
print(add(2, 3))
 
print(add.data)
