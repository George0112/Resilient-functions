# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import os

PACKAGE_NAME = "fn_enable_hsts"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_disable_hsts''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("fn_disable_hsts")
    def _fn_disable_hsts_function(self, event, *args, **kwargs):
        """Function: None"""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'fn_disable_hsts' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:

            log = logging.getLogger(__name__)
            os.system('ssh chao@140.114.79.72 /snap/bin/kubectl apply -f /home/chao/digi/nginx-configmap-without-hsts.yaml')

            yield StatusMessage("Finished 'fn_disable_hsts' that was running in workflow '{0}'".format(wf_instance_id))

            results = {
                "content": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
