import unittest

from wyszukiwanie.wyszukiwania import linear_search, binary_search, jump_search

# ------------------------------------------------------
# Linear searching tests


class linear_searching_test_uneven_list(unittest.TestCase):
    search_list = [8, 2, -1, 9, 100, 2039, -4938, 0, 17]

    def test_find_in_empty(self):
        test = linear_search(8, [])
        self.assertIsNone(test)

    def test_find_first_value(self):
        test = linear_search(8, self.search_list)
        self.assertTrue(test)

    def test_find_last_value(self):
        test = linear_search(17, self.search_list)
        self.assertTrue(test)

    def test_find_middle_value(self):
        test = linear_search(100, self.search_list)
        self.assertTrue(test)

    def test_find_biggest_value(self):
        test = linear_search(2039, self.search_list)
        self.assertTrue(test)

    def test_find_smallest_value(self):
        test = linear_search(-4938, self.search_list)
        self.assertTrue(test)

    def test_not_find(self):
        test = linear_search(-49, self.search_list)
        self.assertIsNone(test)


class linear_searching_test_even_list(unittest.TestCase):
    search_list = [8, 2, -1, 9, 100, 2039, -4938, 0]

    def test_find_in_empty(self):
        test = linear_search(8, [])
        self.assertIsNone(test)

    def test_find_first_value(self):
        test = linear_search(8, self.search_list)
        self.assertTrue(test)

    def test_find_last_value(self):
        test = linear_search(0, self.search_list)
        self.assertTrue(test)

    def test_find_middle_value(self):
        test = linear_search(100 or 9, self.search_list)
        self.assertTrue(test)

    def test_find_biggest_value(self):
        test = linear_search(2039, self.search_list)
        self.assertTrue(test)

    def test_find_smallest_value(self):
        test = linear_search(-4938, self.search_list)
        self.assertTrue(test)

    def test_not_find(self):
        test = linear_search(-49, self.search_list)
        self.assertIsNone(test)

# ------------------------------------------------------
# Binary searching tests


class binary_searching_test_uneven_list(unittest.TestCase):
    search_list = [8, 2, -1, 9, 100, 2039, -4938, 0, 17]

    def test_find_in_empty(self):
        test = binary_search(8, [])
        self.assertIsNone(test)

    def test_find_first_value(self):
        test = binary_search(8, self.search_list)
        self.assertTrue(test)

    def test_find_last_value(self):
        test = binary_search(17, self.search_list)
        self.assertTrue(test)

    def test_find_middle_value(self):
        test = binary_search(100, self.search_list)
        self.assertTrue(test)

    def test_find_biggest_value(self):
        test = binary_search(2039, self.search_list)
        self.assertTrue(test)

    def test_find_smallest_value(self):
        test = binary_search(-4938, self.search_list)
        self.assertTrue(test)

    def test_not_find(self):
        test = binary_search(-49, self.search_list)
        self.assertIsNone(test)


class binary_searching_test_even_list(unittest.TestCase):
    search_list = [8, 2, -1, 9, 100, 2039, -4938, 0]

    def test_find_in_empty(self):
        test = binary_search(8, [])
        self.assertIsNone(test)

    def test_find_first_value(self):
        test = binary_search(8, self.search_list)
        self.assertTrue(test)

    def test_find_last_value(self):
        test = binary_search(0, self.search_list)
        self.assertTrue(test)

    def test_find_middle_value(self):
        test = binary_search(100 or 9, self.search_list)
        self.assertTrue(test)

    def test_find_biggest_value(self):
        test = binary_search(2039, self.search_list)
        self.assertTrue(test)

    def test_find_smallest_value(self):
        test = binary_search(-4938, self.search_list)
        self.assertTrue(test)

    def test_not_find(self):
        test = binary_search(-49, self.search_list)
        self.assertIsNone(test)

# ------------------------------------------------------
# Jump searching tests


class jump_searching_test_uneven_list(unittest.TestCase):
    search_list = [8, 2, -1, 9, 100, 2039, -4938, 0, 17]

    def test_find_in_empty(self):
        test = jump_search(8, [])
        self.assertIsNone(test)

    def test_find_first_value(self):
        test = jump_search(8, self.search_list)
        self.assertTrue(test)

    def test_find_last_value(self):
        test = jump_search(17, self.search_list)
        self.assertTrue(test)

    def test_find_middle_value(self):
        test = jump_search(100, self.search_list)
        self.assertTrue(test)

    def test_find_biggest_value(self):
        test = jump_search(2039, self.search_list)
        self.assertTrue(test)

    def test_find_smallest_value(self):
        test = jump_search(-4938, self.search_list)
        self.assertTrue(test)

    def test_not_find(self):
        test = jump_search(11, self.search_list)
        self.assertIsNone(test)


class jump_searching_test_even_list(unittest.TestCase):
    search_list = [8, 2, -1, 9, 100, 2039, -4938, 0]

    def test_find_in_empty(self):
        test = jump_search(8, [])
        self.assertIsNone(test)

    def test_find_first_value(self):
        test = jump_search(8, self.search_list)
        self.assertTrue(test)

    def test_find_last_value(self):
        test = jump_search(0, self.search_list)
        self.assertTrue(test)

    def test_find_middle_value(self):
        test = jump_search(100 or 9, self.search_list)
        self.assertTrue(test)

    def test_find_biggest_value(self):
        test = jump_search(2039, self.search_list)
        self.assertTrue(test)

    def test_find_smallest_value(self):
        test = jump_search(-4938, self.search_list)
        self.assertTrue(test)

    def test_not_find(self):
        test = jump_search(11, self.search_list)
        self.assertIsNone(test)


if __name__ == '__main__':
    unittest.main()
