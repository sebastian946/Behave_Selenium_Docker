from selenium.webdriver.common.by import By

class LoginWebElements:
    input_email = (By.ID,"input-email")
    input_password = (By.ID,"input-password")
    button_login = (By.XPATH,"//input[@value='Login']")