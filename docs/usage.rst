========
Usage
========


Include it in your middleware classes, BEFORE middlewares you potentially want skipped
::
   MIDDLEWARE_CLASSES = ( ... 'shorcircuit.middleware.ShortCircuitMiddleware', ... )

Define a list of urlpatterns you want skipped

::
   SHORTCIRCUIT_URL_PATTERNS = (r'^/skip_me', r'^/also_me')

