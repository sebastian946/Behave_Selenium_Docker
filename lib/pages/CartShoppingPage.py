from lib.components.CartShoppingWebElements import CartShoppingWebElements


class CartShoppingPage:
    def __init__(self,context):
        self.context = context
        self.web_element = CartShoppingWebElements

    def clickCheckout(self):
        self.context.actions.clickElement(self.web_element.button_checkout)