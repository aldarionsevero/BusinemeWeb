"""
Django settings for BusinemeWeb project.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import apps
import databases
import security
import statics

# Security configurations
SECRET_KEY = security.SECRET_KEY
DEBUG = security.DEBUG
TEMPLATE_DEBUG = security.TEMPLATE_DEBUG
ALLOWED_HOSTS = security.ALLOWED_HOSTS

# Application definition
INSTALLED_APPS = apps.INSTALLED_APPS
MIDDLEWARE_CLASSES = apps.MIDDLEWARE_CLASSES

# Default URLs
ROOT_URLCONF = 'BusinemeWeb.urls'

# WSGI
WSGI_APPLICATION = 'BusinemeWeb.wsgi.application'

# Database configuration
DATABASES = databases.DATABASES

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files
STATIC_URL = statics.STATIC_URL
STATIC_ROOT = statics.STATIC_ROOT
STATICFILES_DIRS = statics.STATICFILES_DIRS
TEMPLATE_DIRS = statics.TEMPLATE_DIRS
