import logging

import sentry_sdk
from aprsd import messaging, plugin
from oslo_config import cfg
from sentry_sdk.integrations.flask import FlaskIntegration

import aprsd_sentry_plugin
from aprsd_sentry_plugin.conf import sentry as sentry_conf


CONF = cfg.CONF
LOG = logging.getLogger("APRSD")


class SentryPlugin(plugin.APRSDPluginBase):

    enabled = False

    def setup(self):
        """Allows the plugin to do some 'setup' type checks in here.

        If the setup checks fail, set the self.enabled = False.  This
        will prevent the plugin from being called when packets are
        received."""
        # Do some checks here?
        if CONF.aprsd_sentry_plugin.dsn == sentry_conf.DEFAULT_DSN:
            LOG.error(
                "Using default DSN for Sentry.  "
                "Please set services.sentry.dsn in config file.",
            )
            self.enabled = False
            return

        dsn = CONF.aprsd_sentry_plugin.dsn
        LOG.info(f"Initializing Sentry to DSN {dsn}")

        sentry_sdk.init(
            dsn=dsn,
            # Set traces_sample_rate to 1.0 to capture 100%
            # of transactions for performance monitoring.
            # We recommend adjusting this value in production.
            traces_sample_rate=1.0,
            integrations=[FlaskIntegration()],
            release=f"APRSD_SENTRY@{aprsd_sentry_plugin.__version__}",
        )
        self.enabled = True

    def filter(self, packet):
        return messaging.NULL_MESSAGE

    def process(self, packet):
        pass
