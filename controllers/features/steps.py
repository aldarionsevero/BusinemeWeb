from lettuce import *
from lettuce.django import django_url
from lxml import html
#from django.test.client import Client
from nose.tools import assert_equals
from splinter.browser import Browser

@before.all
def set_browser():
    world.browser = Browser('zope.testbrowser')


@step('I am on Busine.me home page')
def i_am_on_busineme_home_page(step):
    name = "/"
    full_url = django_url(name)
    world.browser.response = world.browser.visit(full_url)

@step('I type "(.*)" in the field search lines')
def i_type_value_in_the_field_search_lines(step, value):
    world.browser.fill("busline", value)

@step('When I press "(.*)"')
def when_i_press_search(step,button):
    world.browser.find_by_name('pesquisar').first.click()

@step('Then I should see "(.*)"')
def then_i_should_see(step, value):
    world.browser.find_by_css('h1').first
@step('And I should see "(.*)"')
def and_i_should_see(step, value):
    world.browser.find_by_css('h3').first.value