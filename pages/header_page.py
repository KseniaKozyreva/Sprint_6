import allure
from pages.base_page import BasePage
from locators.header_locators import HeaderLocators

class HeaderPage(BasePage):
    @allure.step("Кликнуть на логотип 'Самокат'")
    def click_scooter_logo(self):
        self.click_element(HeaderLocators.LOGO_SCOOTER)

    @allure.step("Кликнуть на логотип 'Яндекс'")
    def click_yandex_logo(self):
        self.click_element(HeaderLocators.LOGO_YANDEX)

    @allure.step("Переключиться на новую вкладку и дождаться загрузки Дзена")
    def check_yandex_open_dzen(self):
        self.switch_to_new_window()
        self.wait_for_url_contains("dzen.ru")
        return self.driver.current_url
