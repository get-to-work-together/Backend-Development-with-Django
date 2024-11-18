import unittest


def my_func(a, b, c):
    """Dit is mijn waanzinnige functie
    
    >>> my_func(4, 3, 5)
    32
    """
    return a * (b + c)


# def test_my_func():
#     actual = my_func(4, 3, 5)
#     expected = 33
#     assert actual == expected, 'wrong result'


class TestMyFunc(unittest.TestCase):

    def test_my_func1(self):
        actual = my_func(4, 3, 5)
        expected = 32
        self.assertEqual(actual, expected)

    def test_my_func2(self):
        actual = my_func(1, 1, 1)
        expected = 2
        self.assertEqual(actual, expected)




# ------------------------

# print(help(my_func))

# actual = my_func(4, 3, 5)
# expected = 33

# print(actual, actual == expected)

# assert actual == expected, 'wrong result'


# test_my_func()

# import doctest
# doctest.testmod(verbose=True)

unittest.main()