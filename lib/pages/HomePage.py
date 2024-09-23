from lib.components.HomeWebElements import HomeWebElements


class HomePage:
    def __init__(self,product:str,context):
        self.product = product
        self.context = context
        self.webElements = HomeWebElements

    def searchProduct(self):
        self.context.actions.send_keys(self.webElements.input_search,self.product)

    def clickSearchbutton(self):
        self.context.actions.clickElement(self.webElements.button_search)

    def clickImageProduct(self):
        self.context.actions.clickElement(self.webElements.image_items)