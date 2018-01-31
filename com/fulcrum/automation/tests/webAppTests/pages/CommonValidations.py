from com.fulcrum.automation.framework.reportFactory.StatusEnum import Status
from ..pageObjectRepository.CommonObjects import CommonObjects
from ..pageObjectRepository.HomePageObjects import PageObjects
from ..reusableLibrary.CommonFuntions import WebReusableFunctions
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CValidations(WebReusableFunctions, PageObjects, CommonObjects):

    def __init__(self, driver, report):
        WebReusableFunctions.__init__(self, driver, report)
        PageObjects.__init__(self)
        CommonObjects.__init__(self)


    def export_fun(self, data_form_folder, data_form):
        self.click_element_xpath(self.xpath_client_folder, "Client Folder")
        self.click_element_xpath(self.xpath_dataform_folder.format(data_form_folder), data_form_folder+' Folder')
        self.click_data_form(self.xpath_data_form, data_form)
        self.click_element_xpath(self.xpath_btn.format('Search'), 'Search button')

        if self.wait_until_element_is_present('XPATH','//div[@class=\'blocking-screen\']'):
            check_boxes = self.driver.find_elements_by_xpath(self.xpath_edit_tab_record_checkbox)
            total_records = len(check_boxes)
            for i in range(0,len(check_boxes)):

                check_boxes[i].click()

                self.report.addTestStep('Click checkbox', 'Record ' + str(i+1) + ' is selected', Status.PASS)

                if i == 3:
                    break

            self.click_element_xpath(self.xpath_btn.format('Export'), 'Export button')

            if self.wait_until_element_is_present('XPATH', '//div[@class=\'blocking-screen\']'):
                self.report.addTestStep('Export', 'Export pop-up is displayed', Status.PASS)

