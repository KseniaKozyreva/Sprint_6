import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    
    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url
    
    
    @allure.step("Проверка наличия элемента {locator}")
    def check_element_exists(self, locator):
        return len(self.driver.find_elements(*locator)) > 0

    @allure.step("Ожидание появления элемента {locator}")
    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    @allure.step("Клик по элементу {locator}")
    def click_element(self, locator):
        self.wait_for_element(locator).click()

    @allure.step("Ввод текста '{text}' в элемент {locator}")
    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста из элемента {locator}")
    def get_text_from_element(self, locator):
        return self.wait_for_element(locator).text

    @allure.step("Скролл до элемента {locator}")
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Переключение на новую вкладку")
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Ожидание, что URL содержит '{url_part}'")
    def wait_for_url_contains(self, url_part):
        return WebDriverWait(self.driver, 10).until(
            lambda d: url_part in d.current_url
        )
