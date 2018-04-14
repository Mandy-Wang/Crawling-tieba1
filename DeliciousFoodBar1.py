import json
import urllib.request
from urllib import parse
# import urllib
from lxml import etree


class Food_Tieba(object):
    """美食吧数据解析"""
    def __init__(self):
        # url 地址和headers头信息
        self.base_url = 'http://tieba.baidu.com/f?'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        # 第一层解析 url 注意浏览器的xpath插件 只是辅助，自动过滤空格
        self.first_url = '//div[@class="t_con cleafix"]/div/div/div/a/@href'
        # 第二层解析url
        self.second_url = '//img[@class="BDE_Image"]/@src'


    def send_request(self,url):
        # 创建请求对象
        request = urllib.request.Request(url,headers=self.headers)
        # 发送请求，获取响应 读取数据
        response = urllib.request.urlopen(request)
        data = response.read()
        # 返回数据
        return data



    # 写入数据
    def write_file(self,data,imagename):
        print(imagename)
        file_path = './images/'+imagename
        print(file_path)
        with open(file_path,'w') as f:
            f.write(data)

    # 解析数据data,解析规则xpathStr
    def analysis_data(self,data,xpathStr):
        # 1转换 类型 可解析的类型
        html_data =etree.HTML(data)
        # 2解析
        result_list =html_data.xpath(xpathStr)
        return result_list
    # 调度数据
    def start_work(self):
        # # 贴吧的名字
        # tieba_name = input('请输入抓取的贴吧的名字：')
        # # 开始的页数
        # start_page = int(input('请输入开始页数：'))
        # # 结束的页数
        # end_page = int(input('请输入结束页数：'))

        # 开启循环
        # for page in range(start_page,end_page+1):
        #     pn = (page-1)*50
            params = {
                "kw":'美食吧',# tieba_name,
                "ie":"utf-8",
                "pn": 50 # str(pn)
                }
            params_str = parse.urlencode(params)
            # print(type(params_str))

            # url拼接
            new_url = self.base_url+params_str

            # 发送请求
            data = self.send_request(new_url)
            # 第二层分析 获取每一个子链接 发送请求
            link_list = self.analysis_data(data,self.first_url)
            for link in link_list:
                child_url = 'http://tieba.baidu.com/' + link
                # print(child_url)

                # 发送二次请求
                first_data = self.send_request(child_url)

                # 第三次分析 发送第三次请求 获取图片url 发送图片的请求
                link_first = self.analysis_data(first_data,self.second_url)
                # http://imgsrc.baidu.com/forum/w%3D580/sign=cc624ee183d6277fe912323018391f63/
                # 7b43fbf2b2119313fb1d25ea61380cd791238d0a.jpg'
                # print(link_first)
                for image_url in link_first:
                    # print(image_url)
                    # 遍历获取图片  imge_data 是发送请求得到的数据，用于写入数据
                    image_data = self.send_request(image_url)
                    print(image_data)
                    # 给每一张图片取一个名字
                    image_name = image_url[-10:]
                    # print(image_name)
                    print(type(image_data))
                    print(image_data)
                    # 写入数据
                    self.write_file(image_data,image_name)

if __name__ == '__main__':
    foo = Food_Tieba()
    foo.start_work()