# -*- coding: utf-8 -*-
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Static files configurations and directories

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), )
TEMPLATE_DIRS = (os.path.join(BASE_DIR, "templates"), )
