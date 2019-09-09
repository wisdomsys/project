import unittest


class FirstCase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("所有case执行之前的前置")

    @classmethod
    def tearDownClass(cls) -> None:
        print("所有case执行之后的后置")

    def setUp(self) -> None:
        print("...case 的前置条件...\n")

    def tearDown(self) -> None:
        print("...case 的后置条件...\n")

    # @unittest.skip("不执行第一条")
    def test_first01(self):
        print("这是第01条case")

    def test_first02(self):
        print("这是第02条case")

    def test_first03(self):
        print("这是第03条case")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(FirstCase01('test_first02'))
    suite.addTest(FirstCase01('test_first03'))
    suite.addTest(FirstCase01('test_first01'))
    unittest.TextTestRunner().run(suite)
