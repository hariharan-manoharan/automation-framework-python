from .pages.LoginPage import *
from .pages.HomePage import *
from .pages.CommonValidations import *
from .reusableLibrary.CustomFuntions import WebCustomFunctions


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

    def click_client_folder(self):
        cf = WebCustomFunctions(self.driver, self.report)
        cf.click_client_folder()

    def verify_export_fun_parts_parts(self):
        cv = CValidations(self.driver, self.report)
        cv.export_fun('Parts','Parts')

    def verify_export_fun_parts_item_types(self):
        cv = CValidations(self.driver, self.report)
        cv.export_fun('Parts','Item Types')

    def verify_clear_grid_fun_parts(self):
        cv = CValidations(self.driver, self.report)
        cv.clear_grid_fun('Parts', 'Parts')

    def verify_refresh_fun_parts(self):
        cv = CValidations(self.driver, self.report)
        cv.refresh_fun('Parts', 'Parts')

    def verify_add_row_fun_parts(self):
        cv = CValidations(self.driver, self.report)
        cv.add_row__fun('Parts', 'Parts')

    def verify_delete_fun_parts(self):
        cv = CValidations(self.driver, self.report)
        cv.delete_fun('Parts', 'Parts')


