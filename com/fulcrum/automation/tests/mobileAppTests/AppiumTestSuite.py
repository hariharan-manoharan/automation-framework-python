import os
from reusableLibrary.CommonFuntions import MobileReusableFunctions

fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)


class TestSuite1(MobileReusableFunctions):

    def __init__(self, driver, report):
        MobileReusableFunctions.__init__(self,driver, report)
        self.driver = driver
        print 'TestSuite1 constructor is executed...'

    def add_connection(self):
        self.click_element_id('my_connections')
        self.click_element_id('connections_add')
        self.enter_text_id('connection_edit_name','NAME','AIRTEL-WL-QA1-MASTER')
        self.enter_text_id('connection_edit_host', 'HOST', 'services-uswest.skytap.com')
        self.enter_text_id('connection_edit_port', 'PORT', '24624')
        self.click_element_id('connections_save')
        self.click_element_id('action_bar_title')

    def login(self):
        self.enter_text_id('username', 'USERNAME', 'catsadm')
        self.enter_text_id('password', 'PASSWORD', 'catscats11')
        self.click_element_id('remember_me')
        self.driver.hide_keyboard()
        self.click_element_id('btn_connect')
        self.select_user_profile('ADMIN')
        self.select_routine_folder('Receiving')
        self.select_routine('Receiving', 'MRR Receive')


