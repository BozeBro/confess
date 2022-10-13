from __future__ import print_function

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from PIL import Image
from google_util.goo_utils import getcreds, getservice
import os.path
import json


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


def uploadImgs(folder_id, folder, img_names, scopes, oauth=False):
    for name in img_names:
        uploadImg(folder_id, folder, name, scopes, oauth)
