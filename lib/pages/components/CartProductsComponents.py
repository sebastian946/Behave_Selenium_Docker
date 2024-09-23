from lib.components.CartProductsWebElements import CartProductWebElements


class CartProductsComponents:
    def __init__(self,context):
        self.context = context
        self.webElement = CartProductWebElements

    def clickButtonCart(self):
        self.context.actions.clickElement(self.webElement.button_cart)

    def clickLinkCheckout(self):
        self.context.actions.clickElement(self.webElement.link_Checkout)