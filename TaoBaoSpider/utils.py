import json
from selenium import webdriver

def create_chrome_driver(*, headless=False):  # 创建谷歌浏览器对象，用selenium控制浏览器访问url
    options = webdriver.ChromeOptions()
    options.add_argument('disable-blink-features=AutomationControlled')
    if headless:  # 如果为True，则爬取时不显示浏览器窗口
        options.add_argument('--headless')

    # 做一些控制上的优化
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    # 创建浏览器对象
    # browser = webdriver.Chrome(options=options, executable_path=r"./chromedriver")
    browser = webdriver.Chrome(options=options, executable_path=r"/Users/pengyang/Desktop/WorkSpace/TaoBaoSpider/TaoBaoSpider/chromedriver")
    # 破解反爬措施
    browser.execute_cdp_cmd(
        'Page.addScriptToEvaluateOnNewDocument',
        {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'}
    )

    return browser

def add_cookies(browser, cookie_file):  # 给浏览器对象添加登录的cookie
    with open(cookie_file, 'r') as file:
        cookie_list = json.load(file)
        for cookie_dict in cookie_list:
            if cookie_dict['secure']:
                browser.add_cookie(cookie_dict)