from selenium.webdriver.common.by import By


class test_locator_landing_questions:

    BUTTON_QUESTION = (By.ID, "accordion__heading-{}")
    QUESTION_8 = (By.ID, "accordion__heading-7")


class test_locator_landing_answer:

    TEXT_ANSWER = (By.ID, "accordion__panel-{}")


class test_locators:

    BUTTON_MAKE_ORDER_HEADER = (By.XPATH, '//button[text()="Заказать"]')
    BUTTON_MAKE_ORDER_LANDING = (By.XPATH, '//button[text()="Заказать"]')

    LOGO_SCOOTER = (By.CSS_SELECTOR, ".Header_LogoScooter__3lsAR img")
    YA_LOGO = (By.CSS_SELECTOR, "img[src='/assets/ya.svg']")
