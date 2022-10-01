from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client import client, file, tools
from post import makeManyIMG
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"
FORM_ID = r"1wSbJXHo-a3VgWktVMTrQhA3a1E_bGRHq5vsuoeMw24w"
SCOPES = [
    "https://www.googleapis.com/auth/forms.currentonly", 
    "https://www.googleapis.com/auth/forms"
    ]
def getResponses(my_form_id : str):
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    with build("forms", "v1", credentials=creds, discoveryServiceUrl=DISCOVERY_DOC) as user:
        forms = user.forms()
        responses = forms.responses().list(formId=my_form_id).execute()
    return responses

def transformRes(responses):
    submissions = []
    for resp in responses["responses"]:
        my_id = list(resp["answers"].keys())[0]
        submission = resp["answers"][my_id]["textAnswers"]["answers"][0]["value"]
        submissions.append(submission)
    makeManyIMG(submissions)

if __name__ == "__main__":
    transformRes(getResponses(FORM_ID))