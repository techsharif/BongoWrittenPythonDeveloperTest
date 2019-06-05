import unittest
from solution import *


class TestSecondProblem(unittest.TestCase):

    def test_is_non_primitive(self):

        class CustomClass(object):
            pass

        class Person(object):
            def __init__(self, first_name, last_name, father):
                self.first_name = first_name
                self.last_name = last_name
                self.father = father
        person = Person("User", "1", None)
        obj = CustomClass()

        data = [
            is_non_primitive(5),
            is_non_primitive("hello"),
            is_non_primitive(5.2),
            is_non_primitive(person),
            is_non_primitive(obj)
        ]

        result_data = [
            False,
            False,
            False,
            True,
            True
        ]
        self.assertEqual(data, result_data)


    def test_with_provided_data(self):
        class Person(object):
            def __init__(self, first_name, last_name, father):
                self.first_name = first_name
                self.last_name = last_name
                self.father = father

        person_a = Person("User", "1", None)
        person_b = Person("User", "2", person_a)

        data = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4,
                "user": person_b,
                }
            },
        }

        result = [
            ["key1", 1],
            ["key2", 1],
            ["key3", 2],
            ["key4", 2],
            ["key5", 3],
            ["user", 3],
            ["first_name", 4],
            ["last_name", 4],
            ["father", 4],
            ["first_name", 5],
            ["last_name", 5],
            ["father", 5]
        ]

        self.assertEqual(calculate_depth(data, 1), result)

    def test_with_blank_object(self):
        class CustomClass(object):
            pass

        obj = CustomClass()

        data = {
            "key": obj
        }

        result = [
            ["key", 1]
        ]

        self.assertEqual(calculate_depth(data, 1), result)


    def test_with_just_one_object(self):
        class CustomClass(object):
            def __init__(self, one, two, three):
                self.one = one
                self.two = two
                self.three = three

        obj1 = CustomClass(1,2,3)
        obj2 = CustomClass(1,2,obj1)

        data = obj2

        result = [
            ['one', 1], 
            ['two', 1], 
            ['three', 1],
            ['one', 2],
            ['two', 2],
            ['three', 2]
        ]

        self.assertEqual(calculate_depth(data, 1), result)

    def test_with_just_one_complex_object(self):
        class CustomClass(object):
            def __init__(self, one, two, three):
                self.one = one
                self.two = two
                self.three = three

        obj1 = CustomClass(1,2,3)
        obj2 = CustomClass(obj1,2,3)
        obj3 = CustomClass(obj1,obj2,3)
        obj4 = CustomClass(obj1,obj2,obj3)

        data = obj4

        result = [
            ['one', 1], 
            ['one', 2], 
            ['two', 2],
            ['three', 2],
            ['two', 1],
            ['one', 2],
            ['three', 3],
            ['two', 2],
            ['three', 2],
            ['three', 1],
            ['one', 2],
            ['three', 3],
            ['two', 2],
            ['three', 3],
            ['three', 2]
        ]

        self.assertEqual(calculate_depth(data, 1), result)

    def test_with_just_one_blank_object(self):
        class CustomClass(object):
            pass

        obj = CustomClass()

        data = obj

        result = []

        self.assertEqual(calculate_depth(data, 1), result)

    def test_with__blank_data(self):
        
        data = {}

        result = []

        self.assertEqual(calculate_depth(data, 1), result)


if __name__ == '__main__':
    unittest.main()