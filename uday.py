'''data types in python important datatypes'''
# -------------------------------------------------------------------------------------------------------
# 1) int 
# 2) float
# 3) complex     a + bj
# 4) str
# 5) list
# 6) tuple
# 7) set
# 8) dict
# 9) bool
# 10) None
# 11) bytes
# 12) byte array

# ------------------------------------------------------------------------------------------------------

# uday rama koteswa rao          # Single Line Comment in python
'''uday rama koteswarao'''       # multiline comments in python

# alt + shift + downarrow = to copy uppder line to down line 
# ctrl + frontword + /   =  to comment the code in python


# ------------------------------------------------------------------------------------------------------

''' to know the types of data in python '''

'''int (integer)'''
# print(type(0)) 
# print(type(2))
# print(type(6))
# print(type(5463246326324))
# print(type(-3323))


'''flt (float)'''
# print(type(.0))
# print(type(0.3))
# print(type(6.7))
# print(type(-9.1))
# print(type(-.3))


'''str (string)'''
# print(type('hello'))
# print(type("hello"))
# print(type('''hello'''))
# print(type("""hello"""))

# print('Hello') 
# print("Python")
# print('Hi')


''' bool '''
# print(type(True))
# print(type(False))
# print(6<8)
# print(16<8)

''' list '''
# print(type([1,'2',3.5,[4,3]]))
# print(type([]))

''' tuple '''
# a=1,2,3,4
# print(a)
# print(type(a))

''' set '''
# print(type({1}))
# print(type({1,2,3}))

''' dict '''
# print(type({}))
# print(type({1:'python'}))

''' complex '''
# a=complex(4)
# print(a)
# c=complex(5j)
# print(c)
# print(type(3+4j))

''' bytes '''
# print(type('hello'))
# print(type(b'hello'))

''' bytearray'''
# print((type(bytearray(b'hello'))))



# -------------------------------------------------------------------------------------------------------

''' ASCI VALUES IN PYTHON '''
# AMERICAN STANDRED CODE FOR INFORMATION INTERCHANGE

# a = 97 
# z = 122
# A = 65
# Z = 90

# Space = 32

# print(ord("A"))
# print(ord(" "))
# print(ord(","))
# print(chr(65))
# print(chr(42000))

# ----------------------------------------------------------------------------------------------------

'''Strings_Basics'''

# A String can be multiplied by only with integer
# A string cannot be multiplied with float and string 
# if we tried to multiply string with float or string we get any error 



# print('hello'* 5)                    # hellohellohellohellohello
# print('hello ' * 5)                  # hello hello hello hello hello   
# print('he\n'*5,end='')

# print('hi' * 3.4)                      # error

# print('hi' * 'b')                      # error

# print('hi' + 4)                        # error
# print('hi' + 3.7)                      # error

# print('hi'+'bye')                       # hibye
# print('hi '+'bye')                      # hi bye
# print('hi'+' bye')                      # hi bye
# print('hi'+''+'bye')                    # hibye  
# print('hi'+' '+'bye')                   # hi bye
# print('hi'+'                 '+'bye')     # hi          bye

# print('hi'+'-'+'5')                        # hi-5

# print('hello' 'bye')                         # hellobye
# print('hello' ,'bye')                           # hello bye
# print('hello'+'  '+'bye')                       # hello  bye
# print('hello'+'  '+str(7))                      # hello 7



# print('Today is thursday time is 4:32pm')
# print("Today is thursday time is 4:32pm")
# print('''Today is thursday time is 4:32pm''')
# print("""Today is thursday time is 4:32pm""")
# print('Today'+' '+'is'+' '+'thursday'+' '+'time'+' '+'is'+' '+'4:32pm')

# print(1,2,3,4,5,6,7)
# print('1'+'  '+'2'+'  '+'3')



# --------------------------------------------------------------------------------------------------------

'''End_&_sep Methods'''

# print(1,2,3,4,5,sep='')
# print(1,2,3,4,5,sep=' ')
# print(1,2,3,4,5,sep='  ')
# print(1,2,3,4,5,sep='-')
# print('he\n'*5,end='')
# print('he\n'*5,end='')


# --------------------------------------------------------------------------------------------------------

'''Type_Conversion & Casting Meothed'''

# print(type(6))
# print(type(8.9))
# print(type('hello'))

# a=1
# print(a)
# print(float(a))
# print(str(a))

# b=2.9
# print(int(b))
# print(str(b))
# print(str(b)+'hey')

# c='hello'                            # error
# print(int(c))                          # error
# print(float(c))                           # error

# d='7'
# print(type(d))
# print(int(d))
# print(float(d))

# e='4.8'
# print(type(e))
# print(float(e))
# n=float(e)                                      # 4.8
# print(int(n))                                      # 4

# ---------------------------------------------------------------------------------------------------













































































































































































