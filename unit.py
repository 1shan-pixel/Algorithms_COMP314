import unittest 

import insertion_sort as insertion

import quick_sort as quick 

import selection_sort as selection 

class TestSortingAlgorithms(unittest.TestCase):
    def test_insertion_sort(self):
        arr = [6,5,4,3,2,1]
        sorted_arr = insertion.insertion_sort(arr)
        self.assertEqual(sorted_arr, [1,2,3,4,5,6])
    def test_selection_sort(self):
        arr = [6,5,4,3,2,1]
        sorted_arr = selection.selection_sort(arr)
        self.assertEqual(sorted_arr, [1,2,3,4,5,6])
    def test_quick_sort(self):
        arr = [6,5,4,3,2,1]
        sorted_arr = quick.quick_sort(arr)
        self.assertEqual(sorted_arr, [1,2,3,4,5,6])

    
if __name__ == '__main__':
    unittest.main()