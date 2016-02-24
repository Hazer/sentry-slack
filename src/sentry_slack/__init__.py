try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('sentry-slack').version
except Exception, e:
    VERSION = 'unknown'
from __future__ import absolute_import

from sentry.plugins import register

from .plugin import SlackPlugin

register(SlackPlugin)