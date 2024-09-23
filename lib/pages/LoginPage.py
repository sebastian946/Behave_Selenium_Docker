from lib.components.LoginWebElements import LoginWebElements


class LoginPage:
    def __init__(self,context):
        self.context = context
        self.web_element = LoginWebElements

    def fillLoginForm(self,email,password):
        self.context.actions.send_keys(self.web_element.input_email,email)
        self.context.actions.send_keys(self.web_element.input_password,password)

    def clickLoginButton(self):
        self.context.actions.clickElement(self.web_element.button_login)