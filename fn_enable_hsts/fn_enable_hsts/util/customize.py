# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_enable_hsts"""

try:
    from resilient import ImportDefinition
except ImportError:
    # Support Apps running on resilient-circuits < v35.0.195
    from resilient_circuits.util import ImportDefinition


def codegen_reload_data():
    """
    Parameters required reload codegen for the fn_enable_hsts package
    """
    return {
        "package": u"fn_enable_hsts",
        "message_destinations": [u"fn_enable_hsts"],
        "functions": [u"fn_enable_hsts"],
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
        - fn_enable_hsts
    - Functions:
        - fn_enable_hsts
    """

    yield ImportDefinition(u"""
eyJpbmNpZGVudF90eXBlcyI6IFt7ImNyZWF0ZV9kYXRlIjogMTYwNjkwODk2NzM0NCwgImRlc2Ny
aXB0aW9uIjogIkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJleHBvcnRfa2V5
IjogIkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJpZCI6IDAsICJuYW1lIjog
IkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJ1cGRhdGVfZGF0ZSI6IDE2MDY5
MDg5NjczNDQsICJ1dWlkIjogImJmZWVjMmQ0LTM3NzAtMTFlOC1hZDM5LTRhMDAwNDA0NGFhMCIs
ICJlbmFibGVkIjogZmFsc2UsICJzeXN0ZW0iOiBmYWxzZSwgInBhcmVudF9pZCI6IG51bGwsICJo
aWRkZW4iOiBmYWxzZX1dLCAibG9jYWxlIjogbnVsbCwgInNjcmlwdHMiOiBbXSwgImFjdGlvbnMi
OiBbXSwgImxheW91dHMiOiBbXSwgImV4cG9ydF9mb3JtYXRfdmVyc2lvbiI6IDIsICJpZCI6IDcs
ICJpbmR1c3RyaWVzIjogbnVsbCwgImZ1bmN0aW9ucyI6IFt7ImRpc3BsYXlfbmFtZSI6ICJmbl9l
bmFibGVfaHN0cyIsICJkZXNjcmlwdGlvbiI6IHsiY29udGVudCI6IG51bGwsICJmb3JtYXQiOiAi
dGV4dCJ9LCAidGFncyI6IFtdLCAidmlld19pdGVtcyI6IFtdLCAiY3JlYXRvciI6IHsiZGlzcGxh
eV9uYW1lIjogIkNoYW8gV2VuIENoZW4iLCAidHlwZSI6ICJ1c2VyIiwgImlkIjogNSwgIm5hbWUi
OiAiY2hhb3dlbkBkZW1vLmNvbSJ9LCAiZXhwb3J0X2tleSI6ICJmbl9lbmFibGVfaHN0cyIsICJs
YXN0X21vZGlmaWVkX2J5IjogeyJkaXNwbGF5X25hbWUiOiAiQ2hhbyBXZW4gQ2hlbiIsICJ0eXBl
IjogInVzZXIiLCAiaWQiOiA1LCAibmFtZSI6ICJjaGFvd2VuQGRlbW8uY29tIn0sICJuYW1lIjog
ImZuX2VuYWJsZV9oc3RzIiwgInZlcnNpb24iOiAxLCAid29ya2Zsb3dzIjogW10sICJsYXN0X21v
ZGlmaWVkX3RpbWUiOiAxNjA2OTA4OTU5MjY2LCAiZGVzdGluYXRpb25faGFuZGxlIjogImZuX2Vu
YWJsZV9oc3RzIiwgImlkIjogNTUsICJ1dWlkIjogIjc1NzQ2OWVmLWU1NGEtNDQ1Ny1iNGFmLTky
MTc0YzUyMzUwNyJ9XSwgImFjdGlvbl9vcmRlciI6IFtdLCAiZ2VvcyI6IG51bGwsICJ0YWdzIjog
W10sICJhcHBzIjogW10sICJ0YXNrX29yZGVyIjogW10sICJzZXJ2ZXJfdmVyc2lvbiI6IHsibWFq
b3IiOiAzOCwgInZlcnNpb24iOiAiMzguMC42MDA2IiwgImJ1aWxkX251bWJlciI6IDYwMDYsICJt
aW5vciI6IDB9LCAidGltZWZyYW1lcyI6IG51bGwsICJ3b3Jrc3BhY2VzIjogW10sICJpbmJvdW5k
X21haWxib3hlcyI6IG51bGwsICJhdXRvbWF0aWNfdGFza3MiOiBbXSwgInBoYXNlcyI6IFtdLCAi
bm90aWZpY2F0aW9ucyI6IG51bGwsICJyZWd1bGF0b3JzIjogbnVsbCwgImdyb3VwcyI6IG51bGws
ICJ3b3JrZmxvd3MiOiBbXSwgInR5cGVzIjogW10sICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFt7
InV1aWQiOiAiZjUwNmI5MjMtNDkwZS00ZDA4LThlMDItYmY2YmE3ZTVmNGM0IiwgIm5hbWUiOiAi
Zm5fZW5hYmxlX2hzdHMiLCAidGFncyI6IFtdLCAiZXhwb3J0X2tleSI6ICJmbl9lbmFibGVfaHN0
cyIsICJleHBlY3RfYWNrIjogdHJ1ZSwgImRlc3RpbmF0aW9uX3R5cGUiOiAwLCAidXNlcnMiOiBb
ImNoYW93ZW5AZGVtby5jb20iLCAidXNlcjRAZGVtby5jb20iLCAidXNlcjJAZGVtby5jb20iLCAi
dXNlcjFAZGVtby5jb20iXSwgImFwaV9rZXlzIjogWyI5YzEyZTg3MS03NjRkLTRiMTgtYjVlZC1l
ODY5MmE4NzY4YTIiXSwgInByb2dyYW1tYXRpY19uYW1lIjogImZuX2VuYWJsZV9oc3RzIn1dLCAi
aW5jaWRlbnRfYXJ0aWZhY3RfdHlwZXMiOiBbXSwgInJvbGVzIjogW10sICJmaWVsZHMiOiBbeyJy
ZWFkX29ubHkiOiB0cnVlLCAiaW50ZXJuYWwiOiB0cnVlLCAibmFtZSI6ICJpbnRlcm5hbF9jdXN0
b21pemF0aW9uc19maWVsZCIsICJ0ZXh0IjogIkN1c3RvbWl6YXRpb25zIEZpZWxkIChpbnRlcm5h
bCkiLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgInR5cGVfaWQiOiAwLCAiZXhwb3J0X2tleSI6ICJp
bmNpZGVudC9pbnRlcm5hbF9jdXN0b21pemF0aW9uc19maWVsZCIsICJpZCI6IDAsICJ1dWlkIjog
ImJmZWVjMmQ0LTM3NzAtMTFlOC1hZDM5LTRhMDAwNDA0NGFhMSJ9XSwgIm92ZXJyaWRlcyI6IFtd
LCAiZXhwb3J0X2RhdGUiOiAxNjA2OTA4OTY3NzI4fQ==
""")
