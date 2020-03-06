import unittest

def addition(a,b):
    return a+b


class AdditionTest(unittest.TestCase):

    def testAdditionEntier(self):
        res = addition(1,1)
        self.assertEqual(res, 3)
        print("eee")

    def testAdditionDec(self):
        res = addition(1.1,1.1)
        self.assertEqual(res, 2.2)


if __name__ == '__main__':
    print("eeess")
    unittest.main()
