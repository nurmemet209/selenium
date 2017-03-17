from selenium import webdriver
import time


# 关闭打开京东时网页欢迎页面
def closeMask(driver):
    try:
        mask = driver.find_element_by_xpath('//*[@id="guide-price"]/div[2]/a')
        mask.click()
    except:
        pass


# 判断京东有无下一页
def hasNextPage(driver):
    try:
        onclick_source = driver.find_element_by_class_name("pn-next").get_attribute("onclick")
        if onclick_source is not None:
            return True
    except:
        return False


# 返回下一页，没有返回None
def getNextPage(driver):
    try:
        onclick_source = driver.find_element_by_class_name("pn-next").get_attribute("onclick")
        return onclick_source
    except:
        return None


def grabData(driver):
    lis = driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
    index = 0
    while True:
        if index < len(lis):
            li = lis[index]
            li.location_once_scrolled_into_view
            # time.sleep(1)
            print("节点%d信息" % index)
            sku = li.get_attribute("data-sku")
            img_ulr = li.find_element_by_xpath('div[1]/div[1]/a[1]/img').get_attribute("src")
            title = li.find_element_by_xpath('div/div[3]/a').text
            price = li.find_element_by_xpath('div/div[2]/strong').text
            print(sku, price, title, img_ulr)
            lis = driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
            print("本页总数据", len(lis))
            index = index + 1
        else:
            break


def scroll2NextPage(driver):
    next = driver.find_element_by_class_name("pn-next")
    driver.execute_script('arguments[0].scrollIntoView({ behavior: "smooth"});', next)


def scrollTop(driver):
    driver.execute_script("$('html, body').animate({scrollTop: 0,scrollLeft:0});")


def start(driver):
    driver.get(
        "https://search.jd.com/Search?keyword=%E8%BD%AE%E6%AF%82&enc=utf-8&wq=%E8%BD%AE%E6%AF%82&pvid=31069b4d12884271b7313b667b002fcf")
    closeMask(driver)
    pageNum = 0
    while True:
        nextPage = getNextPage(driver)
        if nextPage is not None:
            print("当前页码：", pageNum)
            scrollTop(driver)
            driver.execute_script(nextPage)

            time.sleep(5)
            # 抓取数据
            grabData(driver)
            pageNum = pageNum + 1
        else:
            break
    print("quite")

driver = webdriver.Chrome()
start(driver)
