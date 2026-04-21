from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Метод для ожидания появления элемента
    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    # Метод для клика по элементу
    def click_element(self, locator):
        self.wait_for_element(locator).click()

    # Метод для ввода текста в поле
    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear() 
        element.send_keys(text)

    # Метод для получения текста 
    def get_text_from_element(self, locator):
        return self.wait_for_element(locator).text

    # Метод для скролла до элемента
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    # Метод для переключения на новую вкладку
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
