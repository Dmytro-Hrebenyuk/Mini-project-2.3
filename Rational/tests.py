import unittest
class TestRational(unittest.TestCase):

    def test_initialization(self):
        r = Rational(3, 4)
        self.assertEqual(r.numerator, 3)
        self.assertEqual(r.denominator, 4)

    def test_initialization_with_negative_denominator(self):
        with self.assertRaises(ValueError):
            Rational(3, 0)

    def test_str_representation(self):
        r = Rational(3, 4)
        self.assertEqual(str(r), '3/4')

    def test_mixed_form_representation(self):
        r = Rational(5, 4)
        self.assertEqual(r.mixed_form, '1 1/4')
    def test_zero_numerator(self):
        r = Rational(0, 4)
        self.assertEqual(r.mixed_form, '0')

    def test_addition(self):
        r1 = Rational(1, 2)
        r2 = Rational(1, 3)
        result = r1 + r2
        self.assertEqual(str(result), '5/6')
    def test_mixed_form_setter_normal_fraction(self):
        r = Rational(0, 1)
        r.mixed_form = '3/4'
        self.assertEqual(r.numerator, 3)
        self.assertEqual(r.denominator, 4)
    def test_mixed_form_setter(self):
        r = Rational(0, 1)
        r.mixed_form = '1 1/2'
        self.assertEqual(r.numerator, 3)
        self.assertEqual(r.denominator, 2)
    
    def test_negative_denominator(self):
        r = Rational(3, -4)
        self.assertEqual(r.numerator, -3)
        self.assertEqual(r.denominator, 4)

    def test_subtraction(self):
        r1 = Rational(3, 4)
        r2 = Rational(1, 4)
        result = r1 - r2
        self.assertEqual(str(result), '1/2')
    def test_reduce_zero_numerator(self):
        r = Rational(0, 4)
        result = r.reduce()
        self.assertEqual(result.numerator, 0)
        self.assertEqual(result.denominator, 1)
    def test_normal_fraction_representation(self):
        r = Rational(3, 4)
        self.assertEqual(r.mixed_form, '3/4')

    def test_multiplication(self):
        r1 = Rational(3, 4)
        r2 = Rational(1, 3)
        result = r1 * r2
        self.assertEqual(str(result), '1/4')

    def test_division(self):
        r1 = Rational(3, 4)
        r2 = Rational(1, 3)
        result = r1 / r2
        self.assertEqual(str(result), '9/4')

    def test_equality(self):
        r1 = Rational(3, 4)
        r2 = Rational(6, 8)
        self.assertEqual(r1, r2)

    def test_inequality(self):
        r1 = Rational(1, 2)
        r2 = Rational(2, 3)
        self.assertNotEqual(r1, r2)

    def test_less_than(self):
        r1 = Rational(1, 2)
        r2 = Rational(3, 4)
        self.assertTrue(r1 < r2)

    def test_less_than_or_equal(self):
        r1 = Rational(1, 2)
        r2 = Rational(3, 4)
        r3 = Rational(1, 2)
        self.assertTrue(r1 <= r2)
        self.assertTrue(r1 <= r3)

    def test_greater_than(self):
        r1 = Rational(3, 4)
        r2 = Rational(1, 2)
        self.assertTrue(r1 > r2)

    def test_greater_than_or_equal(self):
        r1 = Rational(3, 4)
        r2 = Rational(1, 2)
        r3 = Rational(3, 4)
        self.assertTrue(r1 >= r2)
        self.assertTrue(r1 >= r3)

    def test_reduce(self):
        r = Rational(4, 8)
        r.reduce()
        self.assertEqual(str(r), '1/2')

if __name__ == '__main__':
    unittest.main()