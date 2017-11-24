import os
from ..reusableLibrary.CommonFuntions import WebReusableFunctions
from ..pageObjectRepository.HomePageObjects import PageObjects
from ..pageObjectRepository.CommonObjects import CommonObjects

fileDir = os.path.dirname(os.path.realpath('__file__'))
parentDir = os.path.dirname(fileDir)


class Home(WebReusableFunctions, PageObjects, CommonObjects):

    def __init__(self, driver, report):
        WebReusableFunctions.__init__(self, driver, report)
        PageObjects.__init__(self)
        CommonObjects.__init__(self)

    def update_serial_number(self):
        self.click_data_forms_link()
        self.click_data_form(self.xpath_data_form, 'Assets')
        self.enter_text_by_xpath(self.xpath_txt_field, 'Asset Code', 'TA00049040')
        self.click_element_xpath(self.xpath_btn.format('Search'), 'Search button')
        self.click_element_xpath(self.xpath_btn_results_tab_edit_icon, 'Edit icon')
        self.enter_text_by_xpath(self.xpath_txt_field, 'Serial Number', 'SLN0123')
        self.click_element_xpath(self.xpath_btn.format('Save'), 'Save button')
        self.click_element_xpath(self.xpath_btn_popup_yes, 'Yes button')
        if not self.is_element_present('XPATH', self.xpath_exception_window_title.format('ValidationException')):
            self.click_element_xpath(self.xpath_link_search_tab, 'Search tab')
        else:
            self.report.addTestStep('update_serial_number', 'Serial number is not updated successfully', 'FAIL')
