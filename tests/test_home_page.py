import pytest
import allure
from pages.home_page import HomePage

class TestHomePage:
    
    URL = "https://qa-scooter.praktikum-services.ru/"

    @allure.title("Проверка заголовков вопросов и текстов ответов в FAQ")
    @pytest.mark.parametrize(
        "index, expected_question, expected_answer",
        [
            (0, "Сколько это стоит? И как оплатить?", "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
            (1, "Хочу сразу несколько самокатов! Так можно?", "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
            (2, "Как рассчитывается время аренды?", "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
            (3, "Можно ли заказать самокат прямо на сегодня?", "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
            (4, "Можно ли продлить заказ или вернуть самокат раньше?", "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
            (5, "Вы привозите зарядку вместе с самокатом?", "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
            (6, "Можно ли отменить заказ?", "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
            (7, "Я жизу за МКАДом, привезёте?", "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
        ]
    )
    def test_faq_questions(self, driver, index, expected_question, expected_answer):
        home_page = HomePage(driver)
        
        # Опечатка в 8-м вопросе
        if index == 7:
            allure.dynamic.title("Проверка FAQ: Вопрос №8 (Обнаружен БАГ: опечатка)")
            allure.dynamic.description("Найдена опечатка в тексте вопроса: 'жизу' вместо 'живу'.")
            allure.dynamic.severity(allure.severity_level.MINOR)
            allure.dynamic.label("tag", "BUG")

        with allure.step("Открыть главную страницу"):
            driver.get(self.URL)

        with allure.step("Принять куки"):
            home_page.accept_cookies()

        with allure.step(f"Проверить текст вопроса №{index + 1}"):
            home_page.click_on_question(index) 
            actual_question = home_page.get_question_text(index)
            assert actual_question == expected_question, f"Текст вопроса №{index+1} не совпадает!"

        with allure.step(f"Проверить текст ответа №{index + 1}"):
            actual_answer = home_page.get_answer_text(index)
            assert actual_answer == expected_answer, f"Текст ответа №{index+1} не совпадает!"
  