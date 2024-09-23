from hamcrest import assert_that, equal_to, contains_string
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Actions:
    def __init__(self,driver):
        self.driver = driver

    def waitElementPresent(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def openUrl(self,url):
        self.driver.get(url)

    def clickElement(self,locator:WebElement):
        element = self.waitElementPresent(locator)
        element.click()

    def send_keys(self,locator,content):
        element = self.waitElementPresent(locator)
        element.send_keys(content)

    def selectOptionValue(self,locator,value):
        select = self.waitElementPresent(locator)
        element = Select(select)
        element.select_by_value(value)

    def selectOptionText(self,locator,value):
        select = self.waitElementPresent(locator)
        element = Select(select)
        element.select_by_visible_text(value)

    def getText(self,locator):
        element = self.waitElementPresent(locator)
        text = element.text
        return text

    def clearInput(self,locator):
        elemet = self.waitElementPresent(locator)
        elemet.clear()

    def assertText(self,textGet,textToWait):
        assert_that(textGet,equal_to(textToWait))

    def assertContent(self,textGet,textToWait):
        assert_that(textGet,contains_string(textToWait))