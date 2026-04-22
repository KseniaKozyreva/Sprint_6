import pytest
import allure
from pages.home_page import HomePage
from pages.registration_page import RegistrationPageFirstStep
from locators.home_page_locators import HomePageLocators
from data import Urls, TestData  

class TestRegistrationPage:

    @allure.title("Проверка позитивного сценария заказа самоката")
    @pytest.mark.parametrize(
        "user_data, order_button",
        [
            (TestData.USER_1, HomePageLocators.ORDER_BUTTON_TOP),
            (TestData.USER_2, HomePageLocators.ORDER_BUTTON_BOTTOM)
        ]
    )
    def test_order_scooter_successfully(self, driver, user_data, order_button):
        name, surname, address, metro, phone, date, comment = user_data
        
        home_page = HomePage(driver)
        driver.get(Urls.BASE_URL) 
        home_page.accept_cookies()

        home_page.click_element(order_button)
        
        first_step = RegistrationPageFirstStep(driver)
        first_step.fill_user_data(name, surname, address, metro, phone)
        
        second_step = first_step.click_next_button()
        
        first_step = second_step.click_back_button()
        second_step = first_step.click_next_button()
        
        second_step.fill_rent_data(date, comment)
        second_step.click_order_button()
        second_step.confirm_order()
        
        assert second_step.check_success_modal_is_visible(), "Окно 'Заказ оформлен' не появилось"

    @allure.title("Проверка ошибок валидации при пустых полях формы заказа")
    def test_registration_empty_fields_errors(self, driver):
        home_page = HomePage(driver)
        driver.get(Urls.BASE_URL)
        home_page.accept_cookies()
        
        home_page.click_element(HomePageLocators.ORDER_BUTTON_TOP)
        first_step = RegistrationPageFirstStep(driver)
        
        assert first_step.check_all_validation_errors(), "Не все сообщения об ошибках отобразились!"
