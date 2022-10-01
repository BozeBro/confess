"""
LINK: https://docs.google.com/forms/d/e/1FAIpQLScjF-ucQg74uK3LTr2TGiBmKw2zPN0kfnB593Z6k8FoebseRg/viewform?usp=sf_link
Use this link for testing. Development.
Need to change the LINK, folder_id, form_id
"""
from cliforms import *
from drive import uploadImgs
from post import saveImgs
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"
FORM_ID = r"1FAIpQLScjF-ucQg74uK3LTr2TGiBmKw2zPN0kfnB593Z6k8FoebseRg"
SCOPES = [
    "https://www.googleapis.com/auth/forms.responses.readonly", 
    "https://www.googleapis.com/auth/forms.currentonly", 
    "https://www.googleapis.com/auth/forms",
    'https://www.googleapis.com/auth/script.projects',
    "https://www.googleapis.com/auth/drive"
    ]
SCRIPT_ID = "AKfycbzZAg_kQ4u8SxviDCKdQ_SuQ9SVLPmV-KDTawQOmYy3or-_ryb6GItJ_CI4wcg7ni2X"
FOLDER_ID = "1tZ-TyWn8gBbh3fH4H6gEm89p2XTNH5k8"

def main():
    resp = getResponses(FORM_ID, DISCOVERY_DOC, SCOPES)
    if resp:
        imgs = list(transformRes(resp))
        names = makeNames(len(imgs))
        saveImgs(imgs)
        uploadImgs(FOLDER_ID, imgs, names, SCOPES)
        deletePosts(FORM_ID, SCRIPT_ID, SCOPES)

main()
