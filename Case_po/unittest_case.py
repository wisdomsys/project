import unittest


class FirstCase01(unittest.TestCase):
    def setUp(self):
        print("这是case的前置条件")

    def tearDown(self):
        print("这是case的后置条件")

    def testfirst01(self):
        print("这是第一个case")

    def testfirst02(self):
        print("这是第二个case")


if __name__ == '__main__':
    unittest.main()
