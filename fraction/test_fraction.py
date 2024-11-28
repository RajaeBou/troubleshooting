import unittest
from fraction import Fraction

class TestFraction(unittest.TestCase):
    def test_init(self):
        f = Fraction(3,2)
        self.assertEqual(f.numerator,3)
        self.assertEqual(f.denominator, 2)

        f=Fraction(9)
        self.assertEqual(f.numerator,9)
        self.assertEqual(f.denominator ,1)

        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)

    def test_str(self):
        f = Fraction(1,2)
        self.assertEqual(str(f),"1/2")

        f1 = Fraction(3, 1)
        self.assertEqual(str(f1), "3/1")


    def test_as_mixed_number(self):
        f=Fraction (12,5)
        self.assertEqual(f.as_mixed_number(),'2 + 2/5')

        f1=Fraction(10,11)
        self.assertEqual(f1.as_mixed_number(),'10/11')

        f2 = Fraction(8, 4)
        self.assertEqual(f2.as_mixed_number(), "2")

        #f3 = Fraction(-7, 3)
        #self.assertEqual(f3.as_mixed_number(), "-2 + 1/3")

    def test_add(self):
        f1= Fraction(2,3) 
        f2= Fraction(1,2)
        somme=f1 + f2
        self.assertEqual(str(somme),'7/6')

        f3 = Fraction(1, 3)
        somme2 = f1 + f3
        self.assertEqual(str(somme2), '1/1')
        
    def test_sub(self):

        f1=Fraction(3,5)
        f2=Fraction(1,3)
        sub=f1-f2
        self.assertEqual(str(sub),'4/15')

        f3 = Fraction(1, 1)
        sub2 = f1 - f3
        self.assertEqual(str(sub2), '-2/5')

    def test_mult(self):
        
        f1=Fraction(1,2)
        f2=Fraction(2,4)
        result = f1*f2
        self.assertEqual(str(result),'1/4')

        f3 = Fraction(3, 5)
        result2 = f1 * f3
        self.assertEqual(str(result2), '3/10')

        f1 = Fraction(-1, 2)
        #f2 = Fraction(2, -4)
        #result = f1 * f2
        #self.assertEqual(str(result), '1/4')

        f3 = Fraction(3, 5)
        result2 = f1 * f3
        self.assertEqual(str(result2), '-3/10')
        
        


    def test_div(self):
        f1=Fraction(2,5)
        f2=Fraction(4,3)
        div = f1/f2
        self.assertEqual(str(div),'3/10')

        with self.assertRaises(ZeroDivisionError):
            f2/Fraction(0,8)
            
    
    def test_truediv(self):
        f1=Fraction(6,5)
        f2=Fraction(4,10)
        div=f1/f2
        f3=Fraction(3,5)
        div2=f3/f1
        self.assertEqual(str(div),'3/1')
        self.assertNotEqual(str(div2),'15/30')
        
    def test_is_meth(self):
        f1=Fraction(0,5)
        self.assertTrue(f1.is_zero())

        f2 = Fraction(3, 4)
        self.assertFalse(f2.is_zero())

        f1=Fraction(6,2)
        self.assertTrue(f1.is_integer())

        f2 = Fraction(5, 3)
        self.assertFalse(f2.is_integer())

        f3 = Fraction(-4,5)
        f4 = Fraction(2,3)
        f5 = Fraction(3,3)
        f6 = Fraction(7,5)
        self.assertTrue(f3.is_proper())
        self.assertTrue(f4.is_proper())
        self.assertFalse(f5.is_proper())
        self.assertFalse(f6.is_proper())

        f7 = Fraction(-4,4)
        f8 = Fraction(6,6)
        f9= Fraction(-3,-3)
        self.assertFalse(f7.is_unit())
        self.assertTrue(f8.is_unit())
        self.assertTrue(f9.is_unit())
        

    def test_is_adjascent(self):
        f1=Fraction(1,4)
        f2=Fraction(1,5)
        
        self.assertTrue(f1.is_adjacent_to(f2))
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 2)

        self.assertFalse(f2.is_adjacent_to(f3))

        
        
        
if __name__ == "__main__":
    unittest.main()