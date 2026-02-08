from selenium.webdriver.common.by import By


class Order_Page_Locators:

    INPUT_NAME = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    INPUT_SURNAME = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    INPUT_PHONE = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")

    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")

    INPUT_DATE = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат?']")
    DATE_OPTION = (By.XPATH, "//div[text()='{}']")

    DROPDOWN_RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-root")
    RENTAL_OPTION = (By.XPATH, "//div[text()='{}']")

    COLOR_CHECKBOX = (By.ID, "{}")

    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    
    ORDER_SUCCESS = (By.CLASS_NAME, "Order_ModalHeader")
