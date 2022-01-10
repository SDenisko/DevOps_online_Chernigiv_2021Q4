This is the first part of the first task in the Python course. 
Let's install Jupyter Notebook to learn Python syntax.

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/43d421a687fa443328e81559a4b80dbeb6a17f27/task8.1/images/pip.JPG" width="400">


Mathematical functions:
Python has several basic math operators:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/43d421a687fa443328e81559a4b80dbeb6a17f27/task8.1/images/math_operators.JPG" width="400">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/43d421a687fa443328e81559a4b80dbeb6a17f27/task8.1/images/print.JPG" width="400">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/43d421a687fa443328e81559a4b80dbeb6a17f27/task8.1/images/math_example.JPG" width="400">


Python automatically define type of variables, but if two variables has different type - then need to convert to the same type:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/43d421a687fa443328e81559a4b80dbeb6a17f27/task8.1/images/math_example_2.JPG" width="400">


Let's try work with files:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/43d421a687fa443328e81559a4b80dbeb6a17f27/task8.1/images/files1.JPG" width="400">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/43d421a687fa443328e81559a4b80dbeb6a17f27/task8.1/images/files2.JPG" width="400">

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/43d421a687fa443328e81559a4b80dbeb6a17f27/task8.1/images/files3.JPG" width="400">


Listing:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/43d421a687fa443328e81559a4b80dbeb6a17f27/task8.1/images/list_exaples.JPG" width="400">


Strings:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/43d421a687fa443328e81559a4b80dbeb6a17f27/task8.1/images/string_examples.JPG" width="400">


Loops:

<img src="https://github.com/SDenisko/DevOps_online_Chernigiv_2021Q4/blob/43d421a687fa443328e81559a4b80dbeb6a17f27/task8.1/images/string_examples.JPG" width="400">



Let's try to do some more seriously.

In the second part of assignment 8.1, I decided to use PyCharm.
According to the task, i need to write a script to solve the equation: ax ^ 2 + bx + c = 0.
Some parameters: for a better study of python3, the script should have 6 functions (main (), validate_param (integer), discriminant (a, b, c), roots (d, a, b, c), solv_square (a, b, c) ) -> roots, Square_print (a, b, c, roots)), there should be unit tests.
I decided to split the script into three files: main.py, function.py, unitest.py. The "function.py" file contains all the functions, the unitest.py file contains all unit tests, and the main.py file contains only the call to the main () function.
Let's try!

function.py:


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


unitests.py:


	import function
	import unittest
	class TestModule (unittest.TestCase):
    		def test_discriminant(self):
        		self.assertEqual(function.discriminant(1,2,1), (0))
        		self.assertEqual(function.discriminant(1, 1, 1), (-3))
        		self.assertEqual(function.discriminant(10, -1, -1), (41))
    		def test_roots(self):
        		self.assertEqual(function.roots(4, 3, 4, 1), (-0.3333333333333333, -1.0))
        		self.assertEqual(function.roots(0,1,2,1),(-1))
        		self.assertEqual(function.roots(-8,1,2,3),(-1 - 1.4142135623730951j, -1 + 1.4142135623730951j))


main.py:


	import function #import functions from function file

	function.main()


<img src="" width="300">
<img src="" width="300">
<img src="" width="300">
