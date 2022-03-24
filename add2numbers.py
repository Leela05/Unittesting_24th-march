import unittest

def add(x,y):
    return x+y

class Myapp2(unittest.TestCase):
    def test_case_add(self):
         a=12
         b=22
         c=add(a,b)
         self.assetEqual(a+b,c)

    def test_case_add1(self):
        a=12.34
        b=34.5
        c=add(a,b)
        self.assetEqual(c,a+b)

if __name__=="__main__":
    unittest.main()