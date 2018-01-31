from .pages.LoginPage import *
from .pages.HomePage import *
from .pages.CommonValidations import *


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

    def verify_export_fun_parts_parts(self):
        cv = CValidations(self.driver, self.report)
        cv.export_fun('Parts','Parts')

    def verify_export_fun_parts_item_types(self):
        cv = CValidations(self.driver, self.report)
        cv.export_fun('Parts','Item Types')






