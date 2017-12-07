from selenium import webdriver


class CookieHandler:

    driver = webdriver
    cookies_dict = {}

    def __init__(self, driver):
        self.driver = driver

    def get_all_cookies(self):
        cookies_list = self.driver.get_cookies()
        for cookie in cookies_list:
            self.cookies_dict[cookie['name']] = cookie['value']
        return self.cookies_dict

    def get_session_id(self):
        session_id = self.cookies_dict.get('JSESSIONID')
        return session_id




