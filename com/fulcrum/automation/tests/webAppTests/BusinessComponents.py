from .pages.LoginPage import *
from .pages.HomePage import *


class BusinessComp:

    def __init__(self, driver, report):
        self.driver = driver
        self.report = report

    def login(self):
        login = Login(self.driver, self.report)
        login.login()

    def update_serial_number(self):
        home = Home(self.driver, self.report)
        home.update_serial_number()



