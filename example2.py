import unittest

class MyApp2(unittest.TestCase):


    def test_case3(self):
        self.assestEqual("helloworld", "hello")

class MyApp(unittest.TestCase):

    def test_case1(self):
        a=10
        b=22
        c=a+b
        self.assetEqual(32, c)

    def test_case2(self):
        self.assertNotEqual("hello", "hai")

if __name__=="__main__":
    unittest.main()