# -*-coding:utf-8-*-
import sys
import scrapy
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from myproj.items import MyprojItem

reload(sys)
sys.setdefaultencoding("utf-8")


class ListSpider(CrawlSpider):
    # 爬虫名称
    name = "myproj"
    # 设置下载延时
    download_delay =3
    # 允许域名
    allowed_domains = ["ss.wedid.us"]
    # 开始URL
    #start_urls = ['http://ss.wedid.us/thread0806.php?fid=7&search=&page=1']
    start_urls=[]
    
    for page in range(1,100): 
        start_urls.append('http://ss.wedid.us/thread0806.php?fid=7&search=&page=%s'%page)
        
    def parse(self, response):
        for sel in response.xpath("//a[contains(@href, 'htm_data')]/@href"):
            detaillink = sel.extract()
            url = 'http://ss.wedid.us/' + detaillink
            yield scrapy.Request(url, callback = self.parse_item)

    #headers = {
    #            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    #}

    #def start_requests(self):
    #    url='http://ss.wedid.us/thread0806.php?fid=7'
    #    yield Request(url,headers=self.headers)

    # 爬取规则,不带callback表示向该类url递归爬取
    #rules = (
    #    Rule(SgmlLinkExtractor(allow=(r'http://ss.wedid.us/htm_data/\d',))),
    #    Rule(SgmlLinkExtractor(allow=(r'http://ss.wedid.us/htm_data/\S*',)), callback='parse'),
    #)

    # 解析内容函数
    def parse_item(self, response):
        item = MyprojItem()

        # 当前URL
        title = response.selector.xpath('//div[@id="main"]/div[@class="t t2"]/table/tr[@class="tr1 do_not_catch"]/th[@height="100%"]/table/tr/td/h4/text()')[0].extract()
        item['name'] = title
        
        #author = response.selector.xpath('//div[@class="t t2"]/table/tr/th/b/text()')[0].extract()
        #item['author'] = author

        #imgurl = response.xpath("//img[contains(@src, '.gif')]/@src")
        #item['imgurl'] = imgurl
        image_urls=[]
        for select in response.xpath("//img[contains(@src, '.gif') and not(contains(@src,'sinaimg')) and  not(contains(@src,'viidii'))]/@src").extract():
            image_urls.append(select)
        item['image_urls']=image_urls

        yield item