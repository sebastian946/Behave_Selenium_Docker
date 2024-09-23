from selenium.webdriver.common.by import By

class RegisterWebElements:
    input_firstName = (By.ID,"input-firstname")
    input_lastName = (By.ID,"input-lastname")
    input_Email = (By.ID,"input-email")
    input_Phone = (By.ID, "input-telephone")
    input_Password = (By.ID, "input-password")
    input_ConfirmPassword = (By.ID,"input-confirm")
    checkbox_PrivacyPolicy = (By.XPATH, "//input[@type='checkbox']")
    button_Continue = (By.XPATH,"//input[@type='submit']")
    title_Congratulations = (By.XPATH,"(//div[@id='content']/p)[1]")