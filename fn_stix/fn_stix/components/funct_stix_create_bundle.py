# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

from stix2 import DomainName, File, IPv4Address
from stix2 import (ObjectPath, EqualityComparisonExpression, ObservationExpression,
                   GreaterThanComparisonExpression, IsSubsetComparisonExpression,
                   FloatConstant, StringConstant)

PACKAGE_NAME = "fn_stix"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'stix_create_bundle''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("stix_create_bundle")
    def _stix_create_bundle_function(self, event, *args, **kwargs):
        """Function: None"""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'stix_create_bundle' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)

            artifacts = self.rest_client().get("/incidents/{}/artifacts".format(incident_id))
            results = {"patterns": []}
            patterns = []
            for a in artifacts:
                log.debug(a)
                if a['type'] == 1: # ip address
                    obj = ObjectPath("ipv4-addr", ["value"])
                    pattern = ObservationExpression(EqualityComparisonExpression(lhs, "140.114.79.72"))
                    info.debug("append pattern %s", pattern)
                    patterns.append(pattern)
                else if a['type'] == 
                

            yield StatusMessage("Finished 'stix_create_bundle' that was running in workflow '{0}'".format(wf_instance_id))

            results = {
                "content": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult({"patterns": patterns})
        except Exception:
            yield FunctionError()
