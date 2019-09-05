import unittest

class FirstCase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("所有case执行之前的前置")
    @classmethod
    def tearDownClass(cls) -> None:
        print("所有case执行之后的后置")

    def testfirst01(self):
        print("这是第一条case")

    def testfirst02(self):
        print("这是第二条case")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(FirstCase01('testfirst01'))
    unittest.TextTestRunner().run(suite)
