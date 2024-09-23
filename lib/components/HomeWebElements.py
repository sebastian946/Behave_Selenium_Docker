from selenium.webdriver.common.by import By


class HomeWebElements:
    input_search = (By.XPATH,"//input[@placeholder='Search']")
    button_search = (By.XPATH,"//div[@id='search']//button")
    image_items = (By.XPATH,"//div[@class='image']")
    