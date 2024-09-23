from selenium.webdriver.common.by import By

class CheckoutWebElements:
    input_firstname = (By.ID,"input-payment-firstname")
    input_lastname = (By.ID,"input-payment-lastname")
    input_company = (By.ID,"input-payment-company")
    input_address1 = (By.ID,"input-payment-address-1")
    input_city = (By.ID,"input-payment-city")
    input_postalCode = (By.ID,"input-payment-postcode")
    select_country = (By.ID,"input-payment-country")
    select_state = (By.ID,"input-payment-zone")
    textArea_comment = (By.CLASS_NAME,"comment")
    checkbox_Terms = (By.XPATH,"//input[@type='checkbox']")
    title_successfully = (By.XPATH, "(//div[@id='content']/p)[1]")
    button_continuePayment = (By.ID,"button-payment-address")
    button_continueShippingAddress = (By.ID,"button-shipping-address")
    button_continueShippingMethod = (By.ID,"button-shipping-method")
    button_continuePaymentMethod = (By.ID,"button-payment-method")
    button_confirm_order = (By.ID, "button-confirm")
