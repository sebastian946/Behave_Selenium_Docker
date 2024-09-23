from selenium.webdriver.common.by import By


class HeaderWebElements:
    icon_user = (By.XPATH,"//a[@title='My Account']")
    link_register = (By.XPATH,"//a[text()='Register']")
    link_login = (By.XPATH,"//a[text()='Login']")
    link_cart = (By.XPATH,"//a[@title='Shopping Cart']")