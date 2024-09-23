from lib.components.DetailProductWebElements import DetailProductWebElements


class DetailsProductPage:
    def __init__(self,quantity,context):
        self.context = context
        self.quantity = quantity
        self.web_element = DetailProductWebElements

    def sendQuantity(self):
        self.context.actions.clearInput(self.web_element.input_Quality)
        self.context.actions.send_keys(self.web_element.input_Quality,self.quantity)

    def clickAddCart(self):
        self.context.actions.clickElement(self.web_element.button_AddCart)

    def validateAlert(self,contentText):
        content  = self.context.actions.getText(self.web_element.alertText_Success)
        self.context.actions.assertContent(content,contentText)

    