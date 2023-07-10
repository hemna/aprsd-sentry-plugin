from oslo_config import cfg

from aprsd_sentry_plugin.conf import sentry


CONF = cfg.CONF
sentry.register_opts(CONF)
