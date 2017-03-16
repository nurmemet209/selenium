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
            time.sleep(1)
            print("节点%d信息" % index)
            sku=li.get_attribute("data-sku")
            img_ulr = li.find_element_by_xpath('div[1]/div[1]/a[1]/img').get_attribute("src")
            title = li.find_element_by_xpath('div/div[3]/a').text
            price = li.find_element_by_xpath('div/div[2]/strong').text
            print(sku,price, title, img_ulr)
            lis = driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
            print("本页总数据",len(lis))
            index = index + 1
        else:
            break


def scroll2NextPage(driver):
    next = driver.find_element_by_class_name("pn-next")
    driver.execute_script('arguments[0].scrollIntoView({ behavior: "smooth"});', next)

def scrollTop(driver):
    driver.execute_script("$('html, body').animate({scrollTop: 0,scrollLeft:0});")

def start(driver):
    driver.get("https://search.jd.com/Search?keyword=%E8%BD%AE%E6%AF%82&enc=utf-8&wq=%E8%BD%AE%E6%AF%82&pvid=31069b4d12884271b7313b667b002fcf")
    closeMask(driver)
    pageNum=0
    while True:
        nextPage = getNextPage(driver)
        if nextPage is not None:
            print("当前页码：",pageNum)
            scrollTop(driver)
            driver.execute_script(nextPage)

            time.sleep(10)
            # 抓取数据
            grabData(driver)
            pageNum = pageNum + 1
        else:
            break
    print("quite")


driver = webdriver.Chrome()

start(driver)
# print(pre_1.find_element_by_class_name("disabled"))
# grabJd(driver)

# driver.page_source.encode('gbk', 'ignore')
# 返回html页面

# driver.execute_script("arguments[0].scrollIntoView(true);",a)
# 滚动浏览器到a元素可见,arguments[0]是传过去的参数a

# driver.execute_script("SEARCH.page(3, true)")
# 执行页面的js函数

# onclick_source= driver.find_element_by_class_name("pn-next").get_attribute("onclick")
# print("has next page",onclick_source)
# driver.execute_script(onclick_source)
# 获取 下一页的js代码并执行

# driver.execute_script("$('html, body').animate({scrollTop: 20000,scrollLeft:0},60000,'linear');")
# 60000 速度 ,leaner 变换方式

# lis=driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
# for li in lis:
#      li 节点下寻找 div[1]/div[1]/a[1]/img 注意前面没有斜杠
#     img_ulr=li.find_element_by_xpath('div[1]/div[1]/a[1]/img').get_attribute("src")
#     print(img_ulr)

# img_ulr=li.find_element_by_xpath('div[1]/div[1]/a[1]/img').get_attribute("src")
# 获取img元素的src属性的值

# time.sleep(30)
# 线程睡眠30秒


# lis = driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
# for li in lis:
#     # 滚动节点到可见区域,注意，location_once_scrolled_into_view后面没有括号
#     li.location_once_scrolled_into_view
#     time.sleep(1)
#     img_ulr = li.find_element_by_xpath('div[1]/div[1]/a[1]/img').get_attribute("src")
#     print(img_ulr)

# title = li.find_element_by_xpath('div/div[3]/a').text
