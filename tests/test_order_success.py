from pages.order_page import OrderPage
import allure
import pytest


@allure.title("Оформление заказа самоката через кнопки Заказать")
@pytest.mark.parametrize('button', ['header_button', 'page_button'])
def test_order_upp_success(driver, button):

    order_page = OrderPage(driver)
    order_page.open_url()

    with allure.step("Проверяем возможность сделать заказ самоката"):
        order_page.click_on_element_make_order_header(button=button)
        order_page.name_field_find_element_with_wait()
        order_page.fill_name_field()
        order_page.fill_surname_field()
        order_page.fill_adress_field()
        order_page.select_metro()
        order_page.fill_phone_field()
        order_page.click_on_element_next()
        order_page.pick_date()
        order_page.pick_rental_period()
        order_page.click_on_element_color_black()
        order_page.fill_comment_field()
        order_page.click_on_element_create_order()
        order_page.click_on_element_confirm_order_yes()

    with allure.step("Проверяем успешное оформление заказа"):
        assert order_page.is_order_success(), "Заказ не был оформлен"


