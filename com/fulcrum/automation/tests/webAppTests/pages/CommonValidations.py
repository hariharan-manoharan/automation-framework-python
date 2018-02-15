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

    def clear_grid_fun(self, data_form_folder, data_form):
        self.click_element_xpath(self.xpath_client_folder, "Client Folder")
        self.click_element_xpath(self.xpath_dataform_folder.format(data_form_folder), data_form_folder + ' Folder')
        self.click_data_form(self.xpath_data_form, data_form)
        self.click_element_xpath(self.xpath_btn.format('Search'), 'Search button')

        if self.wait_until_element_is_present('XPATH', '//div[@class=\'blocking-screen\']'):
            check_boxes = self.driver.find_elements_by_xpath(self.xpath_edit_tab_record_checkbox)

            if  len(check_boxes) > 0:
                self.click_element_xpath(self.xpath_btn.format('Clear Grid'), 'Clear Grid button')
                self.click_element_xpath_1(self.xpath_btn_popup_clear, 'Pop-up Clear button')

                if not self.is_element_present('XPATH',self.xpath_edit_tab_record_checkbox):
                    self.report.addTestStep('Clear Grid', 'Clear is working as expected', Status.PASS)
                else:
                    self.report.addTestStep('Clear Grid', 'Clear is not working as expected', Status.FAIL)

    def refresh_fun(self, data_form_folder, data_form):
        self.click_element_xpath(self.xpath_client_folder, "Client Folder")
        self.click_element_xpath(self.xpath_dataform_folder.format(data_form_folder), data_form_folder + ' Folder')
        self.click_data_form(self.xpath_data_form, data_form)
        self.click_element_xpath(self.xpath_btn.format('Search'), 'Search button')

        if self.wait_until_element_is_present('XPATH', '//div[@class=\'blocking-screen\']'):
            check_boxes_before = self.driver.find_elements_by_xpath(self.xpath_edit_tab_record_checkbox)

            if  len(check_boxes_before) > 0:
                self.click_element_xpath(self.xpath_btn.format('Clear Grid'), 'Clear Grid button')
                self.click_element_xpath_1(self.xpath_btn_popup_clear, 'Pop-up Clear button')

                if not self.is_element_present('XPATH',self.xpath_edit_tab_record_checkbox):
                    self.click_element_xpath(self.xpath_btn.format('Refresh'), 'Refresh button')

                    if self.is_element_present('XPATH', self.xpath_edit_tab_record_checkbox):
                        check_boxes_after = self.driver.find_elements_by_xpath(self.xpath_edit_tab_record_checkbox)

                        if len(check_boxes_before) == len(check_boxes_after):
                            self.report.addTestStep('Refresh', 'Refresh is working as expected', Status.PASS)
                        else:
                            self.report.addTestStep('Refresh', 'Refresh is not working as expected', Status.FAIL)

    def add_row__fun(self, data_form_folder, data_form):
        self.click_element_xpath(self.xpath_client_folder, "Client Folder")
        self.click_element_xpath(self.xpath_dataform_folder.format(data_form_folder), data_form_folder + ' Folder')
        self.click_data_form(self.xpath_data_form, data_form)
        self.click_element_xpath(self.xpath_btn.format('Search'), 'Search button')

        if self.wait_until_element_is_present('XPATH', '//div[@class=\'blocking-screen\']'):
            check_boxes_before = self.driver.find_elements_by_xpath(self.xpath_edit_tab_record_checkbox)
            #self.report.addTestStep('Open Search', 'Search returned - ' +str(len(check_boxes_before))+ ' records', Status.PASS)

            self.click_element_xpath(self.xpath_btn.format('Add Row'), 'Add Row button')

            check_boxes_after = self.driver.find_elements_by_xpath(self.xpath_edit_tab_record_checkbox)

            if len(check_boxes_after) == len(check_boxes_before)+1:
                self.report.addTestStep('Add Row', 'No. of rows added - ' + str(len(check_boxes_after) - len(check_boxes_before)),
                                        Status.INFO)
                self.report.addTestStep('Add Row', 'Add Row is working as expected', Status.PASS)
            else:
                self.report.addTestStep('Add Row',
                                        'No. of rows added - ' + str(len(check_boxes_after) - len(check_boxes_before)),
                                        Status.INFO)
                self.report.addTestStep('Add Row', 'Add Row is not working as expected', Status.FAIL)

    def delete_fun(self, data_form_folder, data_form):
        self.click_element_xpath(self.xpath_client_folder, "Client Folder")
        self.click_element_xpath(self.xpath_dataform_folder.format(data_form_folder), data_form_folder + ' Folder')
        self.click_data_form(self.xpath_data_form, data_form)
        self.click_element_xpath(self.xpath_btn.format('Search'), 'Search button')

        if self.wait_until_element_is_present('XPATH', '//div[@class=\'blocking-screen\']'):
            check_boxes_before = self.driver.find_elements_by_xpath(self.xpath_edit_tab_record_checkbox)

            self.click_element_xpath(self.xpath_btn.format('Add Row'), 'Add Row button')

            check_boxes_after_1 = self.driver.find_elements_by_xpath(self.xpath_edit_tab_record_checkbox)

            if len(check_boxes_after_1) == len(check_boxes_before)+1:
                self.click_element_xpath(self.xpath_btn.format('Delete'), 'Delete button')
                self.click_element_xpath_1(self.xpath_btn_popup_delete, 'Pop-up Delete button')

                check_boxes_after_2 = self.driver.find_elements_by_xpath(self.xpath_edit_tab_record_checkbox)

                if len(check_boxes_after_2) == len(check_boxes_before):
                    self.report.addTestStep('Delete', 'Delete is working as expected', Status.PASS)
                else:
                    self.report.addTestStep('Delete', 'Delete is not working as expected', Status.FAIL)
