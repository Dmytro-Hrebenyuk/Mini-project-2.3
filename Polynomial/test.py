import unittest
from your_module import Polynomial, Mono

class TestPolynomial(unittest.TestCase):
    def test_mono(self):
        m1 = Mono(5, 2)
        self.assertEqual(m1.coefficient, 5)
        self.assertEqual(m1.degree, 2)
        # Add assertions for other properties of Mono instances
    
    def test_polynomial_creation(self):
        m1 = Mono(5, 2)
        m2 = Mono(3, 1)
        p1 = Polynomial(m1, m2)
        self.assertEqual(p1.head, m1)
        self.assertEqual(p1.head.next, m2)
        # Add more assertions for polynomial creation
    
    def test_polynomial_sorting(self):
        m1 = Mono(5, 2)
        m2 = Mono(3, 1)
        m3 = Mono(2, 3)
        p1 = Polynomial(m1, m2, m3)
        p1.sort()
        # Add assertions to check if polynomial is sorted correctly
    
    def test_polynomial_simplification(self):
        m1 = Mono(5, 2)
        m2 = Mono(0, 0)
        m3 = Mono(2, 1)
        p1 = Polynomial(m1, m2, m3)
        p1.simplify()
        # Add assertions to check if polynomial is simplified correctly
    
    def test_polynomial_operations(self):
        m1 = Mono(5, 2)
        m2 = Mono(3, 1)
        m3 = Mono(2, 0)
        p1 = Polynomial(m1, m2, m3)
        p2 = Polynomial(Mono(-1, 2), Mono(2, 1), Mono(4, 0))
        # Test addition
        p3 = p1 + p2
        self.assertEqual(str(p3), "Polynomial: 4x**2+5x+6")
        # Test subtraction
        p4 = p1 - p2
        self.assertEqual(str(p4), "Polynomial: 6x**2+x-2")
        # Test multiplication
        p5 = p1 * p2
        self.assertEqual(str(p5), "Polynomial: -5x**4+7x**3+24x**2+16x+8")
    
    def test_evaluation(self):
        m1 = Mono(5, 2)
        m2 = Mono(3, 1)
        m3 = Mono(2, 0)
        p1 = Polynomial(m1, m2, m3)
        self.assertEqual(p1.eval_at(2), 28)
        self.assertEqual(p1.eval_at(0), 2)
    
    def test_equality(self):
        m1 = Mono(5, 2)
        m2 = Mono(3, 1)
        m3 = Mono(2, 0)
        p1 = Polynomial(m1, m2, m3)
        p2 = Polynomial(Mono(5, 2), Mono(3, 1), Mono(2, 0))
        p3 = Polynomial(Mono(5, 2), Mono(3, 1))
        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)
    
    def test_set_membership(self):
        m1 = Mono(5, 2)
        m2 = Mono(3, 1)
        m3 = Mono(2, 0)
        p1 = Polynomial(m1, m2, m3)
        p2 = Polynomial(Mono(5, 2), Mono(3, 1), Mono(2, 0))
        p3 = Polynomial(Mono(1, 1), Mono(2, 0))
        s = set()
        s.add(p1)
        self.assertTrue(p2 in s)
        self.assertFalse(p3 in s)
    
    def test_derivative(self):
        m1 = Mono(5, 2)
        m2 = Mono(3, 1)
        m3 = Mono(2, 0)
        p1 = Polynomial(m1, m2, m3)
        p2 = Polynomial(Mono(10, 1), Mono(3, 0))
        p3 = p1.derivative
        self.assertEqual(p3, p2)

    def test_empty_polynomial(self):
        p = Polynomial()
        self.assertEqual(str(p), "Polynomial: 0")

    def test_single_term_polynomial(self):
        m1 = Mono(5, 2)
        p = Polynomial(m1)
        self.assertEqual(str(p), "Polynomial: 5x**2")

    def test_zero_coefficient(self):
        m1 = Mono(0, 2)
        m2 = Mono(3, 1)
        p = Polynomial(m1, m2)
        self.assertEqual(str(p), "Polynomial: 3x")
    
    # Add more test methods as needed for other functionalities and edge cases

if __name__ == '__main__':
    unittest.main()
