from Solution import Solution
from timeout_decorator import timeout
import unittest

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = {1: ([1,3,2,4], [3,1,2,4], [0,2,3,4]), 
                            2: ([2,3,1], [3,1,2], [0,1,3]),
                            3: ([1], [1], [1])}
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_case_1(self):
        A, B, output = self.__testcases[1]
        result = self.__obj.findThePrefixCommonArray(A = A, B = B)
        self.assertIsInstance(result, list)
        self.assertTrue(all(r == o for r,o in zip(result, output)))

    @timeout(0.5)
    def test_case_2(self):
        A, B, output = self.__testcases[2]
        result = self.__obj.findThePrefixCommonArray(A = A, B = B)
        self.assertIsInstance(result, list)
        self.assertTrue(all(r == o for r,o in zip(result, output)))

    @timeout(0.5)
    def test_case_3(self):
        A, B, output = self.__testcases[3]
        result = self.__obj.findThePrefixCommonArray(A = A, B = B)
        self.assertIsInstance(result, list)
        self.assertTrue(all(r == o for r,o in zip(result, output)))

if __name__ == '__main__': unittest.main()