import unittest
from algo.comparison_sort import *

class TestBubbleSort(unittest.TestCase):
    def test1(self):
        arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
        exp = list(sorted(arr))
        bubblesort(arr)
        self.assertListEqual(arr, exp)

class TestInsertionSort(unittest.TestCase):
    def test1(self):
        arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
        exp = list(sorted(arr))
        insertionsort(arr)
        self.assertListEqual(arr, exp)

class TestSelectionSort(unittest.TestCase):
    def test1(self):
        arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
        exp = list(sorted(arr))
        selectionsort(arr)
        self.assertListEqual(arr, exp)

class TestHeapSort(unittest.TestCase):
    def test1(self):
        arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
        exp = list(sorted(arr))
        heapsort(arr)
        self.assertListEqual(arr, exp)

class TestMergeSort(unittest.TestCase):
    def test1(self):
        arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
        exp = list(sorted(arr))
        b = mergesort(arr)
        self.assertListEqual(b, exp)
