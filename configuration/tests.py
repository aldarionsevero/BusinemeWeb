# -*- coding: utf-8 -*-

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=api,importer',
    '--cover-erase',
    '--cover-min-percentage=80',
]
