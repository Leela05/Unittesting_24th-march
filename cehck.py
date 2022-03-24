import unittest

class Mytest(unittest.TestCase):
    def test_check_divisible(x):
        if x % 7 == 0:
            return True
        else:
            return False

class checkDivisible(unittest.TestCase):
    def test_case1(self):
        result = checkDivisible(7)
        self.assertTrue(result)

if __name__=="__main__":
    unittest.main()