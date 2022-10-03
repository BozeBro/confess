"""
FORM LINK : https://forms.gle/8B6tirfz8E5qydZ26
"""
from cliforms import *
from drive import uploadImgs
from post import saveImgs
import os 
import glob
import json


def main():
    with open("google_test.json") as file:
        data = json.load(file)
    with open("constants.json") as file:
        constants = json.load(file)
    form_id = data["form_id"]
    folder_id = data["folder_id"]

    discovery_doc = constants["discovery_doc"]
    scopes = constants["scopes"]
    script_id  = constants["script_id"]
    
    resp = getResponses(form_id, discovery_doc, scopes)
    if resp:
        imgs = list(transformRes(resp))
        names = makeNames(len(imgs))
        print(len(imgs))
        saveImgs(imgs)
        uploadImgs(folder_id, imgs, names, scopes)
        deletePosts(form_id, script_id, scopes)
        deleteConfessions("./confessions")
def deleteConfessions(path):
    files = glob.glob(path + "/*")
    for f in files:
        os.remove(f)
def getPosts(form_id, discover, scopes):
    resps = getResponses(form_id, discover, scopes)
    print(resps)


if __name__ == "__main__":
    main()
