import pytest
import allure
from pages.landing_page import LandingPage
from data import LandingAnswers


class TestLandingPage:

    @allure.title("Проверка ответов на вопросы в блоке FAQ")
    @pytest.mark.parametrize(
        "question_num, expected_answer",
        LandingAnswers.ANSWERS.items()
    )
    def test_landing_page_answers(self, driver, question_num, expected_answer):

        landing_page = LandingPage(driver)
        landing_page.open_url()
        landing_page.scroll_to_questions()

        landing_page.click_on_question(question_num)
        answer_text = landing_page.get_answer_text(question_num)

        assert answer_text == expected_answer
