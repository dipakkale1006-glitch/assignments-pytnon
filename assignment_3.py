
# task_1 find factorial of number which is given form user .

a=int(input('Enter the number:'))
def factorial(a):
     if a<2:
         return 1
     else:
         return a*factorial(a-1)
result=factorial(a)
print(('factorial of',a,'is',result))


#task_2

a=int(input('Enter the number:'))
import math
print('square root =',math.sqrt(a))
print('logarithm=',math.log(a))
print('sine=',math.sin(a))

