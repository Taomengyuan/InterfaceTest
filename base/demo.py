# coding:utf-8
__author__ = 'Xu'
# 'Xu'
import requests


class RunMain:
    def send_get(self, url, data):
        res = requests.get(url=url, data=data).json()
        return res

    def send_post(self, url, data):
        res = requests.post(url=url, data=data).json()
        return res

    def run_main(self, url, method, data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res

# if __name__ == '__main__':
#     url = 'http://coding.imooc.com/api/testcdn'
#     data = {

#     }
#     run = RunMain(url, 'GET', data)
#     print run.res
