from selenium.webdriver.common.by import By

class RegistrationFirstStepLocators:
    # Для кого самокат 
    # Поле Имя
    NAME_INPUT = (By.XPATH, './/input[@placeholder="* Имя"]')
    # Поле Фамилия
    SURNAME_INPUT = (By.XPATH, './/input[@placeholder="* Фамилия"]')
    # Поле Адрес
    ADDRESS_INPUT = (By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]')
    # Поле Станция метро
    METRO_INPUT = (By.XPATH, './/input[@placeholder="* Станция метро"]')
    # Выбор станции метро
    METRO_STATION_OPTION = (By.XPATH, './/div[@class="select-search__select"]//div[text()="{}"]')
    # Поле Телефон
    PHONE_INPUT = (By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]')
    # Кнопка Далее
    NEXT_BUTTON = (By.XPATH, './/button[text()="Далее"]')

    # Ошибки валидации
    # Поле Имя
    ERROR_NAME = (By.XPATH, './/div[text()="Введите корректное имя"]')
    # Поле Фамилия
    ERROR_SURNAME = (By.XPATH, './/div[text()="Введите корректную фамилию"]')
    # Поле Адрес
    ERROR_ADDRESS = (By.XPATH, './/div[text()="Введите корректный адрес"]')
    # Поле станции метро
    ERROR_METRO = (By.XPATH, './/div[text()="Выберите станцию"]')
    # Поле Телефон
    ERROR_PHONE = (By.XPATH, './/div[text()="Введите корректный номер"]')

class RegistrationSecondStepLocators:
    # Про аренду 
    # Поле Когда привезти самокат
    DATE_INPUT = (By.XPATH, './/input[@placeholder="* Когда привезти самокат"]')
    # Поле Срок аренды
    RENT_DURATION_FIELD = (By.XPATH, ".//div[@class='Dropdown-placeholder' and text()='* Срок аренды']")
    # Время аренды
    RENT_TIME_SUITKI = (By.XPATH, ".//div[@class='Dropdown-menu']//div[text()='сутки']")
    # Цвет самоката черный жемчуг
    BLACK_COLOR = (By.ID, "black")
    # Цвет самоката серая безысходность
    GREY_COLOR = (By.ID, "grey")
    # Поле Комментарий для курьера
    COMMENT_INPUT = (By.XPATH, './/input[@placeholder="Комментарий для курьера"]')
    
    # Кнопка Назад
    BACK_BUTTON = (By.XPATH, './/button[text()="Назад"]')
    # Кнопка Заказать
    ORDER_BUTTON = (By.XPATH, './/div[contains(@class, "Order_Buttons")]//button[text()="Заказать"]')
    # Кнопка Да
    CONFIRM_BUTTON = (By.XPATH, ".//button[text()='Да']")
    
    # Окно Заказ оформлен
    ORDER_SUCCESS_MODAL = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader') and text()='Заказ оформлен']")
