# *-* code:utf-8 *-*
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from xiaomihr.items import XiaomihrItem

class XiaomihrSpider(CrawlSpider):
    name = "xiaomihr"
    # download_delay = 1
    allowed_domains = ["xiaomi.com"]
    start_urls = ["http://hr.xiaomi.com/job/list"]

    rules = [
        Rule(LinkExtractor(allow=('job/view/\d+')), follow=False, callback='parse_item'),
        Rule(LinkExtractor(allow=('job/list/0-0-2-0-\d{,3}',),restrict_xpaths=('//a[@class="numbers last"]')), follow=True)
    ]

    def parse_item(self, response):
        self.logger.info('Now is spidering in this page:   %s', response.url)
        # base = response.xpath('//div[@class="bd bd-table-list"]/div[1]/table/tbody/tr')
        base = response.xpath('//table[@class="job-information"]')
        for sel in base:

            item = XiaomihrItem()
            item['work'] = sel.xpath('tr[1]/td[2]/text()').extract()
            item['location'] = sel.xpath('tr[1]/td[4]/text()').extract()
            item['hr_way'] = sel.xpath('tr[2]/td[4]/text()').extract()
            item['worktype'] = sel.xpath('tr[2]/td[2]/text()').extract()
            item['duty'] = sel.xpath('tr[3]/td[2]/div/text()').extract()
            item['requirement'] = sel.xpath('tr[4]/td[2]/div/text()').extract()
        #     item['work'] = sel.xpath('td[1]/a/text()').extract()
        #     item['worktype'] = sel.xpath('td[2]/text()').extract()
        #     item['location'] = sel.xpath('td[3]/text()').extract()
        #     item['detail_link'] = sel.xpath('td[1]/a/@href').extract()
            yield item

        

