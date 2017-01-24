import unittest

def classifyTriangle(a,b,c):
    if a > 0 and b > 0 and c > 0:
        if (abs(a-b) <= c <= a + b):
            if a * a + b * b == c * c :
                return "right triangle"
            elif a == b == c:
                return "equilateral triangle"
            elif a != b != c:
                return "scalene triangle"
            else:
                return "isosceles triangle"  
        else:
            return "False"
    else:
        return "False"


class TestMyFunctions(unittest.TestCase):

    def test1(self):
        self.assertEqual(classifyTriangle(1,0,2),"False")
        self.assertEqual(classifyTriangle(2,1,-1),"False")
    def test2(self):
        self.assertEqual(classifyTriangle(3,4,6),"scalene triangle") 
        self.assertEqual(classifyTriangle(2,3,4),"scalene triangle")
    def test3(self):
        self.assertEqual(classifyTriangle(3,4,5),"right triangle")
        self.assertEqual(classifyTriangle(7,24,25),"right triangle")
    def test4(self):
        self.assertEqual(classifyTriangle(1,2,2),"isosceles triangle" )
        self.assertEqual(classifyTriangle(2,5,5),"isosceles triangle" )   
    def test5(self):
        self.assertEqual(classifyTriangle(3,3,3),"equilateral triangle")
        self.assertEqual(classifyTriangle(7,7,7),"equilateral triangle")  
    def test6(self):
        self.assertEqual(classifyTriangle(2,3,7),"False")
        self.assertEqual(classifyTriangle(5,4,20),"False")   
     

if __name__ == "__main__":
    unittest.main(exit=False)    
