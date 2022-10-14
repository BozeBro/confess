from __future__ import print_function

from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from google_util.goo_utils import getcreds, getservice
from datetime import datetime
import io


def uploadImgsV2(folder_id, imgs, scopes, oauth=False, creds=None):
    if creds is None:
        if oauth:
            creds = getcreds(scopes)
        else:
            creds = getservice(scopes)
    service = build("drive", "v3", credentials=creds)
    date = str(datetime.now())
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
