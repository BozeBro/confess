from google_util.cliforms import *
from google_util.drive import uploadImgs
from google_util.post import saveImgs
import os
import glob
import json


def main(env="DEV", folder="./confessions"):
    if env == "PROD":
        with open("google_file_info/google.json") as file:
            data = json.load(file)
    elif env == "DEV":
        with open("google_file_info/google_test.json") as file:
            data = json.load(file)
    with open("google_file_info/constants.json") as file:
            constants = json.load(file)
    form_id = data["form_id"]
    folder_id = data["folder_id"]

    discovery_doc = constants["discovery_doc"]
    scopes = constants["old_scopes"]
    script_id = constants["script_id"]

    resp = getResponses(form_id, discovery_doc, scopes, True)
    if resp:
        imgs = list(transformRes(resp))
        names = makeNames(len(imgs))
        print(len(imgs))
        saveImgs(imgs, folder, names)
        uploadImgs(folder_id, folder, scopes, True)
        deletePosts(form_id, script_id, scopes)
        deleteConfessions(folder)


def deleteConfessions(path: str):
    files = glob.glob(path + "/*")
    for f in files:
        os.remove(f)


def getPosts(form_id: str, discover: str, scopes: List[str]):
    resps = getResponses(form_id, discover, scopes)
    print(resps)

if __name__ == "__main__":
    main("PROD")