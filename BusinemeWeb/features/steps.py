from lettuce import *
from lettuce import steps
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
    name = "/"
    full_url = django_url(name)
    world.browser.response = world.browser.visit(full_url)


@step('I type "(.*)" in the field "(.*)"')
def i_type_value_in_the_field_field_name(step, value, field_name):
    world.browser.fill(field_name, value)


@step('I press "(.*)"')
def i_press(step, button):
    world.browser.find_by_value(button).first.click()


@step('And I should see "(.*)"')
def i_should_see(step, value):
    world.browser.find_by_value(value).first


@step('I should see a description saying "(.*)"')
def i_should_see(step, value):
    header = world.browser.find_by_tag('h4')[0]  # first result
    assert header.text == value

@step('I press "Busca Avancada"')
def i_press_advanced_search(step):
	world.browser.click_link_by_href("/busca_avancada/")


@step('I should see a message saying "Erro"')
def i_should_see(step):
    world.browser.find_by_css("h2").first.value

@step('Then I should see "(.*)"')
def then_i_should_see(step, value):
    world.browser.find_by_css('h3').first.value


