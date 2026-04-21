import pytest
import allure
from pages.home_page import HomePage
from pages.registration_page import RegistrationPageFirstStep
from locators.home_page_locators import HomePageLocators

class TestRegistrationPage:

    @allure.title("Проверка позитивного сценария заказа самоката")
    @pytest.mark.parametrize(
        "name, surname, address, metro, phone, date, comment, order_button",
        [
            # Иван + Верхняя кнопка
            ("Иван", "Иванов", "Ленинградская", "Сокольники", "79991112233", "19.04.2026", "Позвоните за час", HomePageLocators.ORDER_BUTTON_TOP),
            # Пётр + Нижняя кнопка
            ("Пётр", "Петров", "Кащенко", "Черкизовская", "79005556677", "20.04.2026", "Оставьте у подъезда", HomePageLocators.ORDER_BUTTON_BOTTOM)
        ]
    )
    def test_order_scooter_successfully(self, driver, name, surname, address, metro, phone, date, comment, order_button):
        home_page = HomePage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")
        
        home_page.accept_cookies()
        
        with allure.step("Нажать на кнопку 'Заказать'"):
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
        driver.get("https://qa-scooter.praktikum-services.ru/")
        home_page.accept_cookies()
        home_page.click_element(HomePageLocators.ORDER_BUTTON_TOP)
        
        first_step = RegistrationPageFirstStep(driver)
        assert first_step.check_all_validation_errors(), "Не все сообщения об ошибках отобразились!"
