from __future__ import print_function

from googleapiclient.discovery import build
from google_util.post import makeManyIMG

from typing import List
from google_util.goo_utils import getcreds

def getResponses(my_form_id: str, discovery: str, scopes: str):
    creds = getcreds(scopes)
    with open("./token.json", "w") as token:
        token.write(creds.to_json())
    with build("forms", "v1", credentials=creds, discoveryServiceUrl=discovery) as user:
        resps = user.forms().responses().list(formId=my_form_id).execute()
    return resps


def makeNames(n: int) -> List[str]:
    with open("./counter.txt") as f:
        val = f.read().strip()
        counter = 0
        if val.isnumeric():
            counter = int(val)
    names = []
    for i in range(n):
        names.append(f"img{counter + i}.png")
    return names


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
