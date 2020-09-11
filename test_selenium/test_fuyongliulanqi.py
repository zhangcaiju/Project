from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestFuyong():
    def test_fuyongliulanqi(self):
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        driver = webdriver.Chrome(options=option)
        driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()