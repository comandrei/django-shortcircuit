import mock

from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase
from django.test.utils import override_settings

from shortcircuit.middleware import ShortcutCircuit


def mock_view(request):
    return "View Result"

class MiddlewareTest(TestCase):

    def setUp(self):
        super(MiddlewareTest, self).setUp()
        self.middleware = ShortcutCircuit()
        self.request = mock.Mock()
        self.request._shortcircuit = False
        self.request.path = '/'

    def test_regular_view(self):
        self.assertIsNone(self.middleware.process_view(self.request, mock_view, [], {}))

    @override_settings(SHORTCIRCUIT_URL_PATTERNS=[r'^/'])
    def test_shortcircuited_view(self):
        self.middleware.process_request(self.request)
        self.assertEqual(self.middleware.process_view(self.request, mock_view, [], {}), "View Result")
    @override_settings(SHORTCIRCUIT_URL_PATTERNS="mistake")
    def test_invalid_config(self):
        with self.assertRaises(ImproperlyConfigured):
            self.middleware.process_request(self.request)
