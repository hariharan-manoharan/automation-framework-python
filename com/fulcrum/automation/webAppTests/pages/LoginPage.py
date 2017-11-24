import os
from ..reusableLibrary.CommonFuntions import WebReusableFunctions
from ..pageObjectRepository.LoginPageObjects import PageObjects

fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)


class Login(WebReusableFunctions, PageObjects):

    def __init__(self, driver, report):
        WebReusableFunctions.__init__(self, driver, report)
        PageObjects.__init__(self)

    def login(self):
        self.get_url('https://172.16.32.38:8443/cats/login', 'CATS CenterPoint:')
        self.enter_text_id(self.id_txt_user_name, 'User name', 'catsadm')
        self.enter_text_id(self.id_txt_password, 'Password' , 'catscats11')
        self.click_element_id(self.id_btn_login, 'Login Button')






