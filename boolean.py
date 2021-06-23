#Boolean get True or False
# used to comparison

2
my_boolean = True
print(my_boolean)  #True

print(2 == 3)    # False
 
print("hello" == "hello")    #True

print(2 != 3)    
print(2 < 3)
print(2 >= 3)

#compared with int and float
print(7 ==7.0)  #True
print(7*0.1 == 0.7) #False

#precicion up to 15 decimal places
print(9.0000000000000001 == 9.0)  #True
print(9.00000000000001 == 9.0)   #False

#Boolean logic 
'''
it is used to make more complicated conditiobns for if statements that reply 
on more than one condition.
Python's Boolean operators are "and","or", and "not"
The end operator takes two arguments, and evaluates as True if, and both of its 
arguments are True. Otherwise, it evaluates to False.
'''
print( 1 == 1 and 2  == 2 )
print( 1 == 1) and (2 == 2)
print( 1 == 1 and 2  == 3 )
print( 1 != 1 and 2 == 2 )
print( 2 < 1 and 3 > 6 ) 

print( 0+0 == 0)
print( 0 * 0  == 0)

print( 1 == 1 or 2 == 2)
print( 1== 1 or 2 == 3)
print( 1 > 2 or 2 ==3)


print(not 1 == 1)   #False
print(not 1 > 7)   #True



if not True:
    print('1')
elif not (1+1 == 3):
    print('2')
else:
    print('3')
    
#Operator Precedence
'''
this is a very important concept in programming. It is an extension of the mathematical
idea of prder of operations to include other operators
'''
print(False == False or True)  #True =print(False == (False and True))
print(False == (False or True))   #False
print(False == (False and True)) #True
print(((False == False) or True))   #True
    

if 1 + 1 * 3 == 6:
    print("yes")
else:
    print("no")
    
    
#Chaining Multiple Conditions
grade = 88
if( grade >=70 and grade <= 100):   #前後兩個grade變數不可以少
    print("passed") 
    
  
x = 4
y = 2
if not 1+1 == y or x ==4 and 7==8:
    print('yes') 
elif x < y :
   print("no")
else:
    print("whatever")
    
    
    
    

    
    
    