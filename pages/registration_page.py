import allure
from pages.base_page import BasePage
from locators.registration_locators import RegistrationFirstStepLocators, RegistrationSecondStepLocators
from selenium.webdriver.common.keys import Keys

# Для кого самокат (Первое окно)
class RegistrationPageFirstStep(BasePage):

    @allure.step("Заполнение первой страницы: Для кого самокат")
    def fill_user_data(self, name, surname, address, metro_station, phone):
        # Вводим Имя
        self.enter_text(RegistrationFirstStepLocators.NAME_INPUT, name)
        
        # Вводим Фамилию
        self.enter_text(RegistrationFirstStepLocators.SURNAME_INPUT, surname)
        
        # Вводим Адрес
        self.enter_text(RegistrationFirstStepLocators.ADDRESS_INPUT, address)
        
        # Поле Метро
        self.click_element(RegistrationFirstStepLocators.METRO_INPUT)
        self.enter_text(RegistrationFirstStepLocators.METRO_INPUT, metro_station)
        
        method, locator = RegistrationFirstStepLocators.METRO_STATION_OPTION
        specific_station_locator = (method, locator.format(metro_station))
        self.click_element(specific_station_locator)
 
        
        # Вводим Телефон
        self.enter_text(RegistrationFirstStepLocators.PHONE_INPUT, phone)


    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        self.click_element(RegistrationFirstStepLocators.NEXT_BUTTON)
        return RegistrationPageSecondStep(self.driver)

    
    @allure.step("Проверка ошибок валидации при пустых полях")
    def check_all_validation_errors(self):
        self.enter_text(RegistrationFirstStepLocators.ADDRESS_INPUT, "п")
        
        self.click_element(RegistrationFirstStepLocators.NEXT_BUTTON)
        
        errors = [
            RegistrationFirstStepLocators.ERROR_NAME,
            RegistrationFirstStepLocators.ERROR_SURNAME,
            RegistrationFirstStepLocators.ERROR_ADDRESS,
            RegistrationFirstStepLocators.ERROR_METRO,
            RegistrationFirstStepLocators.ERROR_PHONE
        ]
        
        for error_locator in errors:
            element = self.wait_for_element(error_locator)
            if not element.is_displayed():
                return False
        
        return True


# Про аренду (Второе окно)
class RegistrationPageSecondStep(BasePage):

    @allure.step("Нажать кнопку 'Назад'")
    def click_back_button(self):
        self.click_element(RegistrationSecondStepLocators.BACK_BUTTON)
        return RegistrationPageFirstStep(self.driver)

    @allure.step("Заполнение второй страницы: Про аренду")
    def fill_rent_data(self, date, comment):
        # Поле Когда привезти самокат
        date_input = self.wait_for_element(RegistrationSecondStepLocators.DATE_INPUT)
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)
        
        # Поле Срок аренды
        self.click_element(RegistrationSecondStepLocators.RENT_DURATION_FIELD)
        self.click_element(RegistrationSecondStepLocators.RENT_TIME_SUITKI)
        
        # Цвета: кликаем на оба по очереди
        self.click_element(RegistrationSecondStepLocators.BLACK_COLOR)
        self.click_element(RegistrationSecondStepLocators.GREY_COLOR)
        
        # Поле Комментарий
        self.enter_text(RegistrationSecondStepLocators.COMMENT_INPUT, comment)

    @allure.step("Нажать 'Заказать'")
    def click_order_button(self):
        self.click_element(RegistrationSecondStepLocators.ORDER_BUTTON)

    @allure.step("Подтверждение заказа (Нажать 'Да')")
    def confirm_order(self):
        self.click_element(RegistrationSecondStepLocators.CONFIRM_BUTTON)

    @allure.step("Заказ оформлен")
    def check_success_modal_is_visible(self):
        return self.wait_for_element(RegistrationSecondStepLocators.ORDER_SUCCESS_MODAL).is_displayed()
