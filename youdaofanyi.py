# coding = utf-8

import requests
from lxml import etree

'''
    This is  the mobile phone  page
'''

class Youdaofanyi:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) \
                AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
        self.url = "https://m.youdao.com/translate"

    # 定义一个接收用户输入内容的方法，puttext为接收的参数
    def parse_url(self, puttext):
        udata = {}
        udata["inputtext"] = puttext
        udata["type"] = "AUTO"
        response = requests.post(self.url, headers=self.headers, data=udata)
        return response.content.decode()

    def printTxt(self):
        while True:
            put_text = input("请输入要翻译的文本：")
            html = self.parse_url(put_text)
            txt_etree = etree.HTML(html)
            txt = txt_etree.xpath("//*[@id='translateResult']/li/text()")[0]
            print("翻译文本：%s\n翻译结果：%s" % (put_text, txt))
            print("*"*20)

if __name__ == '__main__':
    yd = Youdaofanyi()
    yd.printTxt()