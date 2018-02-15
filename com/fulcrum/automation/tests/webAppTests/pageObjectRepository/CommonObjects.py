

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

        self.xpath_btn_popup_yes = '//button[contains(text(),\'Yes\')]'
        self.xpath_btn_popup_no = '//button[contains(text(),\'No\')]'
        self.xpath_btn_popup_save = '//button[contains(text(),\'Save\')]'
        self.xpath_btn_popup_back = '//button[contains(text(),\'Back\')]'
        self.xpath_btn_popup_close = '//form[@class = \'dataform-form form\']//a[contains(text(),\'Close\')]'
        self.xpath_btn_popup_clear = '//button[contains(text(),\'Clear\')]'
        self.xpath_btn_popup_delete = '//button[contains(text(),\'Delete\')]'

        self.xpath_link_search_tab = '//li[@class=\'tab\']/a[contains(text(),\'Search\')]'
        self.xpath_link_results_tab = '//li[@class=\'tab\']/a[contains(text(),\'Results\')]'
        self.xpath_link_edit_tab = '//li[@class=\'tab\']/a[contains(text(),\'Edit\')]'

        self.xpath_div_contains_txt = '//div[contains(text(),\'{}\')]'

        self.xpath_edit_tab_record_checkbox = '//div[@class = \'grid_data_cell grid_data_cell_select\']/input'


