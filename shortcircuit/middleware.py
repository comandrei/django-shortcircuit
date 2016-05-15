import re

from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


class ShortcutCircuit(object):

    def process_request(self, request):
        short_patterns = getattr(settings, 'SHORTCIRCUIT_URL_PATTERNS', [])
        if hasattr(short_patterns, '__iter__'):
            if any(re.match(pattern, request.path) for pattern in short_patterns):
                setattr(request, '_shortcircuit', True)
        else:
            raise ImproperlyConfigured("SHORTCIRCUIT_URL_PATTERNS must be an interable, got '{}'".format(short_patterns))


    def process_view(self, request, view_func, view_args, view_kwargs):
        if hasattr(request, '_shortcircuit') and request._shortcircuit == True:
            return view_func(request, *view_args, **view_kwargs)
