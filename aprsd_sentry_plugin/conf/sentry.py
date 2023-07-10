from oslo_config import cfg


DEFAULT_DSN = "Set the DSN"

sentry_group = cfg.OptGroup(
    name="aprsd_sentry_plugin",
    title="APRSD Sentry Plugin settings",
)

sentry_opts = [
    cfg.StrOpt(
        "dsn",
        default=DEFAULT_DSN,
        help="The Sentry DSN(url) of the running Sentry instance.  "
             "https://docs.sentry.io/product/sentry-basics/dsn-explainer/",
    ),
]

ALL_OPTS = (
    sentry_opts
)


def register_opts(cfg):
    cfg.register_group(sentry_group)
    cfg.register_opts(ALL_OPTS, group=sentry_group)


def list_opts():
    return {
        sentry_group.name: ALL_OPTS,
    }
