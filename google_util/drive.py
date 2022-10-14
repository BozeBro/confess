from __future__ import print_function

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload, MediaIoBaseUpload
from PIL import Image
from google_util.goo_utils import getcreds, getservice
import os.path
from datetime import datetime
import io
def uploadImg(folder_id, folder, img_name, scopes, oauth):
    if oauth:
        creds = getcreds(scopes)
    else:
        creds = getservice(scopes)
    service = build("drive", "v3", credentials=creds)

    file_metadata = {"name": img_name, "parents": [folder_id]}
    media = MediaFileUpload(
        os.path.join(folder, img_name), mimetype="image/png", resumable=True
    )
    file = (
        service.files()
        .create(body=file_metadata, media_body=media, fields="id")
        .execute()
    )
def uploadImgsV2(folder_id, imgs, scopes, oauth = False, creds = None):
    if creds is None:
        if oauth:
            creds = getcreds(scopes)
        else:
            creds = getservice(scopes)
    service = build("drive", "v3", credentials=creds)
    date = str(datetime.now())
    # [f"{date}+{i}.png" for i in range(n)]
    for ind, img in enumerate(imgs):
        name = f"{date}+{ind}.png"
        bytesIO = io.BytesIO()
        img.save(bytesIO, format="PNG")
        media = MediaIoBaseUpload(bytesIO, "image/png", -1, True)
        file_metadata = {"name": name, "parents": [folder_id]}
        file = (
            service.files()
            .create(body=file_metadata, media_body=media, fields="id")
            .execute()
        )
def uploadImgs(folder_id, folder, scopes, oauth=False):
    for file in os.scandir(folder):
        uploadImg(folder_id, folder, os.path.basename(file.name), scopes, oauth)
