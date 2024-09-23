from lib.components.RegisterWebElements import RegisterWebElements
from lib.pages.LoginPage import LoginPage
from lib.pages.components.HeaderComponent import HeaderComponent


class RegisterPage:
    def __init__(self,context):
        self.context = context
        self.web_element = RegisterWebElements
        self.password = self.context.data.generatePassword()
        self.firstName = self.context.data.generateFirstName()
        self.lastName = self.context.data.generateLastName()
        self.email = self.context.data.generateEmail()
        self.phone = self.context.data.generateEmail()

    def fillRegisterForm(self):
        self.context.actions.send_keys(RegisterWebElements.input_firstName,self.firstName)
        self.context.actions.send_keys(RegisterWebElements.input_lastName,self.lastName)
        self.context.actions.send_keys(RegisterWebElements.input_Email,self.email)
        self.context.actions.send_keys(RegisterWebElements.input_Phone,self.phone)
        self.context.actions.send_keys(RegisterWebElements.input_Password,self.password)
        self.context.actions.send_keys(RegisterWebElements.input_ConfirmPassword,self.password)

    def clickPolicy(self):
        self.context.actions.clickElement(RegisterWebElements.checkbox_PrivacyPolicy)

    def clickContinue(self):
        self.context.actions.clickElement(RegisterWebElements.button_Continue)

    def validateAlert(self):
        header = HeaderComponent(self.context)
        login = LoginPage(self.context)
        try:
            content = self.context.actions.getText(RegisterWebElements.title_Congratulations)
            self.context.actions.assertContent(content, "Congratulations")
        except AssertionError:
            header.clicklinkUser()
            header.clicklinkLogin()
            login.fillLoginForm(self.email, self.password)
            login.clickLoginButton()
