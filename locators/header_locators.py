from selenium.webdriver.common.by import By

class HeaderLocators:
    # Логотип "Самокат"
    LOGO_SCOOTER = (By.XPATH, "//img[@alt='Scooter']")
    # Логотип "Яндекс"
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Yandex']")
