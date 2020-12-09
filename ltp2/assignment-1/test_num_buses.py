import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Example tests for function a1.num_buses. """

    def test_general_case(self):
        """
        Test num_buses where there are more people than will fit on a single bus.
        """

        actual = a1.num_buses(75)
        expected = 2
        self.assertEqual(actual, expected)

            
    def test_zero_case(self):
        """
        Test num_buses where there are no people
        """

        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(actual, expected)

        
    def test_boundary_case(self):
        """
        Test num_buses where there are exactly enough people to fill all buses
        """

        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
