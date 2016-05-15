import re

from django.conf import settings

class ShortcutCircuit(object):

    def process_request(self, request):
        if any(re.match(pattern, request.path) for pattern in settings.SHORTCIRCUIT_URL_PATTERNS):
            setattr(request, '_shortcircuit', True)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if hasattr(request, '_shortcircuit') and request._shortcircuit == True:
            return view_func(request, *view_args, **view_kwargs)
