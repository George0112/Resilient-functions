# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from stix2 import *
import pandas as pd
import os
import numpy as np
import json
from io import BytesIO
from resilient_lib import write_file_attachment

PACKAGE_NAME = "fn_stix"
p = pd.read_csv(os.path.dirname(__file__)+'/stix-mapping.csv', encoding='utf-8')

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'stix_create_bundle''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})
        self.mapping = p

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
            incident_id = kwargs.get("incident_id")  # number

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)

            artifacts = self.rest_client().get("/incidents/{}/artifacts".format(incident_id))
            patterns = []
            indicators = []
            for a in artifacts:
                log.debug("artifact: %s", a)
                index = list(np.where(self.mapping['id'] == a['type']))[0][0]
                log.debug("artifact mapping index: ", index)
                row = self.mapping.iloc[index]
                if index and row['object'] is not np.nan and row['property'] is not np.nan:
                    try:
                        obj = ObjectPath(row["object"], [str(row["property"])])
                        pattern = ObservationExpression(EqualityComparisonExpression(obj, str(a['value'])))
                        log.debug("append pattern %s", pattern)
                        a["description"] = str(pattern)
                        self.rest_client().put("/incidents/{}/artifacts/{}".format(incident_id, a["id"]), a)
                        patterns.append(str(pattern))
                    except UnicodeEncodeError:
                         continue
            for p in patterns:
                indicators.append(Indicator(pattern_type='stix', pattern=p))
            
            log.debug('indicators: ', indicators)
            
            # Create new bundle
            bundle = Bundle(*indicators)

            # Upload attachment
            datastream = BytesIO(str(bundle))
            client = self.rest_client()
            new_attachment = write_file_attachment(client, 'bundle_' + str(incident_id) + '.json', datastream, incident_id)

            yield StatusMessage("Finished 'stix_create_bundle' that was running in workflow '{0}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult({"patterns": patterns})
        except Exception:
            yield FunctionError()
