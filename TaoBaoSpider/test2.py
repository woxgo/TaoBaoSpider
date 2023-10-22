'''
通过搜索获取商品信息
'''

from utils import create_chrome_driver, add_cookies

browser = create_chrome_driver()  # 创建谷歌浏览器对象，通过控制浏览器来访问url
browser.get('https://www.taobao.com')
add_cookies(browser, 'taobao2.json')
# browser.get('https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&s=0')  # 淘宝上的搜索功能必须要登录才能搜索，需要用cookie来亮明身份
# browser.get('https://s.taobao.com/search?q=手机&s=0')
browser.get('https://s.taobao.com/search?q=手机')
#todo 分页待确定如何爬取
#todo 滑块如何处理
