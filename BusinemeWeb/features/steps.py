from lettuce import *
from lettuce.django import django_url
from lxml import html
#from django.test.client import Client
from nose.tools import assert_equals
from splinter.browser import Browser
from splinter.driver.zopetestbrowser import ZopeTestBrowser


@before.all
def set_browser():
    world.browser = Browser('zope.testbrowser')


@step(r'I am on Busine.me homepage')
def i_am_on_busineme_home_page(step):
    """ Verify if the actual page is the homepage of the application. """

    name = "/"
    full_url = django_url(name)
    world.browser.response = world.browser.visit(full_url)


@step('I type "(.*)" in the field "(.*)"')
def i_type_value_in_the_field_field_name(step, value, field_name):
    """ Enter the predefined values on predefined field. """

    world.browser.fill(field_name, value)


@step('I press "(.*)"')
def i_press(step, button):
    """ Activate the predefined button. """

    world.browser.find_by_value(button).first.click()


@step('And I should see "(.*)"')
def i_should_see(step, value):
    """
    Verify if the header text of the actual page\
    matches the predefined string for this field.
    """

    world.browser.find_by_value(value).first


@step('I should see a description saying "(.*)"')
def i_should_see_a_description(step, value):
    """
    Verify if the displayed description string matches\
    with the expected description string for this field.
    """

    header = world.browser.find_by_tag('h4')[0]  # first result
    assert header.text == value


@step('I press "Busca Avancada"')
def i_press_advanced_search(step):
    """
    Verify if when the advanced search button is activated\
    the "/busca_avancada/" url is called.
    """

    world.browser.click_link_by_href("/busca_avancada/")


@step('I should see a message saying "Erro"')
def i_should_see_an_error_message(step):
    """
    Verify if the message that was displayed starts\
    with the predefined string for this field.
    """

    world.browser.find_by_css("h2").first.value


@step('Then I should see "(.*)"')
def then_i_should_see(step, value):
    """
    Verify if the displayed description string matches\
    with the expected description string for this field.
    """

    world.browser.find_by_css('h3').first.value
