import requests
import base64
import json
collections = requests.get("https://api.xforce.ibmcloud.com/taxii2/collections", auth=(API_KEY, API_SECRET))

collections = collections.json()
collections['collections']

import os
dir_path = os.path.dirname(os.path.realpath('xfe'))
fail_collection = ['botnets', 'industries', 'malware_analyses', 'threat_groups', 'threats']
col = {}
for collection in collections['collections']:
    if(collection['id'] in fail_collection):
        continue
    objects = requests.get("https://api.xforce.ibmcloud.com/taxii2/collections/{}/objects".format(collection['id']), 
                           auth=('de60ff0f-2958-4554-b35a-76fa29641929', 'd7063403-436d-4e60-9ae4-38e0e238f0f0'))
    if objects.status_code != 200:
        print('id {} query failed'.format(collection['id']))
        continue
    else:
        objects = objects.json()
        print(collection['id'])
        with open(os.path.join(dir_path, './xfe/{}.json'.format(collection['id'])), 'w') as f:
            json.dump(objects, f, indent=4)
