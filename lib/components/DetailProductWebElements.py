from selenium.webdriver.common.by import By


class DetailProductWebElements:
    input_Quality = (By.ID, "input-quantity")
    button_AddCart = (By.ID, "button-cart")
    alertText_Success = (By.XPATH,"//div[contains(text(),'Success')]")
