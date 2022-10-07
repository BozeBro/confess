from flask import Flask, request
from main1 import deleteConfessions
from google_util.post import makeManyIMG, saveImgs
from google_util.cliforms import makeNames
from google_util.drive import uploadImgs
import json
import glob
import os

app = Flask(__name__)

"""
JSON FORMAT
{
    "ids" : [...]
}
"""


def deleteConfessions(path: str):
    files = glob.glob(path + "/*")
    for f in files:
        os.remove(f)


@app.route("/get_image", methods=["POST"])
def get_image():
    posts = request.get_json(force=True)
    if posts:
        with open("google_file_info/google_test.json") as file:
            data = json.load(file)
        with open("constants.json") as file:
            constants = json.load(file)
        folder_id = data["folder_id"]
        scopes = constants["scopes"]
        imgs = list(makeManyIMG(posts["confessions"]))
        names = makeNames(len(imgs))
        saveImgs(imgs)
        uploadImgs(folder_id, imgs, names, scopes)
        deleteConfessions("./confessions")
        return "true"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
