import allure
from pages.base_page import BasePage
from locators.order_page_locators import order_page_locators


class OrderPage(BasePage):

    def _init_(self, driver):
        super()._init_(driver)

    @allure.step("Заполнить имя")
    def fill_name(self, name):
        self.find_element(order_page_locators.INPUT_NAME).send_keys(name)

    @allure.step("Заполнить фамилию")
    def fill_surname(self, surname):
        self.find_element(order_page_locators.INPUT_SURNAME).send_keys(surname)

    @allure.step("Заполнить адрес")
    def fill_address(self, address):
        self.find_element(order_page_locators.INPUT_ADDRESS).send_keys(address)

    @allure.step("Заполнить телефон")
    def fill_phone(self, phone):
        self.find_element(order_page_locators.INPUT_PHONE).send_keys(phone)

    @allure.step("Нажать Далее")
    def click_next(self):
        self.click_on_element(order_page_locators.BUTTON_NEXT)

    @allure.step("Выбрать дату доставки")
    def choose_date(self, day):
        self.click_on_element(order_page_locators.INPUT_DATE)

        date_locator = self.format_locator(
            order_page_locators.DATE_OPTION,
            day
        )
        self.click_on_element(date_locator)

    @allure.step("Выбрать срок аренды")
    def choose_rental_period(self, period):
        self.click_on_element(order_page_locators.DROPDOWN_RENTAL_PERIOD)

        period_locator = self.format_locator(
            order_page_locators.RENTAL_OPTION,
            period
        )
        self.click_on_element(period_locator)

    @allure.step("Выбрать цвет")
    def choose_color(self, color_id):
        color_locator = self.format_locator(
            order_page_locators.COLOR_CHECKBOX,
            color_id
        )
        self.click_on_element(color_locator)

    @allure.step("Нажать кнопку Заказать")
    def click_create_order(self):
        self.click_on_element(order_page_locators.CREATE_ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_on_element(order_page_locators.CONFIRM_YES_BUTTON)
        
        @allure.step("Проверить, что заказ успешно оформлен")
def is_order_success(self):
    return self.find_element(order_page_locators.ORDER_SUCCESS).is_displayed()









