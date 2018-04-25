# coding:utf-8
import sys

sys.path.append("D:\www\InterfaceTest")
# sys.path.append("/Volumes/TOSHIBA EXT/PycharmProjects/ImoocInterface/")
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependdentData
from util.send_email import SendEmail
# from util.operation_header import OperationHeader
from util.operation_json import OperetionJson
import sys

type = sys.getfilesystemencoding()


class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.send_mail = SendEmail()

    # 程序执行的主入口
    def go_on_run(self):
        res = None
        pass_count = []
        fail_count = []
        norun_count = []
        # 5 ---> 0, 1, 2, ,3 ,4
        rows_count = self.data.get_case_lines()
        # 行数从 1 开始，第 0 行不用,i 是excle表格的行号
        for i in range(1, rows_count):
            is_run = self.data.get_is_run(i)

            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                # request_data = self.data.get_data_for_json(i)
                data = self.data.get_request_data(i)
                expect = self.data.get_expcet_data(i)
                header = self.data.is_header(i)
                # depend_case = self.data.get_depend_key(i)
                #
                # if depend_case != None:
                #     self.depend_data = DependdentData(depend_case)
                #     # 获取的依赖响应数据
                #     depend_response_data = self.depend_data.get_data_for_key(i)
                #     # 获取依赖的key
                #     depend_key = self.data.get_depend_field(i)
                #     request_data[depend_key] = depend_response_data

                # method, url, data=None, header=None  顺序要一致
                res = self.run_method.run_main(method, url, data, header)

                if self.com_util.is_contain(expect, res):
                    self.data.write_result(i, 'pass')
                    pass_count.append(i)
                    # print 'pass'
                else:
                    self.data.write_result(i, res)
                    fail_count.append(i)
                    # print 'fail'
            else:
                norun_count.append(i)
        pass_num = float(len(pass_count))
        fail_num = float(len(fail_count))
        count_num = pass_num + fail_num
        pass_result = "%.2f%%" % (pass_num / count_num * 100)
        fail_result = "%.2f%%" % (fail_num / count_num * 100)
        print "通过接口：%s个".decode('UTF-8').encode(type) % len(pass_count)
        print "case_id为：%s \n".decode('UTF-8').encode(type) % pass_count
        print "失败接口：%s个".decode('UTF-8').encode(type) % len(fail_count)
        print "case_id为：%s \n".decode('UTF-8').encode(type) % fail_count
        print "未运行接口: %s个".decode('UTF-8').encode(type) % len(norun_count)
        print "case_id为：%s \n".decode('UTF-8').encode(type) % norun_count
        print "通过率为%s, 失败率为%s \n\nclose..".decode('UTF-8').encode(type) % (pass_result, fail_result)
        # self.send_mail.send_main(pass_count, fail_count)


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()
