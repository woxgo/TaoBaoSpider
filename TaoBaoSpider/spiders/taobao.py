import os
import sys

import scrapy
from scrapy.cmdline import execute
from scrapy import Request,Selector

from TaoBaoSpider.items import TaospiderItem


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']

    def start_requests(self):
        keywords = ['手机', '笔记本电脑', '键鼠套装']
        for keyword in keywords:
            for page in range(1):
                # url = f'https://s.taobao.com/search?q={keyword}&s={48 * page}'
                url = f'https://s.taobao.com/search?q={keyword}'
                yield Request(url=url)

    # def parse_detail(self, response, **kwargs):
    #     pass

    def parse(self, response, **kwargs):  # 淘宝的数据是通过js动态渲染出来的，不是静态内容，通过选择器拿不到，我们要通过selenium帮助我们拿到,在数据管道中实现
        sel = Selector(response)
        # todo 卡滑块了
        selectors = sel.css('div.items > div.item.J_MouserOnv erReq > div.ctx-box.J_MouseEneterLeave.J_IconMoreNew')
        for selector in selectors:  # type: Selector
            item = TaospiderItem()
            item['title'] = ''.join(selector.css('div.row.row-2.title > a::text').extract()).strip()
            item['price'] = selector.css('div.row.row-1.g-clearfix > div.price.g_price.g_price-highlight > strong::text').extract_first().strip()
            item['deal_count'] = selector.css('div.row.row-1.g-clearfix > div.deal-cnt::text').extract_first().strip()
            item['shop'] = selector.css('div.row.row-3.g-clearfix > div.shop > a > span:nth-child(2)::text').extract_first().strip()
            item['location'] = selector.css('div.row.row-3.g-clearfix > div.location::text').extract_first().strip()
            yield item

if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    execute(['scrapy', 'crawl', 'taobao'])
    # execute(['scrapy', 'crawl', 'douban', '-o', 'douban.csv'])
    # execute(['scrapy', 'crawl', 'douban', '--nolog'])