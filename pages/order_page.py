import allure
from pages.base_page import BasePage
from locators.locators_order_page import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Заполнить имя")
    def fill_name(self, name):
        self.find_element(OrderPageLocators.INPUT_NAME).send_keys(name)

    @allure.step("Заполнить фамилию")
    def fill_surname(self, surname):
        self.find_element(OrderPageLocators.INPUT_SURNAME).send_keys(surname)

    @allure.step("Заполнить адрес")
    def fill_address(self, address):
        self.find_element(OrderPageLocators.INPUT_ADDRESS).send_keys(address)

    @allure.step("Заполнить телефон")
    def fill_phone(self, phone):
        self.find_element(OrderPageLocators.INPUT_PHONE).send_keys(phone)

    @allure.step("Нажать Далее")
    def click_next(self):
        self.click_on_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step("Выбрать дату доставки")
    def choose_date(self, day):
        self.click_on_element(OrderPageLocators.INPUT_DATE)

        date_locator = self.format_locator(
            OrderPageLocators.DATE_OPTION,
            day
        )
        self.click_on_element(date_locator)

    @allure.step("Выбрать срок аренды")
    def choose_rental_period(self, period):
        self.click_on_element(OrderPageLocators.DROPDOWN_RENTAL_PERIOD)

        period_locator = self.format_locator(
            OrderPageLocators.RENTAL_OPTION,
            period
        )
        self.click_on_element(period_locator)

    @allure.step("Выбрать цвет")
    def choose_color(self, color_id):
        color_locator = self.format_locator(
            OrderPageLocators.COLOR_CHECKBOX,
            color_id
        )
        self.click_on_element(color_locator)

    @allure.step("Нажать кнопку Заказать")
    def click_create_order(self):
        self.click_on_element(OrderPageLocators.CREATE_ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_on_element(OrderPageLocators.CONFIRM_YES_BUTTON)

    @allure.step("Проверить, что заказ успешно оформлен")
    def is_order_success(self):
        return self.find_element(OrderPageLocators.ORDER_SUCCESS).is_displayed()









