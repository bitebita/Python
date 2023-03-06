import scrapy


class TongchengSpider(scrapy.Spider):
    name = 'tongcheng'
    # allowed_domains = ['sjz.58.com']
    allowed_domains = ['sjz.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&button=%E6%90%9C%C2%A0%E7%B4%A2']
    # start_urls = ['http://sjz.58.com/']
    start_urls = ['http://sjz.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&button=%E6%90%9C%C2%A0%E7%B4%A2/']



    def parse(self, response):
        # print('山东菏泽')

        # response.text 返回字符串
        # content = response.text

        # response.body 返回二进制数据
        # content = response.body

        # print('_____________________________________________________________')
        # print(content)

        # 返回一个空列表 []
        # span = response.xpath('//div[@id="filter"]/div[@class="tabs"]/a/span')[0]
        # 出现错误：IndexError: list index out of range
        # span = response.xpath('//div[@id="filter"]/div[@class="tabs"]/a/span')
        # 出现错误：IndexError: list index out of range
        # span = response.xpath('//div[@id="filter"]/div[@class="tabs"]/a[@class="select"]/span')
        # IndexError: list index out of range

        # 超过list范围原因是在这个网站的HTML代码中有的标识为空，只要加上try...except错误机制，跳过空值就行了
        try:
            span = response.xpath('/html/body/div[@id="filter"]/div[@class="tabs"]/a[@class="select"]/span')
            print("****************************************")
            print(span)
            # print(span.extract())
        except:
            print("跳过空值")
