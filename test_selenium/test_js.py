from test_selenium.base import Base
import time
import pytest


class TestJS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id('kw').send_keys("selenium")
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        # 滑动到10000像素处
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        time.sleep(3)

    def test_datatime(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        time.sleep(3)
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        time.sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))