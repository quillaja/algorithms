import unittest
import random

import sort


def issorted(seq):

    for i, _ in enumerate(seq):
        try:
            if i > 0 and seq[i - 1] > seq[i]:
                return False
        except IndexError:
            pass

        try:
            if seq[i] > seq[i + 1]:
                return False
        except IndexError:
            pass

    return True


class TestSort(unittest.TestCase):
    def setUp(self):

        num_lists = 500

        # generate 1000 lists of length 0-9999, with random integers
        self.int_list = list()
        for i in xrange(1, num_lists):
            self.int_list.append([random.randint(0, 1000) for _ in xrange(i)])

        # 1000 lists of length 0-9999, with random floats
        self.float_list = list()
        for i in xrange(1, num_lists):
            self.float_list.append([random.uniform(0, 1000) for _ in xrange(i)
                                    ])

        # 1000 lists of length 0-9999, with random strings length 0-10
        self.string_list = list()
        alphabet = 'abcdefghijklmnopqrstuvwkyz'
        for i in xrange(1, num_lists):
            self.string_list.append([
                str([random.choice(alphabet) for _ in xrange(len(alphabet))
                     ]) for _ in xrange(i)
            ])


class TestIsSorted(unittest.TestCase):
    def test_issorted(self):
        empty = []
        good = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        bad = [6, 4, 0, 1, 45, 88, 11, 4, 0]
        alpha = 'abcdefg'
        alphabad = 'goiodfmqbe'

        self.assertTrue(issorted(empty))
        self.assertTrue(issorted(good))
        self.assertFalse(issorted(bad))

        self.assertTrue(issorted(alpha))
        self.assertFalse(issorted(alphabad))


class TestSortIntegers(TestSort):
    def test_bubble_sort(self):
        for case in self.int_list:
            sort.bubble_sort(case)
            self.assertNotEqual(self.int_list, case)
            self.assertTrue(issorted(case))

    def test_insertion_sort(self):
        for case in self.int_list:
            sort.insertion_sort(case)
            self.assertNotEqual(self.int_list, case)
            self.assertTrue(issorted(case))

    def test_merge_sort(self):
        for case in self.int_list:
            sort.merge_sort(case)
            self.assertNotEqual(self.int_list, case)
            self.assertTrue(issorted(case))

    def test_quick_sort(self):
        for case in self.int_list:
            sort.quick_sort(case)
            self.assertNotEqual(self.int_list, case)
            self.assertTrue(issorted(case))

    def test_heap_sort(self):
        for case in self.int_list:
            sort.heap_sort(case)
            self.assertNotEqual(self.int_list, case)
            self.assertTrue(issorted(case))
