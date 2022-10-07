"""
LINK: https://docs.google.com/forms/d/e/1FAIpQLSe_fRARQb7S8Q5Y0O86vgaGueYNxQRGbZwbTa3keSR_fyMk8w/viewform?usp=sf_link

"""
from google_util.cliforms import *
from google_util.drive import uploadImgs
from google_util.post import saveImgs
import os
import glob
import json


def main():
    with open("google_file_info/google.json") as file:
        data = json.load(file)
    with open("google_file_info/constants.json") as file:
        constants = json.load(file)
    form_id = data["form_id"]
    folder_id = data["folder_id"]

    discovery_doc = constants["discovery_doc"]
    scopes = constants["scopes"]
    script_id = constants["script_id"]

    resp = getResponses(form_id, discovery_doc, scopes)
    if resp:
        imgs = list(transformRes(resp))
        names = makeNames(len(imgs))
        print(len(imgs))
        saveImgs(imgs)
        uploadImgs(folder_id, imgs, names, scopes)
        deletePosts(form_id, script_id, scopes)
        deleteConfessions("./confessions")


def deleteConfessions(path: str):
    files = glob.glob(path + "/*")
    for f in files:
        os.remove(f)


def getPosts(form_id: str, discover: str, scopes: List[str]):
    resps = getResponses(form_id, discover, scopes)
    print(resps)


if __name__ == "__main__":
    main()