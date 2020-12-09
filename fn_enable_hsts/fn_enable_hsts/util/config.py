# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_enable_hsts"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_enable_hsts when called by `resilient-circuits config [-c|-u]`
    """
    config_data = None

#    config_data = u"""[fn_enable_hsts]
#setting=xxx
#"""
    return config_data
