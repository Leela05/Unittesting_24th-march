import unittest

def Largest_of_twonum(x,y):
    if x > y:
        return True
    else:
        return False

class Check_Largest_num(unittest.TestCase):
    def test_largest_1(self):
        number1 = 10
        number2 = 20
        result = Largest_of_twonum(number1, number2)
        self.assertTrue(number2)

    def test_largest_2(self):
        num1 = 20
        num2 = 10
        result = Largest_of_twonum(num1, num2)
        self.assertTrue(num1)

if __name__ == "_main_":
        unittest.main()