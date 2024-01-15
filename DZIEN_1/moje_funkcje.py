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

#przykład 2

print((lambda a:a+16)(9))
s = lambda a,b,c=3:(a+b)*c
print(s(4,1,2))
print(s(4,0.87677,2.22))
print(s(4,0.87677))

num = [56,7,8,-9,0,7,13,65,12,99,-100,3,5,16,7,-34]

nbparz = list(filter(lambda x:x%2==0,num))
print(nbparz)

cube = list(map(lambda x:x**3,num))
print(cube)

kwadraty = [i**2 for i in range(5,5000,5)]
print(kwadraty)

#przykład 4

import funkcje.bfunkcje as bf
def witaj(imie):
    return f'Miło Cię widzieć {imie}'

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Olaf"))
print(osoba(bf.konkurs,"Ola",66,13))
print(osoba(bf.bonus,66,10))
