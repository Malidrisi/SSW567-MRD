# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016

This file shows some simple (and buggy) python code to solve the Triangles assignment.   
The primary goal of this file is to demonstrate a simple python program and the use of the
unittest package.

Note that this code includes intentional errors for you to find.


@author: jrr
"""

import unittest     # this makes Python unittest module available
def classifyTriangle(a,b,c):
    """
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      
      BEWARE: This is the corrected Code
        
    """
     # require that the input values be > 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
        
 # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput';
        
 # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == c:
        return 'Equilateral'
    elif ((a * a) + (b * b)) == (c * c):
        return 'Right'
    elif (a != b) and  (b != c) and (a != b):
        return 'Scalene'
    else:
        return 'Isosceles'
        
        
def runClassifyTriangle(a, b, c):
     print "classifyTriangle(" , a , "," , b , "," , c  , ")=" , classifyTriangle(a,b,c) 

# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    
    def testClassifyTriangle1(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle','1,2,3 is Not a Triangle')
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(101,101,101),'Equilateral','101,101,101 is a Equilateral triangle')
        self.assertEqual(classifyTriangle(7,9,13),'Scalene','7,9,13 is a scalene triangle')
        self.assertEqual(classifyTriangle(2,2,1),'Isosceles','2,2,1 is an Isosceles triangle')
        
    def testClassifyTriangle2(self): 
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertNotEqual(classifyTriangle(211,211,211),'Equilateral','211,211,211 is invalid')
        self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','10,10,10 should be Equilateral')
        self.assertNotEqual(classifyTriangle(35,7,9),'Right','35,7,9 is Not a Triangle')
        self.assertNotEqual(classifyTriangle(1,2,2),'Scalene','1,2,2 should be Isoceles')
        self.assertNotEqual(classifyTriangle(12,16,20),'Isoceles','12,16,20 should be Right')
        
    def testClassifyTriangle3(self): 
        
        self.assertEqual(classifyTriangle('A','B','c'),'InvalidInput','A,B,c is invalid input')
        self.assertEqual(classifyTriangle(-1,2,1),'InvalidInput','-1,2,1 is invalid input')
        self.assertEqual(classifyTriangle('?',2,'S'),'InvalidInput','?,2,S is invalid input')
        self.assertEqual(classifyTriangle(0,11,100),'InvalidInput','0,11,100 is invalid input')
        self.assertEqual(classifyTriangle(300,11,239),'InvalidInput','300,11,239 is invalid input')
        
        
        

if __name__ == '__main__':
    # examples of running the  code
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    runClassifyTriangle(3,4,5)
    
    
    print('Begin UnitTest')
    unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    #unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    
    
       
                         