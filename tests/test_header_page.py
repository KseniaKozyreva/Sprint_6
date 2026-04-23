import pytest
import allure
from pages.header_page import HeaderPage
from data import Urls  

class TestHeader:
    @allure.feature("Шапка сайта")
    @allure.story("Переходы по логотипам")
    @allure.title("Логотип 'Самокат' ведет на главную страницу")
    def test_scooter_logo_redirect(self, driver):
        header_page = HeaderPage(driver)
        
        driver.get(Urls.BASE_URL) 
        
        header_page.click_scooter_logo()
        
        current_url = header_page.get_current_url()
        assert current_url == Urls.BASE_URL

    @allure.feature("Шапка сайта")
    @allure.story("Переходы по логотипам")
    @allure.title("Логотип 'Яндекс' открывает Дзен в новой вкладке")
    def test_yandex_logo_redirect(self, driver):
        header_page = HeaderPage(driver)
        
        driver.get(Urls.BASE_URL)
        
        header_page.click_yandex_logo()
        
        current_url = header_page.check_yandex_open_dzen() 
        
        assert Urls.DZEN_URL in current_url
