from flask import Flask, request
from google_util.drive import uploadImgsV2
from google_util.goo_utils import getservice
from google_util.post import makeManyIMG
import json

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def get_image(env="PROD"):
    if request.method == 'GET':
        return "Hello World"
    if env == "PROD":
        with open("google_file_info/google.json") as file:
            data = json.load(file)
    elif env == "DEV":
        with open("google_file_info/google_test.json") as file:
            data = json.load(file)
    with open("google_file_info/constants.json") as file:
        constants = json.load(file)
    folder_id = data["folder_id"]
    scopes = constants["scopes"]
    creds = getservice(scopes)
    if 'confessions' not in request.json:
        return "Need a confessions key"
    imgs = makeManyIMG(request.json['confessions'])
    uploadImgsV2(folder_id, imgs, scopes, creds=creds)
    return "DONE"
"""
@app.route("/test", methods=["POST", "GET"])
def get_test(env="DEV"):
    if request.method == "GET":
        return "THIS IS A TEST"
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
    scopes = constants["scopes"]
    script_id = constants["script_id"]
    creds = getservice(scopes)
    # resp = getResponses(form_id, discovery_doc, scopes, creds=creds)
    print(request.json)
    confessions = request.json["confessions"]
    imgs = makeManyIMG(confessions)
    uploadImgsV2(folder_id, imgs, scopes, creds=creds)
    return "DONE"
"""
if __name__ == "__main__":
    localhost = "127.0.0.1"
    host = "0.0.0.0"
    app.run(host=host, port=8080, debug=True)
