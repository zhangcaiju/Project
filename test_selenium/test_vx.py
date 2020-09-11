import shelve
from time import sleep

import pytest

from test_selenium.base import Base


class TestVx(Base):
    @pytest.mark.skip
    def test_get_cookie(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851241085805'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': '4-YetULTTd6MHFV7Jg0s7047oeUvuc1_vWDBJvq1K16U49TQHaluw9Z0P3TLAm0NctBtAs_nLiQTNwQ5-IfDIQmLYwSvU5XA0jAuu0EM5J0TQAszUSc7BO-E3NK_lf4Y6vOpsn4nqpjfamFyp5p3y7ja85MJYDCHdYLGOC_Z-_XfFgQAtaDsJDuTKMS0D4Z-tb3GXzbY7V53NSzf6HtDx1JtUMaLG2O93k84w1jVPVLlRHjzlJTW_JmnG8LtfK4JqXw5HXy36gwuI0XyzgPxsg'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851241085805'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324947154591'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': '1zfMdxxsdQab4zM4XzkYMgxuJWHPE0sdBO4B2GRip9bFq_5oMqH_YI-lypu18LfN'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a3145823'},
            {'domain': '.qq.com', 'expiry': 1599570323, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '358152050201194'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1631105817, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1597978252,1597991066,1599567524,1599569817'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 1599656695, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.537165184.1599567533'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1599599059, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '297b88j'},
            {'domain': '.qq.com', 'expiry': 1914915073, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': False, 'value': '1d7ff5a0ed0ace1d'},
            {'domain': '.qq.com', 'expiry': 1631091073, 'httpOnly': False, 'name': 'eas_sid', 'path': '/',
             'secure': False, 'value': 'D1C5W939F515t5n0f7t330y3p2'},
            {'domain': '.qq.com', 'expiry': 1912665776, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': False, 'value': '0_640c65c77fcfc'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'sameSite': 'None', 'secure': True, 'value': '1256357540'},
            {'domain': '.qq.com', 'expiry': 1662642295, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1918874628.1597235604'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1628771597, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1602162297, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh-cn'}]
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[2]').click()
        self.driver.find_element_by_id('js_upload_file_input').send_keys(
            "C:\\Users\\zhangcaiju_v\Desktop\人群\\tongxunlu.xlsx")
        assert 'tongxunlu.xlsx' == self.driver.find_element_by_id('upload_file_name').text
        sleep(3)

    # shelve是python内置函数，相当于一个小型的数据库
    def test_shelve(self):
        # 打开或者创建一个shelve对象，默认支持读写操作
        db = shelve.open('./mydbs/cookies')
        # db['cookie'] = cookies
        #同步并关闭shelve对象
        # db.close()
        cookies = db['cookie']
        # print(cookies)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[2]').click()
        self.driver.find_element_by_id('js_upload_file_input').send_keys(
            "C:\\Users\\zhangcaiju_v\Desktop\人群\\tongxunlu.xlsx")
        assert 'tongxunlu.xlsx' == self.driver.find_element_by_id('upload_file_name').text
        sleep(3)

