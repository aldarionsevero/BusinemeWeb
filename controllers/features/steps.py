from lettuce import *
from lettuce.django import django_url
from lxml import html
from django.test.client import Client
from nose.tools import assert_equals
#from splinter.browser import Browser

@before.all
def set_browser():
    world.browser = Client()


@step('I am on Busine.me home page')
def i_am_on_busineme_home_page(step):
    name = "/"
    full_url = django_url(name)
    world.browser.response = world.browser.get(full_url)

@step('I type "(.*)" in the field search lines')
def i_type_value_in_the_field_search_lines(step, value):
    pass
