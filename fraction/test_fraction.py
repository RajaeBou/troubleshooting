import unittest
from fraction import Fraction

class TestFraction(unittest.TestCase):
    def test_init(self):
        """
        f = Fraction(3,2)
        self.assertEqual(f.numerator,3)
        self.assertEqual(f.denominator, 2)

        f=Fraction(9)
        self.assertEqual(f.numerator,9)
        self.assertEqual(f.denominator ,1)

        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)
        """
        # Cas classique
        f = Fraction(3, 2)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 2)

        # Fraction entière
        f = Fraction(9)
        self.assertEqual(f.numerator, 9)
        self.assertEqual(f.denominator, 1)

        # Fraction négative
        f = Fraction(-3, 4)
        self.assertEqual(f.numerator, -3)
        self.assertEqual(f.denominator, 4)

        # Dénominateur négatif
        f = Fraction(3, -4)
        self.assertEqual(f.numerator, -3)
        self.assertEqual(f.denominator, 4)

        # Fraction avec 0 comme numérateur
        f = Fraction(0, 5)
        self.assertEqual(f.numerator, 0)
        self.assertEqual(f.denominator, 1)

        # Exception : dénominateur nul
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)

    def test_str(self):

        f = Fraction(1, 2)
        self.assertEqual(str(f), "1/2")

        # Fraction entière
        f = Fraction(3, 1)
        self.assertEqual(str(f), "3/1")

        # Fraction simplifiée
        f = Fraction(2, 4)
        self.assertEqual(str(f), "1/2")

        # Fraction négative
        f = Fraction(-3, 4)
        self.assertEqual(str(f), "-3/4")

        # Numérateur nul
        f = Fraction(0, 5)
        self.assertEqual(str(f), "0/1")

    def test_as_mixed_number(self):

        f1 = Fraction(3, 4)
        self.assertEqual(f1.as_mixed_number(), "3/4")


        f2 = Fraction(9, 4)
        self.assertEqual(f2.as_mixed_number(), "2 + 1/4")


        f3 = Fraction(8, 4)
        self.assertEqual(f3.as_mixed_number(), "2")


        #f4 = Fraction(-7, 3)
        #self.assertEqual(f4.as_mixed_number(), "-2  1/3")


        f5 = Fraction(-1, 4)
        self.assertEqual(f5.as_mixed_number(), "-1/4")


        f6 = Fraction(0, 5)
        self.assertEqual(f6.as_mixed_number(), "0")


        #f7 = Fraction(7, -3)
        #self.assertEqual(f7.as_mixed_number(), "-2  1/3")


        f8 = Fraction(-6, 3)
        self.assertEqual(f8.as_mixed_number(), "-2")


        f9 = Fraction(25, 4)
        self.assertEqual(f9.as_mixed_number(), "6 + 1/4")


        f10 = Fraction(5, 5)
        self.assertEqual(f10.as_mixed_number(), "1")

    def test_add(self):

        f1 = Fraction(1, 3)
        f2 = Fraction(1, 6)
        self.assertEqual(str(f1 + f2), "1/2")


        f3 = Fraction(1, 2)
        f4 = Fraction(1, 1)
        self.assertEqual(str(f3 + f4), "3/2")


        f5 = Fraction(0, 1)
        self.assertEqual(str(f1 + f5), "1/3")


        f6 = Fraction(-1, 3)
        self.assertEqual(str(f1 + f6), "0/1")


        f7 = Fraction(-5, 3)
        self.assertEqual(str(f1 + f7), "-4/3")


        f8 = Fraction(2, 5)
        f9 = Fraction(3, 10)
        self.assertEqual(str(f8 + f9), "7/10")

    def test_sub(self):

        f1 = Fraction(2, 3)
        f2 = Fraction(1, 3)
        self.assertEqual(str(f1 - f2), "1/3")


        f3 = Fraction(3, 4)
        self.assertEqual(str(f3 - f3), "0/1")


        f4 = Fraction(-1, 2)
        self.assertEqual(str(f1 - f4), "7/6")


        f5 = Fraction(1, 2)
        self.assertEqual(str(f5 - f3), "-1/4")


        f6 = Fraction(1, 1)
        self.assertEqual(str(f5 - f6), "-1/2")


        self.assertEqual(str(f1 - Fraction(0, 1)), "2/3")

    def test_mult(self):
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        self.assertEqual(str(f1 * f2), "1/2")


        f3 = Fraction(0, 1)
        self.assertEqual(str(f1 * f3), "0/1")


        f4 = Fraction(1, 1)
        self.assertEqual(str(f1 * f4), "2/3")


        f5 = Fraction(-3, 5)
        self.assertEqual(str(f1 * f5), "-2/5")


        f6 = Fraction(-1, 2)
        f7 = Fraction(-4, 3)
        self.assertEqual(str(f6 * f7), "2/3")


        f8 = Fraction(2, 3)
        self.assertEqual(str(f8 * Fraction(3, 2)), "1/1")
        
        


    def test_div(self):
        f1 = Fraction(2, 3)
        f2 = Fraction(4, 5)
        self.assertEqual(str(f1 / f2), "5/6")


        f3 = Fraction(1, 1)
        self.assertEqual(str(f1 / f3), "2/3")


        f4 = Fraction(-3, 5)
        self.assertEqual(str(f1 / f4), "-10/9")


        f5 = Fraction(-1, 2)
        self.assertEqual(str(f5 / f2), "-5/8")


        f6 = Fraction(6, 5)
        f7 = Fraction(2, 5)
        self.assertEqual(str(f6 / f7), "3/1")


        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 1) / Fraction(0, 1)
            
    
    def test_truediv(self):
        f1 = Fraction(2, 3)
        f2 = Fraction(4, 5)
        self.assertEqual(str(f1 / f2), "5/6")


        f3 = Fraction(1, 1)
        self.assertEqual(str(f1 / f3), "2/3")


        f4 = Fraction(-3, 5)
        self.assertEqual(str(f1 / f4), "-10/9")


        f5 = Fraction(-1, 2)
        self.assertEqual(str(f5 / f2), "-5/8")


        f6 = Fraction(6, 5)
        f7 = Fraction(2, 5)
        self.assertEqual(str(f6 / f7), "3/1")


        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 1) / Fraction(0, 1)

    def test_eq(self):

        f1 = Fraction(1, 2)
        f2 = Fraction(1, 2)
        self.assertTrue(f1 == f2)


        f3 = Fraction(2, 4)
        self.assertTrue(f1 == f3)


        f4 = Fraction(3, 4)
        self.assertFalse(f1 == f4)


        f5 = Fraction(-1, 3)
        f6 = Fraction(1, -3)
        self.assertTrue(f5 == f6)


        f7 = Fraction(-2, 3)
        self.assertFalse(f5 == f7)


        f8 = Fraction(0, 5)
        f9 = Fraction(0, 7)
        self.assertTrue(f8 == f9)


        with self.assertRaises(TypeError):
            f1 == "1/2"


        f10 = Fraction(100, 200)
        f11 = Fraction(1, 2)
        self.assertTrue(f10 == f11)


        f12 = Fraction(1, 3)
        f13 = Fraction(-1, 3)
        self.assertFalse(f12 == f13)


        f14 = Fraction(-2, -4)
        self.assertTrue(f14 == f3)

    def test_float(self):

        f1 = Fraction(1, 2)
        self.assertEqual(float(f1), 0.5)


        f2 = Fraction(4, 2)
        self.assertEqual(float(f2), 2.0)


        f3 = Fraction(-3, 4)
        self.assertEqual(float(f3), -0.75)


        f4 = Fraction(5, -2)
        self.assertEqual(float(f4), -2.5)


        f5 = Fraction(0, 7)
        self.assertEqual(float(f5), 0.0)


        f6 = Fraction(6, 8)
        self.assertEqual(float(f6), 0.75)


        f7 = Fraction(1000, 333)
        self.assertAlmostEqual(float(f7), 3.003003003, places=9)


        f8 = Fraction(-123456789, 100000000)
        self.assertAlmostEqual(float(f8), -1.23456789, places=9)

    def test_is_meth(self):

        self.assertTrue(Fraction(0, 5).is_zero())
        self.assertFalse(Fraction(3, 4).is_zero())


        self.assertTrue(Fraction(6, 3).is_integer())
        self.assertFalse(Fraction(7, 3).is_integer())


        self.assertTrue(Fraction(2, 3).is_proper())
        self.assertFalse(Fraction(4, 3).is_proper())


        self.assertTrue(Fraction(3, 3).is_unit())
        self.assertFalse(Fraction(2, 4).is_unit())

    def test_is_adjascent(self):

        f1 = Fraction(1, 3)
        f2 = Fraction(1, 4)
        self.assertTrue(f1.is_adjacent_to(f2))  # 1/3 - 1/4 = 1/12, adjacentes


        f3 = Fraction(1, 2)
        f4 = Fraction(1, 4)
        self.assertTrue(f3.is_adjacent_to(f4))  # 1/2 - 1/4 = 1/4, non adjacentes


        f5 = Fraction(2, 3)
        self.assertFalse(f5.is_adjacent_to(f5))  # 2/3 - 2/3 = 0/1, non adjacentes


        f6 = Fraction(-1, 3)
        f7 = Fraction(-1, 4)
        self.assertTrue(f6.is_adjacent_to(f7))  # -1/3 - (-1/4) = -1/12, adjacentes


        f8 = Fraction(1, 3)
        f9 = Fraction(-1, 4)
        self.assertFalse(f8.is_adjacent_to(f9))  # 1/3 - (-1/4) = 7/12, non adjacentes


        f10 = Fraction(0, 1)
        f11 = Fraction(1, 1)
        self.assertTrue(f10.is_adjacent_to(f11))  # 0/1 - 1/1 = -1/1, non adjacentescoverage run --source=fraction -m unittest discover


        f12 = Fraction(1000, 2001)
        f13 = Fraction(999, 2001)
        self.assertTrue(f12.is_adjacent_to(f13))  # 1000/2001 - 999/2001 = 1/2001, adjacentes


        with self.assertRaises(TypeError):
            f1.is_adjacent_to("1/4")  # Comparaison avec une chaîne invalide

        
        
        
if __name__ == "__main__":
    unittest.main()