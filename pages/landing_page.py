import allure
from pages.base_page import BasePage

from locators.locators_landing_page import (
    test_locator_landing_questions,
    test_locator_landing_answer,
    test_locators
)


class LandingPage(BasePage):

    def _init_(self, driver):
        super()._init_(driver)

    @allure.step("Прокрутить страницу до блока вопросов")
    def scroll_to_questions(self):
        self.scroll_to_element(test_locator_landing_questions.QUESTION_8)

    @allure.step("Кликнуть по вопросу")
    def click_on_question(self, question_num):
        formatted_locator = self.format_locator(
            test_locator_landing_questions.BUTTON_QUESTION,
            question_num
        )
        self.click_on_element(formatted_locator)

    @allure.step("Получить текст ответа")
    def get_answer_text(self, question_num):
        formatted_locator = self.format_locator(
            test_locator_landing_answer.TEXT_ANSWER,
            question_num
        )
        return self.get_text_from_element(formatted_locator)

    @allure.step("Клик по кнопке Заказать вверху страницы")
    def click_on_order_button(self):
        self.click_on_element(test_locators.BUTTON_MAKE_ORDER_HEADER)


