# -*- coding: utf-8 -*-
from django.conf import settings as d_settings
from django.core.exceptions import ImproperlyConfigured
from moderatormodels import *
from pagemodel import *
from permissionmodels import *
from placeholdermodel import *
from pluginmodel import *
from titlemodels import *
# must be last
from cms import signals as s_import

def validate_settings():
    if not "django.core.context_processors.request" in d_settings.TEMPLATE_CONTEXT_PROCESSORS:
        raise ImproperlyConfigured('django-cms needs django.core.context_processors.request in settings.TEMPLATE_CONTEXT_PROCESSORS to work correctly.')
    if not 'mptt' in d_settings.INSTALLED_APPS:
        raise ImproperlyConfigured('django-cms needs django-mptt installed.')
    
def validate_dependencies():
    # check for right version of reversions
    if 'reversion' in d_settings.INSTALLED_APPS:
        from reversion.admin import VersionAdmin
        if not hasattr(VersionAdmin, 'get_urls'):
            raise ImproperlyConfigured('django-cms requires never version of reversion (VersionAdmin must contain get_urls method)')

validate_dependencies()
validate_settings()
