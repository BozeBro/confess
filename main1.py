from google_util.cliforms import *
from google_util.drive import uploadImgsV2
from google_util.goo_utils import service_account, getcreds
import json


def main(env="DEV"):
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
    creds = getcreds(scopes)
    resp = getResponses(form_id, discovery_doc, scopes, creds=creds)
    if resp:
        print(len(resp["responses"]))
        imgs = transformRes(resp)
        uploadImgsV2(folder_id, imgs, scopes, creds=creds)
        deletePosts(form_id, script_id, scopes)


if __name__ == "__main__":
    main("PROD")
