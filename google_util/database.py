from unicodedata import name
from google.cloud import datastore
from typing import List
datastore_client = datastore.Client()
def makeNames(n: int) -> List[str]:
    key = datastore_client.key('tracker', 'counter')
    counter = datastore_client.get(key)
    names = [f"img{i+counter['count']}.png" for i in range(n)]
    return names

def saveImgs(imgs, names):
    datastore_client = datastore.Client()
    key = datastore_client.key('tracker', 'counter')
    counter = datastore_client.get(key)

    for img,name in zip(imgs,names):
        img.save(f"./confessions/{name}.png")
    counter['count'] += len(imgs)
    datastore_client.put(counter)
