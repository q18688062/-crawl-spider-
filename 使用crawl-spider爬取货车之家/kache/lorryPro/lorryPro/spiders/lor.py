# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from lorryPro.items import LorryproItem, Lorrypro_detail

class LorSpider(CrawlSpider):
    name = 'lor'
    # allowed_domains = ['www.xxx.com']
    #爬取卡车之家首页
    start_urls = ['https://product.360che.com/price/c1_s64_b0_s0.html']
    #页面的链接提取器
    link = LinkExtractor(allow=r'c1_s64_b0_s0_c\d+\.html')
    #详情的链接提取器
    link_detail = LinkExtractor(allow=r'\/s.*?_index\.html')
    rules = (
        Rule(link, callback='parse_item', follow=True),
        Rule(link_detail, callback='parse_detail'),
    )

    def parse_item(self, response):
        li_list = response.xpath('//*[@id="productList"]/li')
        for li in li_list:
            name = li.xpath('./div[1]/div[1]/h2/a/text()').extract_first()  #车辆名称
            price = li.xpath('./div[1]/span/em/a/text()').extract_first() #价格 单位万元
            engi = li.xpath('./div[1]/div[2]/p[1]/a/text()').extract()
            engine = '/'.join(engi)  #发动机
            gear_bo = li.xpath('./div[1]/div[2]/p[3]/text()').extract_first() #变速箱
            gear_box = gear_bo.replace('\n', '/')
            carr_leng = li.xpath('./div[1]/div[2]/p[5]/a/text()').extract()
            carr_length = '/'.join(carr_leng)  #货箱长度
            drive = li.xpath('./div[1]/div[2]/p[2]/a/text()').extract()
            tf_drive = '/'.join(drive)  #驱动形式
            carr_s = li.xpath('./div[1]/div[2]/p[4]/text()').extract_first()  #货箱形式
            carr_st = carr_s.replace('\n', '/')
            emiss_stand = li.xpath('./div[1]/div[2]/p[6]/a/text()').extract()
            emiss_standard = '/'.join(emiss_stand)   #车辆排放标准
            item = LorryproItem()
            item['name'] = name.replace(' ','')
            item['price'] = price.replace(' ','') if price else ''
            item['engine'] = engine.replace(' ','')
            item['gear_box'] = gear_box.replace(' ','')
            item['carr_length'] = carr_length.replace(' ','')
            item['tf_drive'] = tf_drive.replace(' ','')
            item['carr_st'] = carr_st.replace(' ','')
            item['emi'] = emiss_standard.replace(' ','')
            yield item

    def parse_detail(self, response):
        car_name = response.xpath('/html/body/div[4]/div[4]/h1/a/text()').extract_first()
        if car_name:
            item = Lorrypro_detail()
            item['name'] = car_name.replace(' ', '')
            li_list = response.xpath('/html/body/div[4]/div[6]/div[1]/div[3]/div[2]/ul/li')

            for li in li_list:
                detail_url = 'https://product.360che.com'+li.xpath('./a/@href').extract_first()

                yield scrapy.Request(detail_url, callback=self.parse_pic, meta={'item': item})

    def parse_pic(self, response):
        item = response.meta['item']
        pic_url = response.xpath('//*[@id="imgid"]/@src').extract_first()

        item['pic'] = pic_url.replace(' ', '')

        yield item




