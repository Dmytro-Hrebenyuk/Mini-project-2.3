import unittest
from line import Line, Point

class TestLine(unittest.TestCase):
    """Test cases for the Line class."""

    def setUp(self):
        """Set up test fixtures."""
        self.line1 = Line(Point(0.0, 0.0), Point(1.0, 3.0))
        self.line2 = Line(Point(2.0, 0.0), Point(0.0, 6.0))
        self.line3 = Line(Point(-1.0, -3.0), Point(-6.0, -5.0))
        self.line4 = Line(Point(0.0, -4.0), Point(5.0, -2.0))
        self.line5 = Line(Point(0.0, 0.0), Point(-5.0, 2.0))
        self.line6 = Line(Point(2.5, -1.0), Point(10.0, -4.0))

    def test_point_attributes(self):
        """Test attributes of the Point class."""
        point = Point(9, 0)
        self.assertEqual(point.x, 9)
        self.assertEqual(point.y, 0)

    def test_line_attributes(self):
        """Test attributes of the Line class."""
        self.assertEqual(self.line1.k, 3)
        self.assertEqual(self.line1.b, 0)
        self.assertFalse(self.line1 == 'qwer')

    def test_intersect(self):
        """Test intersection of lines."""
        self.assertAlmostEqual(self.line1.intersect(self.line2).x, 1)
        self.assertAlmostEqual(self.line1.intersect(self.line2).y, 3)
        self.assertIsNone(self.line3.intersect(self.line4))
        self.assertEqual(self.line5.intersect(self.line6), Line(Point(0.0, 0.0), Point(-5.0, 2.0)))
        self.assertAlmostEqual(self.line4.intersect(self.line6).x, 5)
        self.assertAlmostEqual(self.line4.intersect(self.line6).y, -2)

    def test_parallel_lines(self):
        """Test intersecting parallel lines."""
        parallel_line1 = Line(Point(0, 0), Point(1, 1))
        parallel_line2 = Line(Point(1, 0), Point(2, 1))
        self.assertIsNone(parallel_line1.intersect(parallel_line2))

    def test_coincident_lines(self):
        """Test intersecting coincident lines."""
        coincident_line1 = Line(Point(0, 0), Point(1, 1))
        coincident_line2 = Line(Point(0, 0), Point(1, 1))
        self.assertEqual(coincident_line1.intersect(coincident_line2), coincident_line1)

    def test_invalid_line_creation(self):
        """Test creation of a line with invalid points."""
        with self.assertRaises(ValueError):
            # Creating a line with identical points should raise a ValueError
            Line(Point(0.0, 0.0), Point(0.0, 0.0))

    def test_horizontal_line(self):
        """Test a line parallel to the x-axis."""
        horizontal_line = Line(Point(0, 3), Point(5, 3))
        self.assertEqual(horizontal_line.k, 0)
        self.assertEqual(horizontal_line.b, 3)

if __name__ == '__main__':
    unittest.main(verbosity=2)
