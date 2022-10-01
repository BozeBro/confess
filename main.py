"""
LINK: https://docs.google.com/forms/d/e/1FAIpQLSe_fRARQb7S8Q5Y0O86vgaGueYNxQRGbZwbTa3keSR_fyMk8w/viewform?usp=sf_link

"""
from cliforms import *

DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"
FORM_ID = r"1wSbJXHo-a3VgWktVMTrQhA3a1E_bGRHq5vsuoeMw24w"
SCOPES = [
    "https://www.googleapis.com/auth/forms.responses.readonly", 
    "https://www.googleapis.com/auth/forms.currentonly", 
    "https://www.googleapis.com/auth/forms",
    'https://www.googleapis.com/auth/script.projects'
    ]
SCRIPT_ID="AKfycbzZAg_kQ4u8SxviDCKdQ_SuQ9SVLPmV-KDTawQOmYy3or-_ryb6GItJ_CI4wcg7ni2X"

def main():
    resp = getResponses(FORM_ID, DISCOVERY_DOC, SCOPES)
    if resp:
        imgs = transformRes(resp)
        saveImgs(imgs)
        deletePosts(FORM_ID, SCRIPT_ID, SCOPES)