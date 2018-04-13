# coding:utf-8
__author__ = 'Xu'


# 'Xu'

class CommonUtil:
    def is_contain(self, str_one, str_two):
        '''
        判断一个字符串是否在另一个字符串中
        str_one 为查找的字符串
        str_two 为被查找的字符串
        :return:
        '''
        flag = None
        if isinstance(str_one, unicode):
            str_one = str_one.encode('unicode-escape').decode('string_escape')
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag
