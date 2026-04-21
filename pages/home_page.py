import allure
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators  
from locators.home_page_locators import HomePageLocators


class HomePage(BasePage):
    
    @allure.step("Принять куки")
    def accept_cookies(self):
        if self.driver.find_elements(*BasePageLocators.COOKIE_BUTTON):
            self.click_element(BasePageLocators.COOKIE_BUTTON)

    @allure.step("Кликнуть на вопрос №{index}")
    def click_on_question(self, index):
        locator_name = f"QUESTION_BUTTON_{index}"
        locator = getattr(HomePageLocators, locator_name)
        
        element = self.wait_for_element(locator)
        
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        
        self.driver.execute_script("arguments[0].click();", element)


    @allure.step("Получить текст вопроса №{index}")
    def get_question_text(self, index):
        locator_name = f"QUESTION_BUTTON_{index}"
        locator = getattr(HomePageLocators, locator_name)
        return self.get_text_from_element(locator)

    @allure.step("Получить текст ответа №{index}")
    def get_answer_text(self, index):
        locator_name = f"ANSWER_TEXT_{index}"
        locator = getattr(HomePageLocators, locator_name)
        return self.get_text_from_element(locator)
    