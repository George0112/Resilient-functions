# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import requests
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

PACKAGE_NAME = "fn_check_hsts"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_check_hsts''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    def has_hsts(self, site):
        """
        Connect to target site and check its headers."
        """
        try:
            req = requests.get('https://' + site, verify=False)
        except requests.exceptions.SSLError as error:
            print("doesn't have SSL working properly (%s)" % (error, ))
            return False
        if 'strict-transport-security' in req.headers:
            print("HSTS is working properly")
            return True
        else:
            print("HSTS can't be found in the header")
            return False

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("fn_check_hsts")
    def _fn_check_hsts_function(self, event, *args, **kwargs):
        """Function: None"""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'fn_check_hsts' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            domain_name = kwargs.get("domain_name")  # text

            log = logging.getLogger(__name__)
            log.info("domain_name: %s", domain_name)

            result = self.has_hsts(domain_name)

            results = {
                "has_hsts": result
            }

            yield StatusMessage("Finished 'fn_check_hsts' that was running in workflow '{0}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
