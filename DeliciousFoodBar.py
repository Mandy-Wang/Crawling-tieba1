import urllib.request
import urllib

class Food_Tieba(object):
    """美食吧数据解析"""
    def __init__(self):
        # url 地址和headers头信息
        self.base_url = 'http://tieba.baidu.com/f?ie=utf-8&kw=%E7%BE%8E%E9%A3%9F&fr=search&red_tag=e0910316858'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}


    def send_request(self,url):
        # 创建请求对象
        request = urllib.request.Request(url,headers=self.headers)
        # 发送请求，获取响应 读取数据
        response = urllib.request.urlopen(request)
        data = response.read()
        # 返回数据
        return data

    # 写入数据
    def write_file(self,data):
        with open('Food1.html','w') as f:
            f.write(data)

    # 调度数据
    def start_work(self):
        # 发送请求
        data = self.send_request(self.base_url)
        print(data)
        #转码数据
        new_data = data.decode('utf8')
        # 写入数据
        self.write_file(new_data)

if __name__ == '__main__':
    foo = Food_Tieba()
    foo.start_work()