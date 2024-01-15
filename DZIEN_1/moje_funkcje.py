#przykład 1
n= 100
def policz(a:int,b:float,c:float,y:int=5)->float:
    global n
    n = (a+b)*y-c+n
    return n

print(policz(4,6,7,2))
print(policz(3.5645,6,7,True))
print(policz(4,6,7))
print(n)

