import unittest
from one_hot_encoder import fit_transform


class TestOneHotEncoder(unittest.TestCase):

    def test_tf(self):
        test_list = ['abc', 'bca', 'abc']
        actual = fit_transform(test_list)
        expected = [('abc', [0, 1]),
                    ('bca', [1, 0]),
                    ('abc', [0, 1])]
        self.assertEqual(actual, expected)

    def test_empty(self):
        with self.assertRaises(TypeError) as cm:
            fit_transform()
        error = cm.exception
        self.assertIsInstance(error, TypeError)

    def test_string(self):
        test_string = 'test'
        actual = fit_transform(test_string)
        expected = [('test', [1])]
        self.assertEqual(actual, expected)

    def test_empty_list(self):
        empty_list = []
        actual = fit_transform(empty_list)
        expected = []
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
