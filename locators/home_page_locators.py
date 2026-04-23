from selenium.webdriver.common.by import By

class HomePageLocators:
    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH, ".//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']")

    # Вопросы и ответы 
    # Вопросы
    QUESTION_BUTTON_TEMPLATE = (By.ID, "accordion__heading-{}")
    # Ответы
    ANSWER_TEXT_TEMPLATE = (By.ID, "accordion__panel-{}")
    
    # Вопросы
    QUESTION_BUTTON_0 = (By.ID, "accordion__heading-0")
    QUESTION_BUTTON_1 = (By.ID, "accordion__heading-1")
    QUESTION_BUTTON_2 = (By.ID, "accordion__heading-2")
    QUESTION_BUTTON_3 = (By.ID, "accordion__heading-3")
    QUESTION_BUTTON_4 = (By.ID, "accordion__heading-4")
    QUESTION_BUTTON_5 = (By.ID, "accordion__heading-5")
    QUESTION_BUTTON_6 = (By.ID, "accordion__heading-6")
    QUESTION_BUTTON_7 = (By.ID, "accordion__heading-7")
    
    # Ответы
    ANSWER_TEXT_0 = (By.ID, "accordion__panel-0")
    ANSWER_TEXT_1 = (By.ID, "accordion__panel-1")
    ANSWER_TEXT_2 = (By.ID, "accordion__panel-2")
    ANSWER_TEXT_3 = (By.ID, "accordion__panel-3")
    ANSWER_TEXT_4 = (By.ID, "accordion__panel-4")
    ANSWER_TEXT_5 = (By.ID, "accordion__panel-5")
    ANSWER_TEXT_6 = (By.ID, "accordion__panel-6")
    ANSWER_TEXT_7 = (By.ID, "accordion__panel-7")
