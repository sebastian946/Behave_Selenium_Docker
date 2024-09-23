from lib.components.HeaderWebElements import HeaderWebElements


class HeaderComponent:
    def __init__(self,context):
        self.context = context
        self.web_element = HeaderWebElements

    def clicklinkUser(self):
        self.context.actions.clickElement(self.web_element.icon_user)

    def clicklinkRegister(self):
        self.context.actions.clickElement(self.web_element.link_register)

    def clicklinkLogin(self):
        self.context.actions.clickElement(self.web_element.link_login)

    def clickCartShopping(self):
        self.context.actions.clickElement(self.web_element.link_cart)
