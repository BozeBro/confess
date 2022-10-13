from google.cloud import datastore

datastore_client = datastore.Client()

def init():
    key = datastore_client.key('tracker', 'counter')
    store = datastore.Entity(key=key)
    store['count'] = 0
    datastore_client.put(store)
def update():
    key = datastore_client.key('tracker', 'counter')
    counter = datastore_client.get(key)
    counter['count'] += 1
    datastore_client.put(counter)
def get():
    key = datastore_client.key('tracker', 'counter')
    counter = datastore_client.get(key)
    print(counter['count'])
init()
update()
get()