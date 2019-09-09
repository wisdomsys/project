import unittest


class UnittestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("所有case执行之前的前提条件\n")

    @classmethod
    def tearDownClass(cls) -> None:
        print("所有case执行之后的后置条件\n")

    def setUp(self) -> None:
        print("...case 的前置条件...\n")

    def tearDown(self) -> None:
        print("...case 的后置条件...\n")

    def test_case001(self):
        print("这是第1条case")

    # 跳过测试用例的执行，即使在容器中添加了测试用例也可以被跳过
    @unittest.skip
    def test_case002(self):
        print("这是第2条case")

    def test_case003(self):
        print("这是第3条case")


if __name__ == "__main__":
    # unittest.main()
    # 创建unittest的容器
    suite = unittest.TestSuite()
    # 添加测试用例到容器
    suite.addTest(UnittestCase("test_case002"))
    suite.addTest(UnittestCase("test_case001"))
    suite.addTest(UnittestCase("test_case003"))
    # 执行容器里的测试用例
    unittest.TextTestRunner().run(suite)
