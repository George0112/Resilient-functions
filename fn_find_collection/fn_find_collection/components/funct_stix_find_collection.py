# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import json
import os

PACKAGE_NAME = "fn_find_collection"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'stix_find_collection''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("stix_find_collection")
    def _stix_find_collection_function(self, event, *args, **kwargs):
        """Function: None"""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'stix_find_collection' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            artifact_value = kwargs.get("artifact_value")  # string

            log = logging.getLogger(__name__)
            log.info("artifact_value: %s", artifact_value)

            ##############################################
            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
            ##############################################
            involved_collections = []
            query_ip = "2.35.192.209"
            dir_path = os.path.dirname(__file__)
            for file in sorted(os.listdir(os.path.join(dir_path, 'xfe'))):
                try:
                    with open(os.path.join(dir_path, "xfe/%s" %(file)), 'r') as f:
                        try:
                            data = json.load(f)
                            if(file == 'public.json'):
                                ID=data['id']
                            else:
                                ID = data['custom_objects'][0]['id']
                        except:
                            print('cant load json')
                            continue
                        try:
                            for obj in data['objects']:
                                if obj['type'] == 'indicator' and ('pattern' in obj):
                                    index = obj['pattern'].split(" ").index("=")
                                    if query_ip in obj['pattern'].split(" ")[index+1]:
                                        involved_collections.append(ID)
                                    pass
                                else:
                                    print(obj['type'])
                        except:
                            print('cant find objects')
                            print(obj)
                            continue
                except:
            #         print(file)
                    continue
            print(involved_collections)
            

            yield StatusMessage("Finished 'stix_find_collection' that was running in workflow '{0}'".format(wf_instance_id))

            #rp = ResultPayload(PACKAGE_NAME, **kwargs)

            results = {
                'involved_collections': involved_collections
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
