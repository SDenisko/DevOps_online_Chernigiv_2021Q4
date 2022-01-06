import math

def solv_square(a, b, c):
  print('Are solving the equation: a•x²+b•x+c=0')
  a = input('Please, enter value a: ')
  b = input('Please, enter value b: ')
  c = input('Please, enter value C: ')
  a = float(a)
  b = float(b)
  c = float(c)

#    return (a,b,c)
#check entered values
#def validate_param(float):
#aa = type(a)
#bb = type(b)
#cc = type(c)

#calculate  discriminant
def discriminant(a, b, c):

  d = b**2 - 4*a*c

def roots(d, a, b, c):
  if d == 0:
     x = -b / ( 2 * a )
  elif d > 0:
       print('there are two roots:')
       x1 = (-b + math.sqrt(d)) / (2 * a)
       x2 = (-b - math.sqrt(d)) / (2 * a)
#print the results
def square_print(d, x, x1, x2):
  if d < 0:
     print('No roots, discriminant<0')
  elif d == 0:
       print('there is one root:')
       print('x =', x)
  elif d > 0:
       print('there are two roots:')
       print('x1 = ',x1)
       print('x2 = ',x2)

def main():
        solv_square()
        discriminant()
        roots()
        square_print()

