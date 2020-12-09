import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_mixed_case(self):
        """
        Test a mixture of positive and negative price changes
        """
        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(actual, expected)
        
    def test_neg_case(self):
        """
        Test when all changes are negative
        """
        actual = a1.stock_price_summary([-0.05, -0.01, -0.01, 0])
        expected = (0, -0.07)
        self.assertEqual(actual, expected)

    def test_empty_case(self):
        """
        Test when an empty set is provided
        """
        actual = a1.stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_zero_case(self):
        actual = a1.stock_price_summary([0, 0, 0])
        expected = (0, 0)
        self.assertEqual(actual, expected)
        

if __name__ == '__main__':
    unittest.main(exit=False)
