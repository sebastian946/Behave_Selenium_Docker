from behave import given,when, then

from lib.pages.CartShoppingPage import CartShoppingPage
from lib.pages.CheckoutPage import CheckoutPage
from lib.pages.DetailProductPage import DetailsProductPage
from lib.pages.HomePage import HomePage
from lib.pages.RegisterPage import RegisterPage
from lib.pages.components.CartProductsComponents import CartProductsComponents
from lib.pages.components.HeaderComponent import HeaderComponent


@given(u'user open browser')
def step_impl(context):
    print(dir(context))
    context.actions.openUrl("https://opencart.abstracta.us")

@given(u'user go to the register page')
def step_impl(context):
    header = HeaderComponent(context)
    header.clicklinkUser()
    header.clicklinkRegister()

@when(u'user register in the page')
def step_impl(context):
    register = RegisterPage(context)
    register.fillRegisterForm()
    register.clickPolicy()
    register.clickContinue()


@then(u'the user registers successfully')
def step_impl(context):
    register = RegisterPage(context)
    register.validateAlert()


@then(u'search the product "{product}" and select it')
def step_impl(context,product):
    homePage = HomePage(product, context)
    homePage.searchProduct()
    homePage.clickSearchbutton()
    homePage.clickImageProduct()


@when(u'add to cart "{quantity}" product')
def step_impl(context,quantity):
    detailsProductPage = DetailsProductPage(quantity, context)
    detailsProductPage.sendQuantity()
    detailsProductPage.clickAddCart()
    detailsProductPage.validateAlert('Success')


@when(u'go to checkout')
def step_impl(context):
    header = HeaderComponent(context)
    cartShopping = CartShoppingPage(context)
    header.clickCartShopping()
    cartShopping.clickCheckout()


@when(u'fill the checkout form "{country}" "{state}"')
def step_impl(context,country,state):
    checkoutPage = CheckoutPage(context)
    checkoutPage.fillForm(country, state)
    checkoutPage.clickContinue()
    checkoutPage.clickContinueShipping()
    checkoutPage.clickContinueShippingMethod()
    checkoutPage.clickCheckoutTerms()
    checkoutPage.clickContinuePaymentMethod()
    checkoutPage.clickConfirmOrder()


@then(u'the user purchase the product')
def step_impl(context):
    pass
