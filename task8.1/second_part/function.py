import math

def validate_param(elem):
    return int(elem)

def solv_square(a, b, c):
    d = discriminant(a, b, c)
    return roots(d, a, b, c)


def discriminant(a, b, c):
    d = b**2 - 4*a*c
    return d


def roots(d, a, b, c):
    if d == 0:
        x = -b / (2 * a)
        return x
    elif d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2
    else:
        from cmath import sqrt
        z = sqrt(d)
        x1 = complex((-b + z) / (2 * a))
        x2 = complex((-b - z) / (2 * a))
        return x1, x2

def square_print(a, b, c, roots):
    print("Are solving the equation: (%.x)•x²+(%.x)•x+(%.x)=0" % (a, b, c))
    for i in roots:
        print('x = ', i)


def main():
    a = validate_param(input('Please, enter value a:'))
    b = validate_param(input('Please, enter value b:'))
    c = validate_param(input('Please, enter value c:'))

    roots = solv_square(a, b, c)
    square_print(a, b, c, roots)
