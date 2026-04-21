import pytest
import allure
from pages.header_page import HeaderPage

class TestHeader:

    @allure.feature("Шапка сайта")
    @allure.story("Переходы по логотипам")
    @allure.title("Логотип 'Самокат' ведет на главную страницу")
    def test_scooter_logo_redirect(self, driver):
        header_page = HeaderPage(driver)
        
        with allure.step("Открыть страницу заказа"):
            driver.get("https://qa-scooter.praktikum-services.ru/")
        
        with allure.step("Нажать на логотип 'Самокат'"):
            header_page.click_scooter_logo()
        
        with allure.step("Проверить, что произошел редирект на главную"):
            assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.feature("Шапка сайта")
    @allure.story("Переходы по логотипам")
    @allure.title("Логотип 'Яндекс' открывает Дзен в новой вкладке")
    def test_yandex_logo_redirect(self, driver):
        header_page = HeaderPage(driver)
        
        with allure.step("Открыть главную страницу"):
            driver.get("https://qa-scooter.praktikum-services.ru/")
        
        with allure.step("Нажать на логотип 'Яндекс'"):
            header_page.click_yandex_logo()
        
        with allure.step("Переключиться на новую вкладку и проверить переход на Дзен"):
            current_url = header_page.check_yandex_open_dzen()
            assert "dzen.ru" in current_url
