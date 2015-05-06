# -*- coding: utf-8 -*-

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--logging-level=ERROR',
    '--with-coverage',
    '--cover-package=BusinemeWeb',
    '--cover-erase',
    '--cover-min-percentage=80',
]
