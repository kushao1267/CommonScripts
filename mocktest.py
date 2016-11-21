import unittest
import mock
import os
'''
unittest:
	测试类里面的setUp/tearDown会在每个case执行之前/之后执行
	setUpClass/tearDownClass加上@classmethod在整个测试类开始和结束的时候执行
mock:
	模仿第三方服务返回的结果
Coverage:
	shell: coverage [测试文件]  # 获得覆盖率，
	生成html格式的报告，每次运行一个文件都会生成一个.coverage文件，combine所有结果才能得到一个完整的报告
Nose:
	将所有的单元测试文件一次全部执行，能够统计整体的覆盖率.
	扫描目标目录，如果发现目录名以“test”或者“Test”开头，则递归地进去扫描，并自动运行所有发现的以“test”或者“Test”开头的测试文件
区别(下面等价):
	mock.patch('class.attribute')
	mock.patch.object(class,'attribute')
'''


class Calculator(object):
    '''
    被测试类
    '''

    def add(self, a, b):
        return a + b

    def is_error(self):
        try:
            os.mkdir("11")
            return False
        except Exception as e:
            return True


def multiple(a, b):
    '''
    被测试函数
    '''
    return a * b


class TestProducer(unittest.TestCase):
    '''
    测试类
    '''

    def setUp(self):
        self.calculator = Calculator()

    @mock.patch('mocktest.Calculator.add')
    def test_add(self, mock_add):
        mock_add.return_value = 3
        self.assertEqual(self.calculator.add(8, 14), 3)

    @mock.patch('mocktest.multiple')
    def test_multiple(self, mock_multiple):
        mock_multiple.return_value = 3
        self.assertEqual(multiple(8, 14), 3)

    @mock.patch('mocktest.Calculator.add')
    def test_effect(self, mock_add):
        mock_add.side_effect = [1, 2, 3]
        self.assertEqual(self.calculator.add(8, 14), 1)
        self.assertEqual(self.calculator.add(8, 14), 2)
        self.assertEqual(self.calculator.add(8, 14), 3)

    @mock.patch('os.mkdir')
    def test_exception(self, mock_mkdir):
        mock_mkdir.side_effect = Exception
        self.assertEqual(self.calculator.is_error(), False)

    @mock.patch('mocktest.Calculator.add')
    @mock.patch('mocktest.multiple')
    def test_both(self, mock_multiple, mock_add):
        mock_add.return_value = 1
        mock_multiple.return_value = 2
        self.assertEqual(self.calculator.add(8, 14), 1)
        self.assertEqual(multiple(8, 14), 2)

    def tearDown(self):
        print('测试完调用tearDown')


def main():
    unittest.main()


if __name__ == '__main__':
    main()
