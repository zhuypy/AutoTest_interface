
__author__ = 'zhuy'

import os,sys
import unittest,requests,ddt
from config import setting
from lib.readexcel import ReadExcel
from lib.sendrequests import SendRequests
from lib.writeexcel import WriteExcel

testData = ReadExcel(setting.SOURCE_FILE, "Sheet1").read_data()
print(testData)
@ddt.ddt
class DemoTest(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        pass

    def tearDown(self):
        pass

    @ddt.data(*testData)
    def test_justTest(self,data):
        # 获取ID字段数值，截取结尾数字并去掉开头0
        rowNum = int(data['ID'].split("_")[2])
        print("******* 正在执行用例 ->{0} *********".format(data['ID']))
        print("请求方式: {0}，请求URL: {1}".format(data['method'], data['url']))
        print("请求参数: {0}".format(data['params']))
        print("post请求body类型为：{0} ,body内容为：{1}".format(data['type'], data['body']))
        # 发送请求
        re = SendRequests().sendRequests(self.s, data)
        # 获取服务端返回的值
        self.result = re.json()
        # 获取excel表格数据的状态码和消息
        print(self.result)
        print(re.status_code)

        readData_code = int(data["status_code"])
        readData_msg = data["msg"]
        if readData_code == self.result['state'] and readData_msg == self.result['msg']:
            OK_data = "PASS"
            print("用例测试结果:  {0}---->{1}".format(data['ID'], OK_data))
            WriteExcel(setting.TARGET_FILE).write_data(rowNum + 1, OK_data)
        if readData_code != self.result['state'] or readData_msg != self.result['msg']:
            NOT_data = "FAIL"
            print("用例测试结果:  {0}---->{1}", format(data['ID'], NOT_data))
            WriteExcel(setting.TARGET_FILE).write_data(rowNum + 1, NOT_data)
        self.assertEqual(self.result['state'], readData_code, "返回实际结果是->:%s" % self.result['state'])
        self.assertEqual(self.result['msg'], readData_msg, "返回实际结果是->:%s" % self.result['msg'])

if __name__ == '__main__':
    unittest.main()















