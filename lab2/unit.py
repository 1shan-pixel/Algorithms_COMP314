import unittest 

import quick_sort as quick


import merge_sort as merge 
#different such test cases. 
test_cases = [
            ([6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6]),
            ([8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8]),
            ([], []),
            ([5], [5]),
        ]

class TestSortingAlgorithms(unittest.TestCase):
    def test_quick_sort(self):
        for input_array, expected_output in test_cases:
            with self.subTest(input_array=input_array): #helps to identify which test case failed. 
                sorted_array = quick.quick_sort(input_array) #calling the function to be tested.
                self.assertEqual(sorted_array, expected_output)
    def test_merge_sort(self):
          for input_array, expected_output in test_cases:
            with self.subTest(input_array=input_array): #helps to indentify which test case it failed. 
                sorted_array = merge.merge_sort(input_array)    #calling the function to be tested.
                self.assertEqual(sorted_array, expected_output)
   

    
if __name__ == '__main__':
    unittest.main()