import unittest
from solution import calculate_depth


class TestFirstProblem(unittest.TestCase):

    def test_default(self):
        data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4
                }
            }
        }

        result_data = [
            ['key1',1],
            ['key2',1],
            ['key3',2],
            ['key4',2],
            ['key5',3]
        ]

        self.assertEqual(calculate_depth(data, 1), result_data)


    def test_with_no_data(self):
        data = {}
        result_data = []

        self.assertEqual(calculate_depth(data, 1), result_data)

    def test_depth(self):
        data = {
            "key1": {
                "key2": {
                    "key3": 4
                }
            }
        }

        result_data = [
            ['key1',1],
            ['key2',2],
            ['key3',3]
        ]

        self.assertEqual(calculate_depth(data, 1), result_data)

    def test_single_depth(self):
        data = {
            "key1": 1,
            "key2": 2,
            "key3": 3
        }

        result_data = [
            ['key1',1],
            ['key2',1],
            ['key3',1]
        ]

        self.assertEqual(calculate_depth(data, 1), result_data)


if __name__ == '__main__':
    unittest.main()