from lib.components.CheckoutWebElements import CheckoutWebElements


class CheckoutPage:
    def __init__(self,context):
        self.context = context
        self.web_element = CheckoutWebElements

    def fillForm(self,country,state):
        self.context.actions.send_keys(self.web_element.input_firstname,self.context.data.generateFirstName())
        self.context.actions.send_keys(self.web_element.input_lastname,self.context.data.generateLastName())
        self.context.actions.send_keys(self.web_element.input_company,self.context.data.generateCompany())
        self.context.actions.send_keys(self.web_element.input_address1,self.context.data.generateAddress())
        self.context.actions.send_keys(self.web_element.input_city,self.context.data.generateCity())
        self.context.actions.send_keys(self.web_element.input_postalCode,"1234567")
        self.context.actions.selectOptionText(self.web_element.select_country,country)
        self.context.web_driver.implicitly_wait(5)
        self.context.actions.selectOptionText(self.web_element.select_state,state)

    def clickContinue(self):
        self.context.actions.clickElement(self.web_element.button_continuePayment)

    def clickContinueShipping(self):
        self.context.actions.clickElement(self.web_element.button_continueShippingAddress)

    def clickContinueShippingMethod(self):
        self.context.actions.clickElement(self.web_element.button_continueShippingMethod)

    def fillComments(self):
        self.context.actions.send_keys(self.web_element.textArea_comment,self.context.data.generateText())

    def clickCheckoutTerms(self):
        self.context.actions.clickElement(self.web_element.checkbox_Terms)

    def clickContinuePaymentMethod(self):
        self.context.actions.clickElement(self.web_element.button_continuePaymentMethod)

    def clickConfirmOrder(self):
        self.context.actions.clickElement(self.web_element.button_confirm_order)