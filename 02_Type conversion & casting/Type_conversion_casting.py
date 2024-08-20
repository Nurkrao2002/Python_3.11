''' Format specifier '''

"""
Note:-
int --> %d or % %in
float --> %f
str --> %s
"""

a=5; b=6.7 ; c='hello'
print(type(a),type(b),type(c))
print(str(a+b)+c)
print(a)
print('%d' %a)
print('%i' %a)
print(b)
print('%f' %b)
print('%.1f'%b)

a=5
print(float(a))
print(str(a))
print('%f' %a)
print('%.1f' %a)

b=6.8
print(int(b))
print(str(b))

c='hello'
print(int('c'))         # value error
print(float(c))

d='5'
print(type(d))
e=int(d)
print(e,type(e))
f=float(d)
print(f,type(f))

g='4.7'
print(type(g))
print(int(g))          # ValueError
h=float(g)
print(h,type(h))
i=int(h)
print(i,type(i))

