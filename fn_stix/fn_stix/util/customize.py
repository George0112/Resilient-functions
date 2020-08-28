# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_stix"""

try:
    from resilient import ImportDefinition
except ImportError:
    # Support Apps running on resilient-circuits < v35.0.195
    from resilient_circuits.util import ImportDefinition


def codegen_reload_data():
    """
    Parameters required reload codegen for the fn_stix package
    """
    return {
        "package": u"fn_stix",
        "message_destinations": [u"fn_stix"],
        "functions": [u"stix_create_bundle"],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    Contents:
    - Message Destinations:
        - fn_stix
    - Functions:
        - stix_create_bundle
    """

    yield ImportDefinition(u"""
eyJpbmNpZGVudF90eXBlcyI6IFt7ImNyZWF0ZV9kYXRlIjogMTU5ODU4Mzk0NDY0NSwgImRlc2Ny
aXB0aW9uIjogIkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJleHBvcnRfa2V5
IjogIkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJpZCI6IDAsICJuYW1lIjog
IkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJ1cGRhdGVfZGF0ZSI6IDE1OTg1
ODM5NDQ2NDUsICJ1dWlkIjogImJmZWVjMmQ0LTM3NzAtMTFlOC1hZDM5LTRhMDAwNDA0NGFhMCIs
ICJlbmFibGVkIjogZmFsc2UsICJzeXN0ZW0iOiBmYWxzZSwgInBhcmVudF9pZCI6IG51bGwsICJo
aWRkZW4iOiBmYWxzZX1dLCAibG9jYWxlIjogbnVsbCwgInNjcmlwdHMiOiBbXSwgImFjdGlvbnMi
OiBbXSwgImxheW91dHMiOiBbXSwgImV4cG9ydF9mb3JtYXRfdmVyc2lvbiI6IDIsICJpZCI6IDEx
LCAiaW5kdXN0cmllcyI6IG51bGwsICJmdW5jdGlvbnMiOiBbeyJkaXNwbGF5X25hbWUiOiAiU1RJ
WDogY3JlYXRlIGJ1bmRsZSIsICJkZXNjcmlwdGlvbiI6IHsiY29udGVudCI6IG51bGwsICJmb3Jt
YXQiOiAidGV4dCJ9LCAidGFncyI6IFtdLCAidmlld19pdGVtcyI6IFtdLCAiY3JlYXRvciI6IHsi
ZGlzcGxheV9uYW1lIjogImNoYW93ZW4gXHU5NjczIiwgInR5cGUiOiAidXNlciIsICJpZCI6IDks
ICJuYW1lIjogImNoYW93ZW5AZGVtby5jb20ifSwgImV4cG9ydF9rZXkiOiAic3RpeF9jcmVhdGVf
YnVuZGxlIiwgImxhc3RfbW9kaWZpZWRfYnkiOiB7ImRpc3BsYXlfbmFtZSI6ICJjaGFvd2VuIFx1
OTY3MyIsICJ0eXBlIjogInVzZXIiLCAiaWQiOiA5LCAibmFtZSI6ICJjaGFvd2VuQGRlbW8uY29t
In0sICJuYW1lIjogInN0aXhfY3JlYXRlX2J1bmRsZSIsICJ2ZXJzaW9uIjogMSwgIndvcmtmbG93
cyI6IFtdLCAibGFzdF9tb2RpZmllZF90aW1lIjogMTU5ODU4MzY5NjM1NCwgImRlc3RpbmF0aW9u
X2hhbmRsZSI6ICJmbl9zdGl4IiwgImlkIjogMjYsICJ1dWlkIjogIjFmZDBiOTZmLTNmMmUtNDhl
My1iMTRiLWY4NTQzNjUzY2ZkMCJ9XSwgImFjdGlvbl9vcmRlciI6IFtdLCAiZ2VvcyI6IG51bGws
ICJ0YWdzIjogW10sICJhcHBzIjogW10sICJ0YXNrX29yZGVyIjogW10sICJzZXJ2ZXJfdmVyc2lv
biI6IHsibWFqb3IiOiAzOCwgInZlcnNpb24iOiAiMzguMC42MDA2IiwgImJ1aWxkX251bWJlciI6
IDYwMDYsICJtaW5vciI6IDB9LCAidGltZWZyYW1lcyI6IG51bGwsICJ3b3Jrc3BhY2VzIjogW10s
ICJpbmJvdW5kX21haWxib3hlcyI6IG51bGwsICJhdXRvbWF0aWNfdGFza3MiOiBbXSwgInBoYXNl
cyI6IFtdLCAibm90aWZpY2F0aW9ucyI6IG51bGwsICJyZWd1bGF0b3JzIjogbnVsbCwgImdyb3Vw
cyI6IG51bGwsICJ3b3JrZmxvd3MiOiBbXSwgInR5cGVzIjogW10sICJtZXNzYWdlX2Rlc3RpbmF0
aW9ucyI6IFt7InV1aWQiOiAiZDk4NzE5NzQtZjlmOS00ZTYzLTk0NDktZmU3NWIyNjA0MzIyIiwg
Im5hbWUiOiAiZm5fc3RpeCIsICJ0YWdzIjogW10sICJleHBvcnRfa2V5IjogImZuX3N0aXgiLCAi
ZXhwZWN0X2FjayI6IHRydWUsICJkZXN0aW5hdGlvbl90eXBlIjogMCwgInVzZXJzIjogWyJjaGFv
d2VuQGV4YW1wbGUuY29tIiwgImNoYW93ZW5AZGVtby5jb20iXSwgImFwaV9rZXlzIjogW10sICJw
cm9ncmFtbWF0aWNfbmFtZSI6ICJmbl9zdGl4In1dLCAiaW5jaWRlbnRfYXJ0aWZhY3RfdHlwZXMi
OiBbXSwgInJvbGVzIjogW10sICJmaWVsZHMiOiBbeyJyZWFkX29ubHkiOiB0cnVlLCAiaW50ZXJu
YWwiOiB0cnVlLCAibmFtZSI6ICJpbnRlcm5hbF9jdXN0b21pemF0aW9uc19maWVsZCIsICJ0ZXh0
IjogIkN1c3RvbWl6YXRpb25zIEZpZWxkIChpbnRlcm5hbCkiLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0
IiwgInR5cGVfaWQiOiAwLCAiZXhwb3J0X2tleSI6ICJpbmNpZGVudC9pbnRlcm5hbF9jdXN0b21p
emF0aW9uc19maWVsZCIsICJpZCI6IDAsICJ1dWlkIjogImJmZWVjMmQ0LTM3NzAtMTFlOC1hZDM5
LTRhMDAwNDA0NGFhMSJ9XSwgIm92ZXJyaWRlcyI6IFtdLCAiZXhwb3J0X2RhdGUiOiAxNTk4NTgz
OTQ1NTgwfQ==
""")
