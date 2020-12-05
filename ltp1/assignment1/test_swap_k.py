import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_empty_case(self):
        """
        Test for when empty list is provided
        """
        actual = []
        expected = []

        a1.swap_k(actual, 0)
        self.assertEqual(actual, expected)

    


    def test_too_small(self):
        """
        Test for a one element list
        """
        actual = [5]
        expected = [5]

        a1.swap_k(actual, 0)
        self.assertEqual(actual, expected)

    def test_small_even(self):
        """
        Test for the smallest possible even-numbered long list
        """
        actual = [1, 2]
        expected = [2, 1]

        a1.swap_k(actual, 1)
        self.assertEqual(actual, expected)

    def test_small_odd(self):
        """
        Test for the smallest possible odd-numbered long list
        """
        actual = ["one", "two", "three"]
        expected = ["three", "two", "one"]

        a1.swap_k(actual, 1)
        self.assertEqual(actual, expected)

    def general_case(self):
        """
        Test when k is not close to the middle of the list
        """

        actual = [1, 2, 3, 4, 5, 6]
        expected = [5, 6, 3, 4, 1, 2]

        a1.swap_k(actual, 2)
        self.assertEqual(actual, expected)



    def test_longer_at_middle(self):
        """
        Test for a longer even-length list where k is close to the middle of the list
        """

        actual = [1, 2, 3, 4, 5, 6]
        expected = [4, 5, 6, 1, 2, 3]

        a1.swap_k(actual, 3)
        self.assertEqual(actual, expected)


    


if __name__ == '__main__':
    unittest.main(exit=False)
