"""
LINK: https://docs.google.com/forms/d/e/1FAIpQLSe_fRARQb7S8Q5Y0O86vgaGueYNxQRGbZwbTa3keSR_fyMk8w/viewform?usp=sf_link

"""
from __future__ import print_function
import json
from apiclient.discovery import build
from google.oauth2 import service_account
from post import makeManyIMG
SCOPES = ["https://www.googleapis.com/auth/forms.responses.readonly", "https://www.googleapis.com/auth/forms.currentonly", "https://www.googleapis.com/auth/forms"]
FORM_ID = r"1wSbJXHo-a3VgWktVMTrQhA3a1E_bGRHq5vsuoeMw24w"

def getResponses(my_form_id : str):
    credentials = service_account.Credentials.from_service_account_file(
    './service_secret.json')
    scoped_creds = credentials.with_scopes(SCOPES)
    with build('forms', 'v1', credentials=scoped_creds) as service:
        forms = service.forms()
        responses = forms.responses().list(formId=my_form_id).execute()
    return responses
def foo():
    # example of how to read json format
    with open("example.json", "r") as file:
        obj = json.load(file)
        submissions = []
        for resp in obj["responses"]:
            my_id = list(resp["answers"].keys())[0]
            submission = resp["answers"][my_id]["textAnswers"]["answers"][0]["value"]
            submissions.append(submission)
        makeManyIMG(submissions)
def transformRes(responses):
    submissions = []
    for resp in responses["responses"]:
        my_id = list(resp["answers"].keys())[0]
        submission = resp["answers"][my_id]["textAnswers"]["answers"][0]["value"]
        submissions.append(submission)
    makeManyIMG(submissions)

if __name__ == "__main__":
    resps = getResponses(FORM_ID)
    transformRes(resps)