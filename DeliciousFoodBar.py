import json
import urllib.request
from urllib import parse
# import urllib

class Food_Tieba(object):
    """美食吧数据解析"""
    def __init__(self):
        # url 地址和headers头信息
        self.base_url = 'http://tieba.baidu.com/f?'
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
    def write_file(self,data,page):
        print('正在下载第%s页......'% page)
        file_path = 'FoodTieBar/' + str(page) + '页.html'
        with open(file_path,'w') as f:
            f.write(data)

    # 调度数据
    def start_work(self):
        # 贴吧的名字
        tieba_name = input('请输入抓取的贴吧的名字：')
        # 开始的页数
        start_page = int(input('请输入开始页数：'))
        # 结束的页数
        end_page = int(input('请输入结束页数：'))

        # 开启循环
        for page in range(start_page,end_page+1):
            pn = (page-1)*50
            params = {
                "kw":tieba_name,
                "ie":"utf-8",
                "pn":str(pn)
                }
            # params 转换成字符串
            # params_str = json.dumps(params)
            params_str = parse.urlencode(params)
            print(type(params_str))

            # url拼接
            new_url = self.base_url+params_str
            print(new_url)
            # 发送请求
            data = self.send_request(new_url)
            print(data)
            #转码数据
            new_data = data.decode('utf8')
            # 写入数据
            self.write_file(new_data,page)

if __name__ == '__main__':
    foo = Food_Tieba()
    foo.start_work()