from selenium.webdriver.common.by import By

class CartProductWebElements:
    button_cart = (By.XPATH,"(//span[contains(text(),'item')])[1]")
    button_RemoveCart = (By.XPATH, "//button[@title='Remove']")
    link_ViewCart = (By.XPATH,"//strong[contains(text(),'Cart')]")
    link_Checkout = (By.XPATH,"//strong[contains(text(),'Checkout')]")