# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import pandas as pd
import os
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

PACKAGE_NAME = "fn_notify_user"

f = pd.read_csv(os.path.dirname(__file__)+'/labIP.csv')

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'CSCC_notify_user''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})
        self.f = f

    def convert_ipv4(self, ip):
        try:
            return tuple(int(n) for n in ip.split('.'))
        except:
            print(ip)

    def check_ipv4_in(self, addr, start, end):
        return self.convert_ipv4(start) <= self.convert_ipv4(addr) <= self.convert_ipv4(end)

    def find_name(self, target, *args, **kwargs):

        for index, ip in enumerate(self.f['IP']):
            ips = ip.split('--')
            try:
                start = ips[0]
                end = ips[1]
            except:
                start = ips[0]
                end = ips[0]

            if self.check_ipv4_in(target, start, end):
                return(f['des'][index])
        return 'UNKNOWN'       
      

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("CSCC_notify_user")
    def _CSCC_notify_user_function(self, event, *args, **kwargs):
        """Function: None"""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'CSCC_notify_user' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)

            artifacts = self.rest_client().get("/incidents/{}/artifacts".format(incident_id))
            results = {"names": []}
            for a in artifacts:
                log.debug(a)
                if a["type"] != 1:
                    continue
                else:
                    log.info("target value: %s", a["value"])
                    name = self.find_name(a["value"])
                    a["description"] = name
                    self.rest_client().put("/incidents/{}/artifacts/{}".format(incident_id, a["id"]), a)
                    results["names"].append(name)


            yield StatusMessage("Finished 'CSCC_notify_user' that was running in workflow '{0}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
