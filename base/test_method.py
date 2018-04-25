# coding:utf-8
import unittest
from demo import RunMain
import HTMLTestRunner
from mock_demo import mock_test
import sys


class TestMethod(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()

    def test_03(self):
        url = ''
        data = {
            'timestamp': '1507034803124',
            'uid': '5249191',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0',
            'errorCode': 1001,
        }
        res = mock_test(self.run.run_main, data, url, 'POST', data)
        # print res
        # 不是xxxx的话 测试失败
        self.assertEqual(res['errorCode'], 1001, '测试失败')
        print '这是第一个case'

    # @unittest.skip('test_02') #←---跳过 xxx 用例
    def test_02(self):
        url = ''
        data = {
            'timestamp': '1507034803124',
            'uid': '5249192',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0'
        }
        res = self.run.run_main(url, 'POST', data)
        # print res
        # 不是xxxx的话 测试失败
        self.assertEqual(res['errorCode'], 1000, '测试失败')
        print '这是第二个case'


if __name__ == '__main__':
    filepath = '../report/htmlreport.html'
    fp = file(filepath, 'wb')
    # 容器
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_02'))
    suite.addTest(TestMethod('test_03'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='this is first report')
    # runner.run(suite)
    unittest.TextTestRunner().run(suite)
