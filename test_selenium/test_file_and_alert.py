import time

import pytest

from test_selenium.base import Base

from selenium.webdriver import ActionChains


class TestFile(Base):
    @pytest.mark.skip
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        time.sleep(3)
        self.driver.find_element_by_id('stfile').send_keys('C:\\Users\zhangcaiju_v\Pictures\984x288.jpg')


class TestAlert(Base):
    def test_alert(self):
        self.driver.get('http://runoob.com/try/try.php?filename=jqueryui-api-droppable')
        # 切换到frame
        self.driver.switch_to.frame('iframeResult')
        action = ActionChains(self.driver)
        # 拖拽元素
        drag = self.driver.find_element_by_id('draggable')
        drop = self.driver.find_element_by_id('droppable')
        action.drag_and_drop(drag, drop).perform()
        # 切换到alert弹框，点击接受
        self.driver.switch_to_alert().accept()
        # 切换到默认页面
        self.driver.switch_to_default_content()
        self.driver.find_element_by_id('submitBTN').click()
        time.sleep(3)
