from __future__ import print_function

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from PIL import Image
from cliforms import getcreds
import json

def uploadImg(folder_id, img, img_name, scopes):
    creds = getcreds(scopes)
    service = build("drive", "v3", credentials=creds)

    file_metadata = {"name": img_name, "parents": [folder_id]}
    media = MediaFileUpload(
        "./confessions/" + img_name, mimetype="image/png", resumable=True
    )
    file = (
        service.files()
        .create(body=file_metadata, media_body=media, fields="id")
        .execute()
    )


def uploadImgs(folder_id, imgs, img_names, scopes):
    for img, name in zip(imgs, img_names):
        uploadImg(folder_id, img, name, scopes)


if __name__ == "__main__":
    scopes = ["https://www.googleapis.com/auth/drive"]
    img = Image.open("./confessions/img0.png")
    data = img.getdata()
    name = "img0.png"
    with open("google_test.json") as f:
        data = json.load(f)
    uploadImg(data["folder_id"], data, name, scopes)
