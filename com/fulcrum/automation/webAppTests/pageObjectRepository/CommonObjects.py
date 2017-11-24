

class CommonObjects:

    def __init__(self):

        self.xpath_txt_field = '//div[@class = \'dataform-tab tab-content has-action-bar\'' \
                               ' and not(contains(@style,\'display: none;\'))]' \
                               '//label[contains(text(),\'{}\')]//following-sibling::input'

        # Results tab
        self.xpath_btn_results_tab_edit_icon = '//div[@class = \'grid_data_cell uppercase\']/div/a'

        # Generic
        self.xpath_btn = '//div[not(contains(@style,\'display: none;\')) ' \
                         'and @class = ' \
                         '\'dataform-tab tab-content has-action-bar\']' \
                         '//div[normalize-space(text())=\'{}\']'

        self.xpath_btn_popup_yes = '//a[contains(text(),\'Yes\')]'
        self.xpath_btn_popup_no = '//a[contains(text(),\'No\')]'

        self.xpath_link_search_tab = '//li[@class=\'tab\']/a[contains(text(),\'Search\')]'
        self.xpath_link_results_tab = '//li[@class=\'tab\']/a[contains(text(),\'Results\')]'
        self.xpath_link_edit_tab = '//li[@class=\'tab\']/a[contains(text(),\'Edit\')]'

        self.xpath_exception_window_title = '//div[text()=\'{}\']'



