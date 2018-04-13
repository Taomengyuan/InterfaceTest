# coding:utf-8
class global_var:
    Id = '0'  # id
    request_name = '1'  # 模块
    url = '2'  # url
    run = '3'  # 是否运行
    request_way = '4'  # 请求类型
    header = '5'  # 是否携带header
    case_depend = '6'  # case依赖
    data_depend = '7'  # 依赖的返回数据
    field_depend = '8'  # 数据依赖字段
    data = '9'  # 请求数据
    expect = '10'  # 预期结果
    result = '11'  # 实际结果


def get_id():
    return global_var.Id


def get_url():
    return global_var.url


def get_run():
    return global_var.run


def get_run_way():
    return global_var.request_way


def get_header():
    return global_var.header


def get_case_depend():
    return global_var.case_depend


def get_data_depend():
    return global_var.data_depend


def get_field_depend():
    return global_var.field_depend


def get_data():
    return global_var.data


def get_expect():
    return global_var.expect


def get_result():
    return global_var.result


def get_header_value():
    header = {
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.4.1",
        "Content-Length": "22",
        "Content-Type": "application/json;charset=utf-8",
        "Connection": "Keep-Alive",

    }
    return header
