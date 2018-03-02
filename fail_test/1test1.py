from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('http://www.baidu.com')  # 加载网页
data = driver.page_source  # 获取网页文本
driver.save_screenshot('1.png')  # 截图保存
print(data)
driver.quit()