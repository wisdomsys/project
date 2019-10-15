import unittest
import os


class RunCase(unittest.TestCase):

    def test_case01(self):
        # os.getcwd()：返回当前进程的工作目录
        case_path = os.path.join(os.getcwd())
        print(os.getcwd())
        print(case_path)
        suite = unittest.defaultTestLoader.discover(case_path, 'unittest_*.py')
        unittest.TextTestRunner().run(suite)


if __name__ == "__main__":
    unittest.main()
