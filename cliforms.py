from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from httplib2 import Http
from post import makeManyIMG, saveImgs

from typing import List


def getcreds(scopes: List[str]) -> Credentials:
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", scopes)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds


def getResponses(my_form_id: str, discovery: str, scopes: str):
    creds = getcreds(scopes)
    with open("token.json", "w") as token:
        token.write(creds.to_json())
    with build("forms", "v1", credentials=creds, discoveryServiceUrl=discovery) as user:
        resps = user.forms().responses().list(formId=my_form_id).execute()
    return resps


def makeNames(n: int) -> List[str]:
    with open("counter.txt") as f:
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
    names = []
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
    req = {"function": "myFunction", "parameters": [form_id]}

    res = service.scripts().run(body=req, scriptId=scriptId).execute()
