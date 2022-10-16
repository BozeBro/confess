from __future__ import print_function

from googleapiclient.discovery import build
from google_util.post import makeManyIMG

from google_util.goo_utils import getcreds, getservice


def getResponses(my_form_id: str, discovery: str, scopes: str, oauth=False, creds=None):
    if not creds:
        if oauth:
            creds = getcreds(scopes)
            with open("./token.json", "w") as token:
                token.write(creds.to_json())
        else:
            creds = getservice(scopes)
    with build("forms", "v1", credentials=creds, discoveryServiceUrl=discovery) as user:
        resps = user.forms().responses().list(formId=my_form_id).execute()
    return resps


def transformRes(responses):
    submissions = []
    for resp in responses["responses"]:
        my_id = list(resp["answers"].keys())[0]
        submission = resp["answers"][my_id]["textAnswers"]["answers"][0]["value"]
        submissions.append(submission)
    return makeManyIMG(submissions)


# Deploy ID AKfycbzZAg_kQ4u8SxviDCKdQ_SuQ9SVLPmV-KDTawQOmYy3or-_ryb6GItJ_CI4wcg7ni2X
# URL https://script.googleapis.com/v1/scripts/AKfycbzZAg_kQ4u8SxviDCKdQ_SuQ9SVLPmV-KDTawQOmYy3or-_ryb6GItJ_CI4wcg7ni2X:run
def deletePosts(form_id: str, scriptId: str, scopes: str) -> None:
    creds = getcreds(scopes)

    service = build("script", "v1", credentials=creds)
    req = {"function": "deleteSubmissions", "parameters": [form_id]}

    res = service.scripts().run(body=req, scriptId=scriptId).execute()
    print(res)
