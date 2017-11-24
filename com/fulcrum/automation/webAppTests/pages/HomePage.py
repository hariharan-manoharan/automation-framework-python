import os
from ..reusableLibrary.CommonFuntions import WebReusableFunctions
from ..pageObjectRepository.HomePageObjects import PageObjects
from ..pageObjectRepository.CommonObjects import CommonObjects
import random

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

        serial_number = 'SLN'+str(random.randint(1, 10000))

        self.enter_text_by_xpath(self.xpath_txt_field, 'Serial Number', serial_number)
        self.click_element_xpath(self.xpath_btn.format('Save'), 'Save button')
        self.click_element_xpath(self.xpath_btn_popup_yes, 'Yes button')

        if self.is_element_present('XPATH', self.xpath_div_contains_txt.format('Transaction saved.')):

            self.click_element_xpath(self.xpath_btn_popup_close, 'Close button')
            self.click_element_xpath(self.xpath_link_search_tab, 'Search tab')
            self.enter_text_by_xpath(self.xpath_txt_field, 'Asset Code', 'TA00049040')
            self.click_element_xpath(self.xpath_btn.format('Search'), 'Search button')
            self.click_element_xpath(self.xpath_btn_results_tab_edit_icon, 'Edit icon')

            actual_serial_number = self.get_text_xpath(self.xpath_txt_field, 'Serial Number')

            if actual_serial_number == serial_number:
                self.report.addTestStep('update_serial_number', 'Serial number is updated successfully', 'PASS')
            elif actual_serial_number is None:
                self.report.addTestStep('update_serial_number', 'Given field (Serial Number) is not present in DOM.', 'FAIL')
            else:
                self.report.addTestStep('update_serial_number', 'Serial number is not updated successfully', 'FAIL')

        elif self.is_element_present('XPATH', self.xpath_div_contains_txt.format('ValidationException')):

            self.report.addTestStep('update_serial_number', 'Serial number is not updated successfully. '
                                                            'Exception occurred while submitting transaction', 'FAIL')
